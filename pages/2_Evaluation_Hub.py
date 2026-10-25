import streamlit as st

# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Evaluation Hub | AI Response Quality Evaluator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at 90% 0%, rgba(91, 115, 255, 0.10), transparent 28%),
                #f7f8fc;
        }
        .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }
        [data-testid="stSidebar"] {
            background: #111827;
        }
        [data-testid="stSidebar"] * {
            color: #f9fafb;
        }
        .hero {
            padding: 2rem 2.1rem;
            border-radius: 24px;
            color: white;
            background: linear-gradient(120deg, #172554 0%, #3730a3 55%, #6d28d9 100%);
            box-shadow: 0 14px 35px rgba(49, 46, 129, 0.18);
            margin-bottom: 1.25rem;
        }
        .hero-kicker {
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            opacity: 0.82;
            margin-bottom: 0.55rem;
        }
        .hero h1 {
            color: white;
            font-size: clamp(1.8rem, 4vw, 2.65rem);
            line-height: 1.15;
            margin: 0 0 0.7rem 0;
        }
        .hero p {
            color: #e0e7ff;
            font-size: 1rem;
            max-width: 760px;
            margin: 0;
            line-height: 1.65;
        }
        .section-heading {
            color: #111827;
            font-size: 1.15rem;
            font-weight: 750;
            margin: 1.35rem 0 0.2rem 0;
        }
        .section-subtitle {
            color: #64748b;
            font-size: 0.92rem;
            margin: 0 0 1rem 0;
        }
        .status-banner {
            border: 1px solid #f5d38a;
            background: #fffbeb;
            color: #854d0e;
            padding: 0.9rem 1rem;
            border-radius: 12px;
            margin: 0.8rem 0 1.25rem 0;
            font-size: 0.92rem;
        }
        .info-card {
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 1rem 1.1rem;
            min-height: 120px;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.035);
        }
        .info-card .icon {
            font-size: 1.35rem;
            margin-bottom: 0.4rem;
        }
        .info-card .label {
            color: #111827;
            font-weight: 700;
            margin-bottom: 0.3rem;
        }
        .info-card .desc {
            color: #64748b;
            font-size: 0.86rem;
            line-height: 1.5;
        }
        div[data-testid="stForm"] {
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 18px;
            padding: 1.3rem 1.35rem 1.1rem 1.35rem;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.045);
        }
        div[data-testid="stTextArea"] label,
        div[data-testid="stFileUploader"] label {
            color: #1f2937;
            font-weight: 650;
        }
        .footer-note {
            color: #64748b;
            font-size: 0.82rem;
            text-align: center;
            padding-top: 1.5rem;
        }
        div.stButton > button[kind="primary"],
        div[data-testid="stFormSubmitButton"] > button[kind="primary"] {
            border-radius: 10px;
            min-height: 2.8rem;
            font-weight: 700;
        }
        

/* Keep all sidebar navigation labels visible */
[data-testid="stSidebar"] button {
    width: 100% !important;
    min-height: 44px !important;
    background-color: #1e293b !important;
    color: #ffffff !important;
    border: 1px solid #475569 !important;
    border-radius: 10px !important;
    justify-content: flex-start !important;
    opacity: 1 !important;
}

[data-testid="stSidebar"] button p,
[data-testid="stSidebar"] button span,
[data-testid="stSidebar"] button div {
    color: #ffffff !important;
    opacity: 1 !important;
    visibility: visible !important;
    font-size: 15px !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] button:hover {
    background-color: #4f46e5 !important;
}



    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:
    st.markdown("## 🧠 Response Evaluator")
    st.caption("Frontend workspace")
    st.divider()

    st.markdown("### Project navigation")

    
    if st.button("🏠  Home page", key="nav_home", use_container_width=True):
        st.switch_page("pages/1_Home.py")

    if st.button("📝  Evaluation Hub", key="nav_evaluation", use_container_width=True):
        st.switch_page("pages/2_Evaluation_Hub.py")

    if st.button("📊  Results & Analytics", key="nav_results", use_container_width=True):
        st.switch_page("pages/3_Results_Analytics.py")

    if st.button("🗂️  Knowledge Base", key="nav_knowledge", use_container_width=True):
        st.switch_page("pages/4_Knowledge_Base.py")

    if st.button("📄  Reports", key="nav_reports", use_container_width=True):
        st.switch_page("pages/5_Reports_Documentation.py")

    st.divider()

    st.markdown("### Current status")
    st.warning("Backend not connected")
    st.caption(
        "The form is ready to collect input. Real evaluation will become available "
        "after the backend integration is completed."
    )

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <div class="hero-kicker">AI Response Quality Evaluator Agent</div>
        <h1>Evaluation Hub</h1>
        <p>
            Review an AI-generated response for relevance, accuracy, hallucination risk,
            and completeness. Submit your input here when the evaluation service is connected.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="status-banner">
        <strong>Development status:</strong> Frontend interface is available.
        Backend integration is pending, so this page will not generate scores or verdicts yet.
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Dimension overview cards
# ---------------------------------------------------------
st.markdown('<div class="section-heading">What will be evaluated?</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">These are the planned evaluation dimensions; no scores are produced yet.</div>',
    unsafe_allow_html=True,
)

card_cols = st.columns(4)
cards = [
    ("🎯", "Relevance", "Does the response address the user's question?"),
    ("✓", "Accuracy", "Are the claims supported by reliable evidence?"),
    ("🛡️", "Hallucination risk", "Are claims unsupported or potentially misleading?"),
    ("📋", "Completeness", "Does the response cover the important information?"),
]
for col, (icon, title, description) in zip(card_cols, cards):
    with col:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="icon">{icon}</div>
                <div class="label">{title}</div>
                <div class="desc">{description}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------------------------------------------------------
# Input form
# ---------------------------------------------------------
st.markdown('<div class="section-heading">Submit a response</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Enter the question and the answer you want the system to assess.</div>',
    unsafe_allow_html=True,
)

with st.form("evaluation_input_form", clear_on_submit=False):
    question = st.text_area(
        "Your question *",
        placeholder="Example: Explain how solar panels generate electricity.",
        height=115,
        help="Enter the original question that was asked to the AI.",
    )

    answer = st.text_area(
        "AI-generated response *",
        placeholder="Paste the complete AI-generated response here...",
        height=190,
        help="Paste the response you want evaluated.",
    )

    with st.expander("Add reference information (optional)", expanded=False):
        reference_answer = st.text_area(
            "Trusted reference answer",
            placeholder="Enter a trusted answer or evidence summary, if available...",
            height=130,
            help="This is optional. The backend may use it to compare claims against reference information.",
        )
        reference_document = st.file_uploader(
            "Upload a reference document (PDF or TXT)",
            type=["pdf", "txt"],
            accept_multiple_files=False,
            help="Optional supporting material. It is not processed or indexed by this frontend page.",
        )

    submitted = st.form_submit_button(
        "🔎  Submit for evaluation",
        type="primary",
        use_container_width=True,
    )

# ---------------------------------------------------------
# Submission validation and honest pending status
# ---------------------------------------------------------
if submitted:
    if not question.strip():
        st.error("Please enter your question before submitting.")
    elif not answer.strip():
        st.error("Please enter the AI-generated response before submitting.")
    else:
        st.success("Your input has passed the basic form checks.")
        st.info(
            "Backend integration is pending. No evaluation has been run, and no scores, "
            "evidence checks, or verdicts have been generated. Your input has not been sent "
            "to an evaluation service."
        )
        st.markdown("**Submission summary**")
        st.write(f"- Question length: {len(question.strip())} characters")
        st.write(f"- AI response length: {len(answer.strip())} characters")
        st.write(f"- Reference answer provided: {'Yes' if reference_answer.strip() else 'No'}")
        st.write(f"- Reference document attached: {'Yes' if reference_document else 'No'}")

st.divider()
st.markdown(
    """
    <div class="footer-note">
        AI Response Quality Evaluator Agent · Frontend prototype · Backend integration pending
    </div>
    """,
    unsafe_allow_html=True,
)
