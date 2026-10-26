
import streamlit as st

st.set_page_config(
    page_title="AI Response Quality Evaluator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧠 AI Response Quality Evaluator")
st.write("Evaluate AI-generated responses for quality, accuracy, and hallucinations.")

st.info("Use the sidebar to navigate to the Evaluation Hub.")

if st.button("Open Evaluation Hub", use_container_width=True):
    st.switch_page("pages/2_Evaluation_Hub.py")
