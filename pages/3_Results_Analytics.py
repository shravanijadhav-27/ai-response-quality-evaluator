
import streamlit as st

st.set_page_config(
    page_title="Results & Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Results & Analytics")
st.write("Review the quality of evaluated AI responses.")

st.info(
    "The evaluation backend is not connected yet. "
    "Actual scores and analytics will appear after integration."
)

st.subheader("Evaluation Dimensions")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 Accuracy")
    st.write("Checks whether the response is factually correct.")

    st.markdown("### 📝 Relevance")
    st.write("Checks whether the response answers the question.")

with col2:
    st.markdown("### 📚 Completeness")
    st.write("Checks whether important information is included.")

    st.markdown("### 🔎 Hallucination Detection")
    st.write("Identifies claims that may not be supported by evidence.")

st.divider()

st.subheader("Analytics Dashboard")

st.write(
    "Charts, evaluation scores, and historical trends "
    "will be displayed here once real evaluation data is available."
)

if st.button("← Back to Home"):
    st.switch_page("pages/1_Home.py")
