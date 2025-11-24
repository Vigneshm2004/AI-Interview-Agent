
# 🚀 Eightfold.ai - Interview Practice Partner Agent

## Project Overview

A highly adaptable and intelligent conversational AI agent built using **Gemini 2.5 Flash** (via LangChain) and **Azure AI Speech Services**. This agent simulates realistic job interviews for specific roles (e.g., Software Engineer, Sales Executive, Retail Associate) and provides **structured, quantifiable feedback** on candidate performance.

The agent is designed to be:
- **Adaptive**: Dynamically selects roles and tailors questions based on role-specific attributes
- **Intelligent**: Generates context-aware follow-up questions and provides detailed performance analysis
- **Interactive**: Offers voice-preferred interaction with text fallback, creating a natural interview experience
- **Scalable**: Fully containerizable and deployable with minimal API costs using Free Tiers

---


## 🎥 Demo Video (Playable)

Click below to watch the demo video (plays directly in GitHub):

https://raw.githubusercontent.com/Vigneshm2004/AI-Interview-Agent/main/demo%20video.mp4




## 🛠️ Tech Stack & Architecture 

This solution leverages a modern, cost-effective tech stack utilizing generous Free Tiers from Google and Azure.

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Core AI / Logic (LLM)** | Gemini 2.5 Flash (Google GenAI SDK) | Cost-effective with high-quality conversational abilities; Free Tier available |
| **Framework** | LangChain (Python) | Manages conversational history, prompt chaining, and agent persona enforcement |
| **Voice Input (STT)** | Azure AI Speech Service | High accuracy transcription; Always Free (F0 Tier): 5 audio hours/month |
| **Voice Output (TTS)** | Azure AI Speech Service | Neural voice quality; Always Free (F0 Tier): 0.5M characters/month |
| **Development IDE** | Cursor IDE / VS Code | AI-assisted development and rapid iteration |
| **Data Storage** | Local JSON / SQLite (Optional) | Feedback reports saved locally as JSON |

### Architecture Diagram

## 🏗️ Architecture Diagram

![AI Interview Agent Architecture](https://github.com/Vigneshm2004/AI-Interview-Agent/blob/main/ai_architecuture.png)

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INPUT LAYER                            |
├──────────────────────────────────────┬──────────────────────────┤
│  Voice Input (Azure STT)             │  Text Chat Input         │
└──────────────────────────────────────┴──────────────────────────┘
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   INTERVIEW AGENT CORE                          |
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ 1. Role Data Structure (Dynamic Selection)              │    │
│  │    - Software Engineer                                  │    │
│  │    - Sales Representative                               │    │
│  │    - Retail Associate                                   │    │
│  └─────────────────────────────────────────────────────────┘    │
│                         ▼                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ 2. LangChain Conversational Memory & Persona            │    │
│  │    - System Prompt (Role-Specific)                      │    │
│  │    - Chat Message History                               │    │
│  │    - Follow-up Question Generation                      │    │
│  └─────────────────────────────────────────────────────────┘    │
│                         ▼                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ 3. Gemini 2.5 Flash LLM via Google GenAI SDK            │    │
│  │    - Complex conversational logic                       │    │
│  │    - Context-aware question generation                  │    │
│  │    - JSON feedback analysis (Pydantic)                  │    │
│  └─────────────────────────────────────────────────────────┘    │
│                         ▼                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ 4. Structured Feedback Engine (Pydantic Schema)         │    │
│  │    - Criterion-based scoring (0.0-5.0)                  │    │
│  │    - Communication & Technical Knowledge metrics        │    │
│  │    - Actionable improvement suggestions                 │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   AGENT RESPONSE LAYER                          │
├──────────────────────────────────────┬──────────────────────────┤
│  Voice Output (Azure TTS)            │  Chat Output             │
└──────────────────────────────────────┴──────────────────────────┘
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              FEEDBACK GENERATION & PERSISTENCE                  │
├──────────────────────────────────────┬──────────────────────────┤
│  JSON Feedback Report                │  Local Storage           │
│  (interview_feedback.json)           │  (Optional Database)     │
└──────────────────────────────────────┴──────────────────────────┘
```

---

## 🧠 Core Design Decisions & Evaluation Focus

The agent's architecture directly addresses key evaluation criteria:

| Feature Implemented | Evaluation Criterion | Rationale |
|-------------------|-------------------|-----------|
| **Dynamic Role-Based Attributes** | Adaptability, Intelligence | The agent references role-specific attributes (e.g., System Design vs. Target Achievement) to customize questions and score feedback accurately. |
| **Interactive Follow-ups & Memory** | Agentic Behaviour, Conversational Quality | Achieved using LangChain's ConversationBufferMemory to analyze previous answers and generate specific, probing follow-up questions (no static Q&A). |
| **Structured JSON Feedback** | Intelligence, Technical Implementation | Uses Pydantic library to force the LLM to output a fixed JSON schema, guaranteeing consistent, quantifiable scores (0.0-5.0). |
| **Voice-Preferred Integration** | Technical Implementation, Interaction Mode | Integrated Azure STT/TTS into the main loop with text chat fallback. |
| **Modular & Extensible Design** | Code Quality, Scalability | Separated concerns (speech, memory, feedback generation) for easy extension and testing. |

---

## ⚙️ Setup and Execution

### Prerequisites

- **Python 3.9+** (Tested on Python 3.11+)
- **Valid Gemini API Key** (Free Tier available at [Google AI Studio](https://ai.google.dev/))
- **Valid Azure AI Speech Key and Region** (Free Tier: F0 Tier with 5 audio hours/month transcription)
- **Git** (for version control)
- **Virtual Environment** (recommended)

### Step 1: Clone and Environment Setup

```bash
# Clone the repository
git clone https://github.com/Vigneshm2004/AI-Interview-Agent.git
cd AI-Interview-Agent

# Create and activate a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

### Step 3: API Key Configuration

Create a file named `.env` in the root directory:

```bash
touch .env   # macOS/Linux
# OR
New-Item -Path .env   # Windows
```

Add the following environment variables:

```env
# Gemini API Key (for AI Logic via LangChain)
GEMINI_API_KEY="YOUR_GEMINI_KEY_HERE"

# Azure Speech Services (for Voice STT/TTS)
AZURE_SPEECH_KEY="YOUR_AZURE_KEY_HERE"
AZURE_SPEECH_REGION="YOUR_AZURE_REGION_HERE"
```

**Security Note**: The `.env` file is listed in `.gitignore` and will **never be committed** to the repository. Your API keys are safe.

### Step 4: Run the Agent

```bash
python interview_agent.py
```

The agent will:
1. Display available roles (Software Engineer, Sales Representative, Retail Associate)
2. Prompt you to select a role (enter 1, 2, or 3)
3. Initiate the interview in voice-preferred mode (with text fallback)
4. Conduct 2-3 main questions with interactive follow-ups
5. Generate structured JSON feedback when you type `END INTERVIEW`

---

## 📋 Supported Interview Roles

### 1. **Software Engineer**
- **Key Attributes**: Algorithms, System Design, Collaboration
- **Focus**: Technical interviews covering data structures, system architecture, and team collaboration
- **Sample Questions**: 
  - "Describe your approach to solving a complex algorithmic problem."
  - "Walk me through how you would design a scalable microservices architecture."

### 2. **Sales Representative / Sales Executive**
- **Key Attributes**: Communication & Persuasion, Customer Relationship Management, Target Achievement & Negotiation
- **Focus**: Behavioral and situational questions on closing deals and managing clients
- **Sample Questions**:
  - "Tell me about a time you successfully negotiated with a difficult client."
  - "How do you build and maintain strong customer relationships?"

### 3. **Retail Associate**
- **Key Attributes**: Customer Service & Engagement, Product Knowledge & Merchandising, POS Handling & Store Operations
- **Focus**: Customer interaction, conflict resolution, and store operational scenarios
- **Sample Questions**:
  - "How would you handle an upset customer in a high-pressure situation?"
  - "Describe your knowledge of our product line and how you'd recommend items to customers."

---

## 📊 Sample Feedback Output

Upon completing the interview, the agent generates a structured JSON feedback report:

```json
{
  "summary_score": 4.2,
  "overall_summary": "Alex demonstrated strong customer service fundamentals with clear communication and empathy toward customer needs. The responses showed practical understanding of retail operations, though deeper product knowledge and handling of complex scenarios could be improved.",
  "criteria_scores": [
    {
      "criterion": "Customer Service & Engagement",
      "score": 4.5,
      "justification": "Alex clearly articulated understanding of customer needs and demonstrated empathy. The mention of greeting customers with a smile and actively helping shows genuine customer-centric approach."
    },
    {
      "criterion": "Communication & Professionalism",
      "score": 4.0,
      "justification": "Response was well-structured and professional. However, could have included more specific examples of handling difficult situations or upselling opportunities."
    },
    {
      "criterion": "Technical Knowledge",
      "score": 3.5,
      "justification": "General understanding of retail operations demonstrated, but limited mention of POS systems, inventory management, or specific merchandising strategies."
    }
  ],
  "areas_for_improvement": [
    "Develop concrete examples of handling upset or difficult customers with specific de-escalation techniques.",
    "Enhance product knowledge by researching our inventory, unique selling points, and cross-selling opportunities.",
    "Familiarize yourself with POS systems and point-of-sale best practices relevant to modern retail.",
    "Practice structured responses that include specific metrics (e.g., customer satisfaction scores, sales targets)."
  ]
}
```

---

## 🔧 Project Structure

```
AI-Interview-Agent/
├── interview_agent.py           # Main agent script
├── requirements.txt             # Python dependencies
├── .env                         # API keys (Git-ignored for security)
├── .gitignore                   # Git ignore rules
├── README.md                    # This file
├── interview_feedback.json      # Generated feedback reports
└── venv/                        # Virtual environment (Git-ignored)
```

---

## 🚀 Key Features

### 1. **Dynamic Role Selection**
Users select from predefined roles, each with unique attributes and expectations.

### 2. **Conversational Memory**
The agent maintains chat history using LangChain, enabling context-aware follow-up questions.

### 3. **Voice-Preferred Interaction**
- **Input**: Azure Speech-to-Text (STT) with text fallback
- **Output**: Azure Text-to-Speech (TTS) with neural voices
- Graceful degradation if Azure services unavailable

### 4. **Intelligent Question Generation**
- **Main Questions**: Role-based, attribute-focused
- **Follow-up Questions**: Generated dynamically based on user responses
- **No Static Q&A**: Every interaction is contextual

### 5. **Structured Feedback**
- Pydantic-enforced JSON schema ensures consistent output
- Criterion-based scoring (0.0-5.0 scale)
- Actionable improvement suggestions
- Saved as `interview_feedback.json`

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`:

```
python-dotenv==1.0.0
langchain==0.1.0
langchain-google-genai==0.1.0
google-generativeai==0.3.0
pydantic==2.0.0
azure-cognitiveservices-speech==1.36.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🔐 Security Best Practices

1. **Never commit `.env`** - Your API keys are protected by `.gitignore`
2. **Use Free Tiers responsibly** - Monitor your API usage
3. **Rotate keys periodically** - Update `.env` keys every 3-6 months
4. **Keep dependencies updated** - Run `pip install --upgrade -r requirements.txt`

---

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'dotenv'`
**Solution**: Ensure you've activated the virtual environment and installed dependencies:
```bash
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### Issue: `[WARNING] Azure Speech config failed`
**Solution**: 
- Verify `AZURE_SPEECH_KEY` and `AZURE_SPEECH_REGION` in `.env`
- Check Azure account has active Free Tier (F0)
- Fall back to chat-only mode if unavailable

### Issue: Gemini API errors
**Solution**:
- Verify `GEMINI_API_KEY` in `.env`
- Ensure API is enabled in Google Cloud Console
- Check rate limits (Free Tier: 60 requests/minute)

---

## 🎥 Demo Video

**[INSERT LINK TO YOUR PUBLIC DEMO VIDEO HERE]**

*Coming soon: Full walkthrough of agent initialization, role selection, interview flow, and feedback generation*

---

## 📈 Roadmap & Future Enhancements

- [ ] Add more interview roles (Data Scientist, Product Manager, etc.)
- [ ] Implement question difficulty levels (Beginner, Intermediate, Advanced)
- [ ] Add real-time performance dashboard
- [ ] Support for multiple languages
- [ ] Integrate with ATS (Applicant Tracking Systems)
- [ ] Database persistence for historical interviews
- [ ] Multi-interviewer panel simulation

---

## 👨‍💻 Author & Contribution

**Developed by**: Vignesh M  
**Repository**: [GitHub - AI-Interview-Agent](https://github.com/Vigneshm2004/AI-Interview-Agent)

### Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📞 Support

For issues, questions, or suggestions:
- **GitHub Issues**: [AI-Interview-Agent/issues](https://github.com/Vigneshm2004/AI-Interview-Agent/issues)
- **Email**: vigneshm2004@example.com

---

## 🙏 Acknowledgments

- **Google Generative AI** for Gemini 2.5 Flash
- **Microsoft Azure** for Speech Services
- **LangChain** for conversational memory and prompt management
- **Pydantic** for data validation and schema enforcement

---

## 🎯 Evaluation Criteria Checklist

- ✅ **Adaptability**: Dynamic role selection with role-specific attributes
- ✅ **Intelligence**: Structured JSON feedback with criterion-based scoring
- ✅ **Agentic Behaviour**: Interactive follow-ups using conversational memory
- ✅ **Conversational Quality**: Context-aware responses without static Q&A
- ✅ **Technical Implementation**: Voice integration with text fallback
- ✅ **Code Quality**: Modular, well-documented, extensible design

---

**Last Updated**: November 24, 2025  
**Status**: ✅ Production Ready
=============================================================================================================================================================================================================

