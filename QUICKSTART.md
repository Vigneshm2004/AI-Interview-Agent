# 🚀 Quick Start Guide - AI Interview Agent

## 5-Minute Setup

### Step 1: Get Your API Keys (2 minutes)

#### Gemini API Key

1. Go to [Google AI Studio](https://ai.google.dev/)
2. Click **Get API Key**
3. Copy the key

#### Azure Speech Key

1. Go to [Azure Portal](https://portal.azure.com/)
2. Create a **Cognitive Services > Speech** resource (F0 Free Tier)
3. Copy Key and Region

### Step 2: Clone & Setup (2 minutes)

```bash
# Clone repository
git clone https://github.com/Vigneshm2004/AI-Interview-Agent.git
cd AI-Interview-Agent

# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate
# OR (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Configure API Keys (1 minute)

Create `.env` file in root directory:

```env
GEMINI_API_KEY="your_key_here"
AZURE_SPEECH_KEY="your_key_here"
AZURE_SPEECH_REGION="eastus"
```

### Step 4: Run Agent (Use immediately!)

```bash
python interview_agent.py
```

---

## Common Issues & Solutions

| Issue                    | Solution                                                  |
| ------------------------ | --------------------------------------------------------- |
| `ModuleNotFoundError`    | Run `pip install -r requirements.txt`                     |
| Azure Speech not working | Check `.env` file and Free Tier status                    |
| No Gemini response       | Verify API key in Google AI Studio                        |
| Can't activate venv      | Try: `python -m venv venv` then `.\venv\Scripts\activate` |

---

## What Happens When You Run It?

1. **Role Selection**: Choose 1 (Software Engineer), 2 (Sales), or 3 (Retail)
2. **Interview Starts**: Agent asks first question with voice output
3. **Your Response**: Speak or type your answer
4. **Follow-ups**: Agent asks deeper questions based on your answers
5. **End Interview**: Type `END INTERVIEW` to get structured feedback
6. **Feedback Report**: JSON file with scores and suggestions

---

## Example Session (Retail Associate)

```
Please select the job role for your practice interview:
  1. Software Engineer - (Prepare for technical interviews...)
  2. Sales Representative / Sales Executive - (Practice behavioral...)
  3. Retail Associate - (Focus on customer interaction...)

Enter the number (1, 2, or 3) for your choice: 3

[Agent: Initializing interview for Retail Associate.]

Agent: Hello Alex, it's a pleasure to conduct this mock interview with
you today for the Retail Associate position. To begin, could you please
tell me about your understanding of excellent customer service in a retail
environment and how you would ensure every customer feels valued and assisted?

You: I believe customer service is about listening to customers and
addressing their needs promptly...

Agent: That's a great perspective! Can you share a specific example from
your experience where you successfully resolved a difficult customer
situation?

You: [Your response]

...

You: END INTERVIEW

|| Generating Final Feedback Report... ||

📊 INTERVIEW FEEDBACK REPORT
{
  "summary_score": 4.2,
  "overall_summary": "Alex demonstrated strong customer service fundamentals...",
  "criteria_scores": [...]
}

💾 Feedback saved to: interview_feedback.json
--- Interview Session Ended ---
```

---

## Next Steps

- ✅ Complete the interview
- 📊 Review your feedback report
- 🎥 Record a demo video
- 🔄 Practice with different roles
- 📤 Push to GitHub

---

**Ready to start? Run `python interview_agent.py` now!** 🎯
