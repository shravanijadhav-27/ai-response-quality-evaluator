
import streamlit as st

st.set_page_config(
    page_title="AI Response Quality Evaluator",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Response Quality Evaluator")
st.subheader("Evaluate AI answers. Identify errors. Improve trust.")

st.write(
    """
    Welcome to the AI Response Quality Evaluator Agent.

    This project aims to evaluate AI-generated responses for:
    - Accuracy and reliability
    - Relevance to the question
    - Completeness of the answer
    - Potential hallucinations
    """
)

st.divider()

st.subheader("How it works")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📝 1. Submit")
    st.write("Enter a question and the AI-generated response.")

with col2:
    st.markdown("### 🔍 2. Evaluate")
    st.write("The evaluation system will check the response against reference information.")

with col3:
    st.markdown("### 📊 3. View results")
    st.write("Review evaluation scores and explanations when the backend is connected.")

st.divider()

st.subheader("Get started")
st.write("Open the Evaluation Hub to enter a response.")

if st.button("📝 Open Evaluation Hub", type="primary"):
    st.switch_page("pages/2_Evaluation_Hub.py")
