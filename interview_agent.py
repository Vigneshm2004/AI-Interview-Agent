import os
import json
from dotenv import load_dotenv
from typing import List, Optional
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import JsonOutputParser
# Azure Speech SDK import
import azure.cognitiveservices.speech as speechsdk

# Load environment variables
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash" # Using the cost-effective model

# --- Pydantic Schema for Structured Feedback ---
class CriteriaScore(BaseModel):
    """Schema for individual criterion score."""
    criterion: str = Field(description="The criterion being scored (e.g., Communication, Technical Knowledge).")
    score: float = Field(description="Score between 0.0 and 5.0.", ge=0.0, le=5.0)
    justification: str = Field(description="Specific examples from their answers to justify the score.")

class InterviewFeedback(BaseModel):
    """The final structured feedback schema."""
    summary_score: float = Field(description="Overall summary score between 0.0 and 5.0.", ge=0.0, le=5.0)
    overall_summary: str = Field(description="A paragraph summarizing the overall interview performance.")
    criteria_scores: List[CriteriaScore] = Field(description="List of detailed scores for each criterion.")
    areas_for_improvement: List[str] = Field(description="List of actionable suggestions for improvement.")
# ---------------------------------------------

# 1. INITIALIZE MODEL AND MEMORY
llm = ChatGoogleGenerativeAI(model=MODEL_NAME, api_key=GEMINI_KEY)
# Memory is CRITICAL for follow-up questions
chat_history = ChatMessageHistory()

# 2. DEFINE THE CORE AGENT SYSTEM PROMPT
# This defines the persona and rules for the agent
SYSTEM_INSTRUCTION = """
You are an expert Interview Practice Partner AI Agent. Your sole purpose is to conduct mock job interviews based on the user-specified role and its key attributes.

Job Role: {job_role}
Key Attributes to Assess: {attributes}

RULES OF ENGAGEMENT:
1. Maintain a professional, formal, and encouraging tone.
2. Conduct the interview ONE QUESTION at a time. Wait for the user's full answer before proceeding.
3. Crucially: Based on the user's answer and the attributes, generate a relevant, probing FOLLOW-UP question (max 1 follow-up per main question) to demonstrate depth and interactivity.
4. Only ask the next MAIN question after the current question and follow-up are exhausted.
5. If the user goes off-topic, gently redirect them back to the current interview question.
6. Start by asking the user to confirm the role and then ask the first MAIN question.
"""

# 3. CREATE THE PROMPT TEMPLATE
# The template includes the system instruction, the memory (history), and the new human input.
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_INSTRUCTION),
        MessagesPlaceholder(variable_name="chat_history"), # Stores the conversation history
        ("human", "{human_input}"),
    ]
)

# 4. CREATE THE CONVERSATIONAL CHAIN using LCEL
def get_chain(job_role, attributes):
    """Create a chain with the job role and attributes"""
    def format_input(input_dict):
        messages = chat_history.messages.copy()
        formatted = {
            "chat_history": messages,
            "human_input": input_dict["human_input"],
            "job_role": job_role,
            "attributes": attributes
        }
        return formatted
    
    chain = (
        RunnablePassthrough() | format_input
        | prompt
        | llm
    )
    return chain

# 5. FEEDBACK GENERATION FUNCTION
def generate_feedback(llm, full_transcript, job_role, attributes):
    """
    Generate structured feedback based on the interview conversation transcript.
    
    Args:
        llm: The language model instance
        full_transcript: The full interview transcript as a string
        job_role: The job role being interviewed for
        attributes: Key attributes being assessed
    
    Returns:
        dict: Structured feedback as a dictionary (JSON-compatible)
    """
    parser = JsonOutputParser(pydantic_object=InterviewFeedback)

    # Use a powerful, dedicated prompt for analysis
    FEEDBACK_PROMPT = """
    You are a Performance Analyst. Your task is to analyze the full interview transcript provided below and generate a detailed feedback report.

    Job Role: {job_role}
    Key Attributes Assessed: {attributes}
    
    TRANSCRIPT:
    ---
    {transcript}
    ---

    INSTRUCTIONS:
    1. **Strictly** follow the required JSON output format defined by the schema.
    2. Score the candidate based on the Key Attributes (for Technical Knowledge) and overall coherence (for Communication).
    3. Ensure the 'justification' fields are specific, referencing points from the transcript.
    4. Provide actionable suggestions in 'areas_for_improvement'.

    {format_instructions}
    """
    
    # Create the feedback prompt template
    feedback_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=FEEDBACK_PROMPT),
            HumanMessage(content="Generate the interview feedback now."),
        ]
    ).partial(format_instructions=parser.get_format_instructions())

    # Create the final chain (Prompt -> LLM -> Parser)
    feedback_chain = feedback_template | llm | parser

    try:
        feedback_data = feedback_chain.invoke(
            {
                "transcript": full_transcript,
                "job_role": job_role,
                "attributes": attributes
            }
        )
        return feedback_data
    except Exception as e:
        print(f"\n--- ERROR DURING FEEDBACK GENERATION ---")
        print(f"Failed to generate structured feedback: {e}")
        return None

# --- ROLE DATA STRUCTURE (From Step 2) ---
ROLE_DATA = {
    "1": {
        "role": "Software Engineer",
        "attributes": "Algorithms, System Design, Collaboration",
        "description": "Prepare for technical interviews focusing on coding and system architecture."
    },
    "2": {
        "role": "Sales Representative / Sales Executive",
        "attributes": "Communication & Persuasion, Customer Relationship Management, Target Achievement & Negotiation",
        "description": "Practice behavioral and situational questions related to closing deals and managing clients."
    },
    "3": {
        "role": "Retail Associate",
        "attributes": "Customer Service & Engagement, Product Knowledge & Merchandising, POS Handling & Store Operations",
        "description": "Focus on customer interaction, conflict resolution, and store operational scenarios."
    }
}
# ----------------------------------------

# 6. AZURE VOICE FUNCTIONS
def configure_speech():
    """
    Configure Azure Speech Service using credentials from .env file.
    Returns speech_config object if successful, None otherwise.
    """
    try:
        speech_key = os.getenv("AZURE_SPEECH_KEY")
        speech_region = os.getenv("AZURE_SPEECH_REGION")
        
        if not speech_key or not speech_region:
            print("[WARNING] AZURE_SPEECH_KEY or AZURE_SPEECH_REGION not found in .env file.")
            return None
        
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
        return speech_config
    except Exception as e:
        print(f"[ERROR] Failed to configure Azure Speech: {e}")
        return None

def agent_speak(speech_config, text):
    """
    Convert agent's text response to speech using Azure Text-to-Speech.
    
    Args:
        speech_config: Azure Speech configuration object
        text: The text to be spoken
    """
    if not speech_config:
        # Fallback to text output if speech config is not available
        print(f"\nAgent: {text}")
        return
    
    try:
        # Use neural voice for better quality
        speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
        
        # Also print the text for reference
        print(f"\nAgent: {text}")
        
        # Synthesize and play the speech
        result = synthesizer.speak_text_async(text).get()
        
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            pass  # Success - audio played
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speechsdk.CancellationDetails(result)
            print(f"[WARNING] Speech synthesis canceled: {cancellation_details.reason}")
    except Exception as e:
        print(f"[WARNING] Speech synthesis failed: {e}")
        print(f"Agent (text): {text}")

def user_listen(speech_config):
    """
    Capture user's voice input using Azure Speech-to-Text.
    Falls back to text input if speech config is not available or recognition fails.
    
    Args:
        speech_config: Azure Speech configuration object
    
    Returns:
        str: The recognized text or typed input
    """
    if not speech_config:
        # Fallback to text input
        return input("\nYou: ")
    
    try:
        # Configure speech recognition
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=speech_config, 
            audio_config=audio_config
        )
        
        print("\nYou (Voice): Speak now, or press Enter to type...")
        
        # Start recognition
        result = speech_recognizer.recognize_once_async().get()
        
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            recognized_text = result.text.strip()
            if recognized_text:
                print(f"You said: {recognized_text}")
                return recognized_text
            else:
                # Empty recognition, fall back to text input
                return input("You (Text): ")
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("[No speech detected. Falling back to text input.]")
            return input("You (Text): ")
        else:
            # Recognition canceled or error, fall back to text input
            return input("You (Text): ")
    except Exception as e:
        print(f"[WARNING] Speech recognition failed: {e}")
        return input("You (Text): ")

# 7. EXECUTION LOOP (Voice/Chat Interface)
def run_interview():
    print("--- Interview Partner Agent Initialized ---")
    
    # --- NEW: Configure speech ---
    speech_config = configure_speech()
    if speech_config:
        print("[SUCCESS] Azure Speech Service is active (Voice preferred mode).")
    else:
        print("[WARNING] Azure Speech config failed. Running in chat-only mode.")
    
    print("Enter 'END INTERVIEW' to stop the session and get feedback.")
    print("-" * 40)
    
    # --- NEW: Role Selection Logic ---
    print("\nPlease select the job role for your practice interview:")
    for key, data in ROLE_DATA.items():
        print(f"  {key}. {data['role']} - ({data['description']})")
    
    selected_key = ""
    while selected_key not in ROLE_DATA:
        selected_key = input("Enter the number (1, 2, or 3) for your choice: ").strip()
        if selected_key not in ROLE_DATA:
            print("Invalid choice. Please enter 1, 2, or 3.")
            
    # Define role and attributes based on user's choice
    selected_role_data = ROLE_DATA[selected_key]
    job_role = selected_role_data['role']
    attributes = selected_role_data['attributes']
    
    print(f"\n[Agent: Initializing interview for {job_role}.]")
    # -----------------------------------
    
    # Create the chain
    chain = get_chain(job_role, attributes)
    
    # Prepare the initial context
    initial_input = f"Start the mock interview for a {job_role} focusing on {attributes}. My name is Alex. The agent MUST ask the first question immediately."
    
    # Start the conversation
    response = chain.invoke({"human_input": initial_input})
    agent_response = response.content
    
    # Add to history
    chat_history.add_user_message(initial_input)
    chat_history.add_ai_message(agent_response)
    
    # --- NEW: Use voice function for Agent's first response ---
    agent_speak(speech_config, agent_response)
    
    while True:
        # --- NEW: Use voice function for User input ---
        user_input = user_listen(speech_config)
        
        if user_input.upper() == 'END INTERVIEW':
            print("\n" + "=" * 50)
            print("|| Generating Final Feedback Report... ||")
            print("=" * 50)
            
            # Extract the full conversation history from memory
            full_transcript = "\n".join([
                f"[{'Interviewer' if isinstance(msg, AIMessage) else 'Candidate'}]: {msg.content}"
                for msg in chat_history.messages
            ])

            # Call the feedback function
            feedback_report = generate_feedback(llm, full_transcript, job_role, attributes)
            
            if feedback_report:
                # Pretty print the structured JSON feedback for display
                print("\n" + "=" * 50)
                print("📊 INTERVIEW FEEDBACK REPORT")
                print("=" * 50)
                print(json.dumps(feedback_report, indent=4))
                
                # Save feedback to JSON file
                output_file = "interview_feedback.json"
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(feedback_report, f, indent=4, ensure_ascii=False)
                
                print(f"\n💾 Feedback saved to: {output_file}")
            
            print("\n--- Interview Session Ended ---")
            break
            
        # Continue the conversation
        response = chain.invoke({"human_input": user_input})
        agent_response = response.content
        
        # Add to history
        chat_history.add_user_message(user_input)
        chat_history.add_ai_message(agent_response)
        
        # --- NEW: Use voice function for Agent's response ---
        agent_speak(speech_config, agent_response)

# Run the interview loop
if __name__ == "__main__":
    run_interview()
