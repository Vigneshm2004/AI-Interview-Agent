# 🎓 QUICK REFERENCE CARD

## Commands You Need

### Setup (One Time)

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Run Agent

```bash
python interview_agent.py
```

### Push to GitHub

```bash
git add .
git commit -m "Your message"
git push origin main
```

---

## File Locations

| What         | Where                          |
| ------------ | ------------------------------ |
| Main Code    | `interview_agent.py`           |
| Dependencies | `requirements.txt`             |
| Setup Guide  | `README.md` or `QUICKSTART.md` |
| API Keys     | `.env` (your computer only)    |
| Key Template | `.env.example` (in GitHub)     |

---

## Important: .env Structure

```env
GEMINI_API_KEY="your_key_here"
AZURE_SPEECH_KEY="your_key_here"
AZURE_SPEECH_REGION="eastus"
```

**⚠️ NEVER put real .env in GitHub!**

---

## 3 Interview Roles

1. **Software Engineer**

   - Algorithms, System Design, Collaboration

2. **Sales Representative**

   - Communication, CRM, Target Achievement

3. **Retail Associate** ⭐ (Use this for demo)
   - Customer Service, Product Knowledge, Operations

---

## Demo Script

```
Run: python interview_agent.py
Select: 3 (Retail)
Answer: 2 questions about customer service
Type: END INTERVIEW
Show: Feedback JSON
```

**Duration**: 2-3 minutes

---

## Safety Checklist

- [ ] .env exists locally
- [ ] .env NOT in GitHub
- [ ] .env.example IS in GitHub
- [ ] .gitignore has `.env`
- [ ] API keys are secret

---

## Files to Ignore (Not in GitHub)

```
.env                ← Your API keys (SAFE!)
venv/              ← Virtual environment
__pycache__/       ← Python cache
test_input.txt     ← Test files
```

---

## Files to Commit (In GitHub)

```
interview_agent.py          ✅
requirements.txt            ✅
README.md                   ✅
QUICKSTART.md              ✅
.gitignore                 ✅
.env.example               ✅
LICENSE                    ✅
CONTRIBUTING.md            ✅
```

---

## Documentation Files

| File                | Purpose             |
| ------------------- | ------------------- |
| README.md           | Complete guide      |
| QUICKSTART.md       | Fast setup          |
| CONTRIBUTING.md     | Dev guide           |
| GITHUB_SAFETY.md    | Security            |
| FINAL_SUBMISSION.md | This entire package |

---

## Roles in Code

```python
ROLE_DATA = {
    "1": {"role": "Software Engineer", ...},
    "2": {"role": "Sales Representative", ...},
    "3": {"role": "Retail Associate", ...}
}
```

---

## Interview Flow

1. User selects role
2. Agent starts interview
3. Agent asks Q1
4. User answers
5. Agent asks follow-up
6. User answers
7. Repeat Q2-Q3
8. Type: END INTERVIEW
9. Get JSON feedback
10. Feedback saved to file

---

## Feedback Structure

```json
{
  "summary_score": 4.2,
  "overall_summary": "...",
  "criteria_scores": [
    {
      "criterion": "Customer Service",
      "score": 4.5,
      "justification": "..."
    }
  ],
  "areas_for_improvement": ["..."]
}
```

---

## Key Features Explained

| Feature      | Why              | Where                        |
| ------------ | ---------------- | ---------------------------- |
| **Roles**    | Adaptability     | ROLE_DATA (line 150)         |
| **Memory**   | Smart follow-ups | LangChain (line 65)          |
| **Feedback** | Intelligence     | generate_feedback (line 95)  |
| **Voice**    | Interaction      | Azure integration (line 190) |
| **Pydantic** | Structure        | Schema (line 5-40)           |

---

## Troubleshooting

**Q: ModuleNotFoundError?**
A: Run `pip install -r requirements.txt`

**Q: Azure not working?**
A: Check .env file has correct keys

**Q: No feedback?**
A: Verify Gemini API key is valid

**Q: .env appearing in GitHub?**
A: Stop! Check .gitignore and remove from git

---

## Git Verification

```bash
# Check what's being tracked
git status
# .env should show as "Untracked" (NOT "to be committed")

# See all tracked files
git ls-files
# Should NOT include .env or venv/
```

---

## Before Demo Video

- [ ] Code runs without errors
- [ ] Roles appear when selected
- [ ] Agent asks role-specific questions
- [ ] Feedback JSON is generated
- [ ] All documentation is readable

---

## Demo Highlights

1. Show role selection menu
2. Ask 2 questions
3. Get feedback with scores
4. Show GitHub repo
5. Mention "MIT License" + "Open to contributions"

---

## Success Criteria

✅ All 10 steps work  
✅ Feedback is JSON formatted  
✅ .env is not on GitHub  
✅ README explains everything  
✅ Demo video is clear

---

## Links to Remember

- **Repo**: https://github.com/Vigneshm2004/AI-Interview-Agent
- **Gemini**: https://ai.google.dev/
- **Azure**: https://portal.azure.com/
- **MIT License**: https://opensource.org/licenses/MIT

---

## Post-Launch

1. Add video link to README
2. Get stars on GitHub ⭐
3. Accept contributions
4. Respond to issues
5. Keep dependencies updated

---

## You've Got This! 🚀

Everything is ready. Just:

1. Test it works
2. Record demo
3. Push to GitHub
4. Share the link

**Good luck!** ✨
