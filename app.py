
import streamlit as st

st.set_page_config(
    page_title="AI Response Quality Evaluator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

from ui import apply_design, render_sidebar

apply_design()
render_sidebar()
st.markdown("""
<style>
section[data-testid="stSidebarNav"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)
# ---------- CUSTOM DESIGN ----------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            180deg,
            #f3f6ff 0%,
            #f8faff 45%,
            #ffffff 100%
        );
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #101b35;
    }

    section[data-testid="stSidebar"] * {
        color: #f1f5ff;
    }

    button[data-testid="collapsedControl"] {
        background: #315efb !important;
        border: 2px solid #ffffff !important;
        border-radius: 10px !important;
        color: white !important;
        box-shadow: 0 3px 12px #315efb55 !important;
    }

    button[data-testid="collapsedControl"] svg {
        color: white !important;
    }

    /* Main hero */
    .hero {
        background: linear-gradient(120deg, #14264d, #315efb);
        padding: 36px 34px;
        border-radius: 22px;
        color: white;
        margin-bottom: 26px;
        box-shadow: 0 12px 30px #2347a522;
    }

    .hero-tag {
        display: inline-block;
        background: #ffffff20;
        border: 1px solid #ffffff40;
        padding: 6px 12px;
        border-radius: 30px;
        font-size: 12px;
        letter-spacing: 1px;
        margin-bottom: 14px;
    }

    .hero h1 {
        color: white;
        font-size: clamp(27px, 4vw, 43px);
        line-height: 1.2;
        margin: 0 0 14px 0;
    }

    .hero p {
        color: #e0e9ff;
        font-size: 16px;
        line-height: 1.7;
        max-width: 760px;
        margin-bottom: 0;
    }

    .section-heading {
        color: #14264d;
        font-size: 24px;
        font-weight: 750;
        margin: 28px 0 6px 0;
    }

    .section-description {
        color: #68758c;
        font-size: 14px;
        margin-bottom: 18px;
    }

    /* Feature cards */
    .feature-card {
        background: #ffffff;
        border: 1px solid #e4eaf5;
        border-radius: 17px;
        padding: 22px 20px;
        min-height: 178px;
        box-shadow: 0 5px 18px #18315b09;
        margin-bottom: 12px;
    }

    .feature-icon {
        font-size: 28px;
        margin-bottom: 13px;
    }

    .feature-card h3 {
        color: #18294b;
        font-size: 17px;
        margin: 0 0 9px 0;
    }

    .feature-card p {
        color: #69768d;
        font-size: 13px;
        line-height: 1.65;
        margin: 0;
    }

    /* Workflow */
    .workflow {
        background: #ffffff;
        border: 1px solid #e4eaf5;
        border-radius: 18px;
        padding: 24px;
        margin-top: 10px;
    }

    .step {
        background: #f3f6ff;
        border: 1px solid #e0e8ff;
        border-radius: 13px;
        padding: 17px 10px;
        text-align: center;
        min-height: 105px;
    }

    .step-number {
        color: #315efb;
        font-weight: 800;
        font-size: 12px;
        margin-bottom: 7px;
    }

    .step-title {
        color: #18294b;
        font-size: 14px;
        font-weight: 700;
    }

    .footer {
        text-align: center;
        color: #8792a6;
        font-size: 12px;
        padding-top: 26px;
    }

    /* Primary action */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(100deg, #315efb, #6448e8);
        color: white;
        border: none;
        border-radius: 11px;
        min-height: 48px;
        font-weight: 700;
        box-shadow: 0 5px 14px #315efb30;
    }

    div.stButton > button[kind="primary"]:hover {
        background: #2348d8;
        border: none;
        color: white;
    }

    @media (max-width: 700px) {
        .hero {
            padding: 25px 20px;
        }

        .block-container {
            padding-top: 1rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- HERO SECTION ----------
st.markdown(
    """
    <div class="hero">
        <div class="hero-tag">AI QUALITY INTELLIGENCE</div>
        <h1>AI Response Quality Evaluator</h1>
        <p>
            Evaluate AI-generated responses with greater confidence.
            Analyze accuracy, relevance, completeness, and potential
            hallucinations using a structured evaluation workflow.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- MAIN ACTION ----------
left, center, right = st.columns([1, 2, 1])

with center:
    if st.button(
        "🚀  Start Evaluating Responses",
        type="primary",
        use_container_width=True,
    ):
        st.switch_page("pages/2_Evaluation_Hub.py")

st.markdown(
    """
    <div class="section-heading">What can you evaluate?</div>
    <div class="section-description">
        Four important dimensions for assessing AI-generated answers.
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- FEATURE CARDS ----------
c1, c2, c3, c4 = st.columns(4)

features = [
    (
        "🎯",
        "Accuracy",
        "Check whether the answer is factually correct and supported by evidence.",
    ),
    (
        "🔎",
        "Relevance",
        "Measure how closely the response answers the user's actual question.",
    ),
    (
        "📋",
        "Completeness",
        "Identify missing details and important parts of an answer.",
    ),
    (
        "🛡️",
        "Hallucination Detection",
        "Look for unsupported claims or statements that conflict with references.",
    ),
]

for col, (icon, title, description) in zip(
    [c1, c2, c3, c4], features
):
    with col:
        st.markdown(
            f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------- WORKFLOW ----------
st.markdown(
    """
    <div class="section-heading">How it works</div>
    <div class="section-description">
        A simple workflow from input to evaluation results.
    </div>
    <div class="workflow">
    """,
    unsafe_allow_html=True,
)

w1, w2, w3, w4 = st.columns(4)

steps = [
    ("01", "Enter Response"),
    ("02", "Add Reference"),
    ("03", "Evaluate Quality"),
    ("04", "Review Results"),
]

for col, (number, title) in zip(
    [w1, w2, w3, w4], steps
):
    with col:
        st.markdown(
            f"""
            <div class="step">
                <div class="step-number">STEP {number}</div>
                <div class="step-title">{title}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("</div>", unsafe_allow_html=True)

# ---------- BATCH EVALUATION ----------
st.markdown(
    """
    <div class="section-heading">Need to evaluate multiple responses?</div>
    <div class="section-description">
        Use the Batch Evaluation page to work with multiple records
        from a supported dataset or CSV file.
    </div>
    """,
    unsafe_allow_html=True,
)

batch_col, info_col = st.columns([1, 2])

with batch_col:
    if st.button(
        "📊  Explore Batch Evaluation",
        use_container_width=True,
    ):
        st.switch_page("pages/5_Batch_Evaluation.py")

with info_col:
    st.info(
        "Batch processing requires a working evaluation pipeline. "
        "Results will depend on the functionality implemented in that page."
    )

# ---------- FOOTER ----------
st.markdown(
    """
    <div class="footer">
        AI Response Quality Evaluator · Quality, evidence and reliability
    </div>
    """,
    unsafe_allow_html=True,
)
