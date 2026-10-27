
import streamlit as st

st.set_page_config(
    page_title="AI Response Quality Evaluator",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)
from ui import apply_design, render_sidebar

apply_design()
render_sidebar()
st.markdown("""
<style>
.stApp {
    background: #F5F8FD;
    color: #17345F;
}

.block-container {
    max-width: 1450px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

.hero {
    background: linear-gradient(120deg, #10264B, #2867C7);
    padding: 38px 35px;
    border-radius: 20px;
    color: white;
    margin-bottom: 24px;
}

.hero h1 {
    color: white;
    font-size: 38px;
    line-height: 1.25;
    margin-bottom: 14px;
}

.hero p {
    color: #E0EAFF;
    font-size: 16px;
    line-height: 1.8;
}

.eyebrow {
    color: #BBD5FF;
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 2px;
}

.section-title {
    font-size: 25px;
    font-weight: 750;
    color: #17345F;
    margin-top: 28px;
    margin-bottom: 8px;
}

.section-copy {
    color: #647792;
    line-height: 1.7;
}

.feature {
    background: white;
    border: 1px solid #DFE8F5;
    border-radius: 15px;
    padding: 23px;
    min-height: 175px;
}

.feature-icon {
    font-size: 30px;
    margin-bottom: 10px;
}

.feature h3 {
    color: #17345F;
    font-size: 18px;
}

.feature p {
    color: #647792;
    font-size: 13px;
    line-height: 1.7;
}

.workflow {
    background: white;
    border: 1px solid #DFE8F5;
    border-radius: 15px;
    padding: 22px;
    text-align: center;
}

.workflow-icon {
    font-size: 30px;
}

.workflow h4 {
    color: #17345F;
    margin-bottom: 8px;
}

.workflow p {
    color: #647792;
    font-size: 12px;
    line-height: 1.6;
}

.stButton button {
    min-height: 46px;
    border-radius: 10px;
    font-weight: 600;
}

.footer {
    text-align: center;
    color: #7A8BA5;
    font-size: 12px;
    margin-top: 35px;
}
</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero">
    <div class="eyebrow">AI QUALITY ASSURANCE PLATFORM</div>
    <h1>AI Response Quality Evaluator</h1>
    <p>
        Evaluate AI-generated answers, identify unsupported claims,
        and understand response quality through structured evaluation.
        Start with a single response or evaluate multiple responses in a batch.
    </p>
</div>
""", unsafe_allow_html=True)

# Main navigation buttons
left, right, space = st.columns([1, 1, 2])

with left:
    if st.button("▶  Start Evaluation", type="primary",
                 use_container_width=True):
        st.switch_page("pages/2_Evaluation_Hub.py")

with right:
    if st.button("▦  Batch Evaluation",
                 use_container_width=True):
        st.switch_page("pages/5_Batch_Evaluation.py")

# Features
st.markdown(
    '<div class="section-title">What this platform does</div>'
    '<div class="section-copy">'
    'A structured approach to understanding the quality of AI responses.'
    '</div>',
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3, gap="medium")

features = [
    (
        c1,
        "🎯",
        "Response Assessment",
        "Examine how well an AI-generated answer addresses the original question."
    ),
    (
        c2,
        "🔎",
        "Evidence & Reliability",
        "Review factual claims against reference information when available."
    ),
    (
        c3,
        "📊",
        "Results & Insights",
        "Present evaluation findings and identify areas that may need improvement."
    ),
]

for col, icon, title, description in features:
    with col:
        st.markdown(f"""
        <div class="feature">
            <div class="feature-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

# Workflow
st.markdown(
    '<div class="section-title">How it works</div>'
    '<div class="section-copy">'
    'Follow these three steps to review AI-generated content.'
    '</div>',
    unsafe_allow_html=True,
)

w1, w2, w3 = st.columns(3, gap="medium")

workflow_steps = [
    (
        w1,
        "📄",
        "1. Submit",
        "Enter a question and AI response, or upload supported batch data."
    ),
    (
        w2,
        "🧠",
        "2. Evaluate",
        "Run the evaluation process using the criteria available in the application."
    ),
    (
        w3,
        "📈",
        "3. Review",
        "Inspect the available scores, explanations, and evaluation findings."
    ),
]

for col, icon, title, description in workflow_steps:
    with col:
        st.markdown(f"""
        <div class="workflow">
            <div class="workflow-icon">{icon}</div>
            <h4>{title}</h4>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    AI Response Quality Evaluator · Built with Streamlit
</div>
""", unsafe_allow_html=True)
