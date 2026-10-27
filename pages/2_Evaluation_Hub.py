
import streamlit as st

st.set_page_config(
    page_title="Evaluation Hub | AI Response Evaluator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Shared design and navigation
from ui import apply_design, render_sidebar

apply_design()
render_sidebar()

# Page-specific design
st.markdown("""
<style>
.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
}

.eval-hero {
    background: linear-gradient(120deg, #10264B 0%, #244E91 65%, #6546C8 100%);
    padding: 30px;
    border-radius: 20px;
    color: white;
    margin-bottom: 22px;
    box-shadow: 0 12px 30px rgba(24, 48, 94, 0.13);
}

.eval-hero .eyebrow {
    color: #C7D8FF;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
}

.eval-hero h1 {
    color: white;
    font-size: 34px;
    line-height: 1.25;
    margin: 10px 0;
}

.eval-hero p {
    color: #E2EAFE;
    font-size: 14px;
    line-height: 1.8;
    max-width: 800px;
    margin-bottom: 0;
}

.mini-card {
    background: white;
    border: 1px solid #E0E8F5;
    padding: 17px;
    border-radius: 14px;
    min-height: 112px;
}

.mini-card .emoji {
    font-size: 25px;
}

.mini-card .heading {
    color: #17345F;
    font-size: 14px;
    font-weight: 750;
    margin-top: 8px;
}

.mini-card .description {
    color: #6B7D98;
    font-size: 11px;
    line-height: 1.5;
    margin-top: 5px;
}

.section-heading {
    color: #17345F;
    font-size: 23px;
    font-weight: 800;
    margin: 28px 0 5px;
}

.section-description {
    color: #71819B;
    font-size: 13px;
    margin-bottom: 17px;
}

.form-panel {
    background: white;
    border: 1px solid #DCE6F4;
    border-radius: 17px;
    padding: 22px;
    box-shadow: 0 5px 20px rgba(28, 53, 94, 0.045);
}

.form-label {
    color: #17345F;
    font-size: 15px;
    font-weight: 750;
    margin-bottom: 5px;
}

.form-hint {
    color: #7B8AA2;
    font-size: 12px;
    margin-bottom: 12px;
}

.tip-panel {
    background: #EDF4FF;
    border: 1px solid #D5E5FF;
    padding: 16px;
    border-radius: 13px;
    color: #254875;
    font-size: 13px;
    line-height: 1.8;
    margin: 15px 0;
}

.status-panel {
    background: #FFF7E6;
    border: 1px solid #F3D49A;
    color: #80530C;
    padding: 14px 17px;
    border-radius: 12px;
    margin: 15px 0;
    font-size: 13px;
    line-height: 1.7;
}

div[data-testid="stForm"] {
    background: white;
    border: 1px solid #DCE6F4;
    border-radius: 17px;
    padding: 22px;
    box-shadow: 0 5px 20px rgba(28, 53, 94, 0.045);
}

div[data-testid="stTextArea"] label,
div[data-testid="stFileUploader"] label {
    color: #17345F;
    font-weight: 650;
}

.stButton button,
div[data-testid="stFormSubmitButton"] button {
    min-height: 46px;
    border-radius: 10px;
    font-weight: 700;
}

.result-panel {
    background: white;
    border: 1px solid #DCE6F4;
    padding: 20px;
    border-radius: 15px;
    margin-top: 18px;
}

.footer {
    text-align: center;
    color: #7A8BA5;
    font-size: 12px;
    padding-top: 30px;
}

/* Fix question and answer fields */
div[data-testid="stTextArea"] textarea {
    background-color: #FFFFFF !important;
    color: #17345F !important;
    -webkit-text-fill-color: #17345F !important;
    caret-color: #17345F !important;
    border: 1px solid #B8C9E3 !important;
    border-radius: 10px !important;
}

/* Keep placeholder text readable */
div[data-testid="stTextArea"] textarea::placeholder {
    color: #71819B !important;
    -webkit-text-fill-color: #71819B !important;
    opacity: 1 !important;
}

/* Keep input fields readable when focused */
div[data-testid="stTextArea"] textarea:focus {
    background-color: #FFFFFF !important;
    color: #17345F !important;
    border: 1px solid #2867C7 !important;
    box-shadow: 0 0 0 1px #2867C7 !important;
}

/* Improve visibility of field labels */
div[data-testid="stTextArea"] label {
    color: #17345F !important;
}

</style>
""", unsafe_allow_html=True)


# Hero banner
st.markdown("""
<div class="eval-hero">
    <div class="eyebrow">AI QUALITY ASSURANCE · WORKSPACE 01</div>
    <h1>Evaluate an AI Response</h1>
    <p>
        Inspect an AI-generated answer using a structured evaluation workflow.
        Provide the original question, the response, and optional reference
        information to prepare your evaluation.
    </p>
</div>
""", unsafe_allow_html=True)


# Compact feature cards
c1, c2, c3 = st.columns(3, gap="medium")

feature_data = [
    (
        c1, "📝", "Individual Review",
        "Evaluate one question and its AI-generated answer."
    ),
    (
        c2, "📚", "Reference Support",
        "Provide trusted information for a future evidence-based check."
    ),
    (
        c3, "🔍", "Quality Inspection",
        "Prepare the input for relevance, accuracy and reliability assessment."
    ),
]

for col, emoji, heading, description in feature_data:
    with col:
        st.markdown(f"""
        <div class="mini-card">
            <div class="emoji">{emoji}</div>
            <div class="heading">{heading}</div>
            <div class="description">{description}</div>
        </div>
        """, unsafe_allow_html=True)


# Input section
st.markdown("""
<div class="section-heading">Response input</div>
<div class="section-description">
    Enter the required information below. You can add supporting reference material if available.
</div>
""", unsafe_allow_html=True)

with st.form("evaluation_form", clear_on_submit=False):

    st.markdown(
        '<div class="form-label">01 · Original question</div>'
        '<div class="form-hint">What did the user ask the AI?</div>',
        unsafe_allow_html=True,
    )

    question = st.text_area(
        "Original question *",
        placeholder="Example: Explain how solar panels generate electricity.",
        height=110,
        label_visibility="collapsed",
    )

    st.markdown(
        '<div class="form-label">02 · AI-generated answer</div>'
        '<div class="form-hint">Paste the complete answer you want to assess.</div>',
        unsafe_allow_html=True,
    )

    answer = st.text_area(
        "AI-generated answer *",
        placeholder="Paste the AI response here...",
        height=210,
        label_visibility="collapsed",
    )

    st.markdown(
        '<div class="form-label">03 · Supporting evidence</div>'
        '<div class="form-hint">Optional — provide a trusted answer or document for comparison.</div>',
        unsafe_allow_html=True,
    )

    with st.expander("＋ Add reference information", expanded=False):

        reference_answer = st.text_area(
            "Trusted reference answer",
            placeholder="Enter verified facts or a trusted answer...",
            height=130,
        )

        reference_document = st.file_uploader(
            "Upload a reference document (PDF or TXT)",
            type=["pdf", "txt"],
            accept_multiple_files=False,
            help="This prototype accepts the file but does not yet process its contents.",
        )

    st.markdown("""
    <div class="tip-panel">
        💡 <strong>Tip:</strong> Include the original question and the complete AI response.
        Reference information can help a connected evaluation system compare factual claims.
    </div>
    """, unsafe_allow_html=True)

    submitted = st.form_submit_button(
        "🔎  Prepare Evaluation",
        type="primary",
        use_container_width=True,
    )


# Submission feedback
if submitted:

    if not question.strip():
        st.error("Please enter the original question.")

    elif not answer.strip():
        st.error("Please enter the AI-generated answer.")

    else:
        st.markdown("""
        <div class="result-panel">
            <h3 style="color:#17345F;margin-top:0;">
                ✓ Input validation complete
            </h3>
            <p style="color:#647792;font-size:13px;line-height:1.8;">
                Your required fields have been checked. This confirms only
                that the input is present — it does not mean the AI response
                has been evaluated.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Submission overview")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Question length",
            f"{len(question.strip())} characters",
        )

        col2.metric(
            "Response length",
            f"{len(answer.strip())} characters",
        )

        has_reference = bool(
            reference_answer.strip() or reference_document
        )

        col3.metric(
            "Reference supplied",
            "Yes" if has_reference else "No",
        )

        st.warning(
            "Backend integration is pending. No evaluation scores, "
            "hallucination checks, evidence analysis, or final verdict "
            "have been generated. The input has not been sent to an "
            "evaluation service."
        )


# Honest prototype status
st.markdown("""
<div class="status-panel">
    <strong>🟡 Current development status</strong><br>
    The interface is ready for input validation. Connecting the evaluation
    backend is still required to generate real scores, identify unsupported
    claims, and produce a final verdict.
</div>

<div class="footer">
    AI Response Quality Evaluator · Individual Evaluation Workspace
</div>
""", unsafe_allow_html=True)
