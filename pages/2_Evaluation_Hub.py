
import streamlit as st

st.set_page_config(
    page_title="Evaluation Hub | AI Quality Evaluator",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f5f7ff 0%, #edf2ff 100%);
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}
.hero {
    background: linear-gradient(120deg, #172554, #4338ca, #6366f1);
    padding: 32px;
    border-radius: 20px;
    color: white;
    margin-bottom: 25px;
}
.hero h1 {
    color: white;
    font-size: 34px;
    margin-bottom: 8px;
}
.hero p {
    color: #e0e7ff;
    font-size: 16px;
}
.section-card {
    background: white;
    padding: 24px;
    border-radius: 16px;
    border: 1px solid #e0e7ff;
    margin-bottom: 18px;
}
div[data-testid="stTextArea"] textarea {
    background-color: #f8faff;
    border: 1px solid #dbe4ff;
    border-radius: 10px;
}
div[data-testid="stFileUploader"] {
    background: #f8faff;
    border-radius: 12px;
    padding: 12px;
}
.stButton > button {
    background: linear-gradient(90deg, #4338ca, #6366f1);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 24px;
    font-weight: 600;
    min-height: 48px;
}
.stButton > button:hover {
    color: white;
    border: 1px solid #4338ca;
}
.info-card {
    background: #eef2ff;
    border-left: 4px solid #6366f1;
    border-radius: 10px;
    padding: 14px 18px;
    color: #312e81;
    margin-bottom: 20px;
}
.small-note {
    color: #64748b;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🧠 AI Response Quality Evaluator</h1>
    <p>Evaluate AI-generated answers for relevance, accuracy,
    hallucination risk, and completeness.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("✨ Evaluation Hub")
    st.write("Enter your question and the AI response you want to review.")

with col2:
    st.markdown("### 🟣 FRONTEND DEMO")

st.markdown("""
<div class="info-card">
    <b>Demo mode:</b> The interface is ready.
    Real AI evaluation will be enabled when the backend is connected.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown("### 📝 Response details")

question = st.text_area(
    "Your question",
    placeholder="Example: What is artificial intelligence?",
    height=110
)

answer = st.text_area(
    "AI-generated response",
    placeholder="Paste the complete response you want to evaluate...",
    height=170
)

st.markdown("### 📚 Reference information")
st.caption("Optional: provide a trusted answer or supporting document.")

reference = st.text_area(
    "Reference answer",
    placeholder="Enter a trusted answer to compare against...",
    height=100
)

document = st.file_uploader(
    "Upload reference document (optional)",
    type=["pdf", "txt"],
    help="PDF and TXT files are accepted."
)

st.markdown('</div>', unsafe_allow_html=True)

left, right = st.columns([1, 2])

with left:
    evaluate = st.button(
        "🔍  Evaluate Response",
        type="primary",
        use_container_width=True
    )

with right:
    st.markdown(
        '<p class="small-note">Required: question and AI response. '
        'Reference information is optional.</p>',
        unsafe_allow_html=True
    )

if evaluate:
    if not question.strip():
        st.warning("Please enter your question first.")
    elif not answer.strip():
        st.warning("Please enter the AI-generated response.")
    else:
        st.success("Your input is valid and ready for evaluation.")
        st.info(
            "Backend integration is pending. Real scores and verdicts "
            "will appear after the evaluation service is connected."
        )

st.divider()
st.markdown(
    '<p class="small-note" style="text-align:center;">'
    'AI Response Quality Evaluator Agent · Frontend Demo</p>',
    unsafe_allow_html=True
)
