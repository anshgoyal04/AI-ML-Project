import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables (your OpenAI API key)
load_dotenv()
client = OpenAI()

st.set_page_config(page_title="Hiring Assistant Chatbot", layout="centered")
st.title("🤖 TalentScout - AI Hiring Assistant")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0
if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {}

# Function to generate technical questions
def generate_questions(tech_stack):
    prompt = (
        f"Based on the following tech stack: {tech_stack}, "
        "generate 3-5 technical questions to assess the candidate’s proficiency. "
        "Keep questions relevant and appropriately challenging."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# Main chatbot flow
if st.session_state.step == 0:
    st.write("Hello! 👋 I'm your AI Hiring Assistant from TalentScout.")
    if st.button("Start Screening"):
        st.session_state.step = 1

elif st.session_state.step == 1:
    st.subheader("📋 Candidate Details")
    with st.form("info_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        exp = st.text_input("Years of Experience")
        role = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        submitted = st.form_submit_button("Next")
        if submitted:
            st.session_state.candidate_info.update({
                "Name": name, "Email": email, "Phone": phone,
                "Experience": exp, "Position": role, "Location": location
            })
            st.session_state.step = 2

elif st.session_state.step == 2:
    st.subheader("💻 Declare Your Tech Stack")
    tech_stack = st.text_area("List your tech stack (e.g., Python, React, MySQL)")
    if st.button("Generate Questions"):
        st.session_state.tech_stack = tech_stack
        st.session_state.questions = generate_questions(tech_stack)
        st.session_state.step = 3

elif st.session_state.step == 3:
    st.subheader("🧪 Technical Questions")
    st.markdown(st.session_state.questions)
    if st.button("End Conversation"):
        st.session_state.step = 4

elif st.session_state.step == 4:
    st.success("✅ Thank you! Your details have been submitted.")
    st.balloons()
