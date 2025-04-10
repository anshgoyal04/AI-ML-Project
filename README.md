# AI-ML-Project
# 🤖 TalentScout AI Hiring Assistant

An intelligent AI-powered chatbot that screens tech candidates based on their skills and experience using OpenAI's GPT and Streamlit.

---

##  Features

- Collects candidate information (name, contact, experience, desired role)
- Asks for the candidate’s tech stack
- Generates dynamic technical interview questions using OpenAI GPT-3.5
- Interactive chatbot interface built with Streamlit
- Secure API key handling with `.env`

---

##  Tech Stack

- Python
- Streamlit
- OpenAI GPT API
- Python-dotenv

---

---
##  Challenges & Solutions
- API key exposed on GitHub → Revoked key, added .env to .gitignore

- API version conflict → Downgraded to openai==0.28 for compatibility

- Rate limit/quota error → Created new account with fresh API key

- .env not loading → Ensured correct format, same directory as app.py

---
## File Structure
AI-ML-Project/
├── app.py
├── .env
├── requirements.txt
├── .gitignore
└── README.md

### Clone the repository

```bash
git clone https://github.com/anshgoyal04/AI-ML-Project
cd AI-ML-project

