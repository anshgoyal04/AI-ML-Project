import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test whether the API key was loaded correctly
print("Loaded API Key:", os.getenv("OPENAI_API_KEY"))  # ✅ Debugging line

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

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"❌ Error generating questions: {str(e)}"

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
        if tech_stack.strip() == "":
            st.warning("⚠️ Please enter your tech stack before generating questions.")
        else:
            st.session_state.tech_stack = tech_stack
            st.session_state.questions = generate_questions(tech_stack)
            st.session_state.step = 3

elif st.session_state.step == 3:
    st.subheader("🧪 Technical Questions")
    if st.session_state.questions:
        st.markdown(st.session_state.questions)
    else:
        st.warning("⚠️ No questions were generated. Please check your tech stack or try again.")
    if st.button("End Conversation"):
        st.session_state.step = 4

elif st.session_state.step == 4:
    st.success("✅ Thank you! Your details have been submitted.")
    st.balloons()
