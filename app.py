import re
from pathlib import Path

import streamlit as st
import textwrap
# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="EvalAI | AI Response Quality",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)
from ui import apply_design, render_sidebar

apply_design()
render_sidebar()
IMAGE_PATH = Path(__file__).parent / "assets" / "ai_quality_illustration.png"

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #07192f;
    --cyan: #55d9ee;
    --ink: #142943;
    --muted: #65758b;
    --border: #e3eaf2;
}

.stApp {
    background: #f7f9fc;
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1440px;
    padding: 0 0 3rem 0;
}

h1, h2, h3 {
    font-family: 'Manrope', sans-serif;
}

[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] * {
    color: #19314d;
}

/* TOP NAVIGATION */

.topbar {
    min-height: 70px;
    background: white;
    border-bottom: 1px solid #e8edf3;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    padding: 12px clamp(20px, 6vw, 90px);
}

.brand {
    font-family: 'Manrope', sans-serif;
    font-size: 29px;
    font-weight: 800;
    letter-spacing: -1.5px;
    color: #10223a;
}

.brand span {
    color: #08aeca;
}

.navlinks {
    display: flex;
    gap: 28px;
}

.navlinks a {
    color: #33465e !important;
    text-decoration: none !important;
    font-size: 13px;
    font-weight: 600;
}

.navlinks a:hover {
    color: #00a9c9 !important;
}

/* HERO SECTION */

.st-key-hero_section {
    background:
        radial-gradient(
            circle at 10% 80%,
            rgba(0, 175, 204, .20),
            transparent 35%
        ),
        linear-gradient(
            115deg,
            #07192f,
            #0a2543 60%,
            #073c55
        );
    padding: 48px clamp(20px, 6vw, 90px) 85px;
    border-bottom: 1px solid #173d59;
    overflow: hidden;
}

.st-key-hero_section [data-testid="stVerticalBlock"] {
    gap: 0.7rem;
}

.eyebrow {
    color: #9cebf4;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.3px;
    margin-bottom: 18px;
}

.hero-title {
    font-family: 'Manrope', sans-serif;
    font-size: clamp(36px, 4.2vw, 56px);
    line-height: 1.12;
    letter-spacing: -2px;
    font-weight: 800;
    color: #ffffff !important;
    margin: 0;
}

.st-key-hero_section .hero-title,
.st-key-hero_section .hero-title span {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}

.st-key-hero_section .hero-title .accent {
    color: #5de1f0 !important;
    -webkit-text-fill-color: #5de1f0 !important;
}

.accent {
    color: #5de1f0;
}

.hero-copy {
    color: #d0deeb;
    font-size: 14px;
    line-height: 1.85;
    margin-top: 18px;
    max-width: 550px;
}

.pill-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 20px;
}

.pill {
    border: 1px solid rgba(117, 220, 239, .55);
    color: #d8f8fc;
    background: rgba(10, 62, 88, .42);
    border-radius: 20px;
    padding: 7px 10px;
    font-size: 10px;
}

.hero-caption {
    color: #b8cbdc;
    font-size: 10px;
    margin-top: 8px;
}

.st-key-hero_section img {
    border-radius: 16px;
}

/* BUTTONS */

div.stButton > button {
    min-height: 44px;
    border-radius: 9px;
    font-size: 13px;
    font-weight: 700;
    transition: all .2s ease;
}

div.stButton > button[kind="primary"] {
    background: #55d9ee !important;
    color: #06243b !important;
    border-color: #55d9ee !important;
}

div.stButton > button:hover {
    border-color: #21bad5;
    transform: translateY(-1px);
}

/* HERO ACTIONS */

.st-key-hero_actions {
    padding: 0 clamp(20px, 6vw, 90px);
    margin-top: -65px;
    position: relative;
    z-index: 2;
}

/* SECTION HEADINGS */

.section-head {
    text-align: center;
    margin: 55px auto 28px;
    padding: 0 20px;
}

.kicker {
    color: #078eae;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.7px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.section-title {
    font-family: 'Manrope', sans-serif;
    font-size: clamp(25px, 3vw, 34px);
    line-height: 1.3;
    font-weight: 800;
    color: #142943;
}

.section-copy {
    color: var(--muted);
    font-size: 13px;
    line-height: 1.8;
    max-width: 680px;
    margin: 10px auto 0;
}

/* FEATURE CARDS */

.st-key-feature_section {
    padding: 0 clamp(20px, 6vw, 90px);
}

.feature-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 22px 20px;
    min-height: 185px;
    box-shadow: 0 9px 26px rgba(15, 38, 65, .06);
    height: 100%;
}

.feature-icon {
    width: 44px;
    height: 44px;
    border-radius: 10px;
    background: #e1f8fb;
    color: #087e96;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    margin-bottom: 15px;
}

.feature-card h3 {
    font-family: 'Manrope', sans-serif;
    font-size: 15px;
    color: #142943;
    margin: 0 0 8px;
}

.feature-card p {
    color: #586a80;
    font-size: 12px;
    line-height: 1.75;
    margin: 0;
}

/* WORKFLOW */

.workflow-wrap {
    padding: 0 clamp(20px, 6vw, 90px);
}

.workflow-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 24px 20px;
    min-height: 170px;
    box-shadow: 0 5px 18px rgba(15, 38, 65, .04);
}

.step-number {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: #123453;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    margin-bottom: 14px;
}

.workflow-card h3 {
    color: #19314d;
    font-size: 15px;
}

.workflow-card p {
    color: #687b91;
    font-size: 12px;
    line-height: 1.75;
}

/* BOTTOM CTA */

.bottom-cta {
    margin: 45px clamp(20px, 6vw, 90px) 0;
    padding: 35px 20px;
    text-align: center;
    border-radius: 17px;
    border: 1px solid #dce8f1;
    background: linear-gradient(115deg, #edf8fb, #eef3fb);
}

/* FOOTER */

.footer {
    margin: 35px clamp(20px, 6vw, 90px) 0;
    padding-top: 18px;
    border-top: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: wrap;
    color: #78879a;
    font-size: 11px;
}

@media (max-width: 850px) {
    .st-key-hero_section {
        padding-top: 35px;
        padding-bottom: 80px;
    }

    .hero-title {
        font-size: 40px;
    }

    .navlinks {
        gap: 15px;
    }
}

@media (max-width: 560px) {
    .topbar {
        align-items: flex-start;
        flex-direction: column;
        gap: 8px;
    }

    .hero-title {
        font-size: 35px;
        letter-spacing: -1px;
    }

    .feature-card,
    .workflow-card {
        min-height: 0;
    }
}

/* EVALUATION OVERVIEW */

.eval-overview {
    padding: 12px clamp(20px, 6vw, 90px) 10px;
}

.eval-panel {
    background: linear-gradient(135deg, #0b2038, #103b55);
    border: 1px solid #214b65;
    border-radius: 20px;
    padding: 28px;
    color: #ffffff;
    box-shadow: 0 18px 45px rgba(8, 30, 53, 0.12);
}

.eval-panel h3 {
    color: #ffffff;
    font-size: 21px;
    margin: 0 0 8px;
}

.eval-panel p {
    color: #c2d5e5;
    font-size: 12px;
    line-height: 1.8;
}

.eval-label {
    color: #66e0ef;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 12px;
}

.eval-check {
    background: rgba(255, 255, 255, 0.055);
    border: 1px solid rgba(175, 219, 239, 0.17);
    border-radius: 12px;
    padding: 16px;
    height: 100%;
}

.eval-check h4 {
    color: #ffffff;
    font-size: 14px;
    margin: 0 0 7px;
}

.eval-check p {
    margin: 0;
    font-size: 11px;
}

.eval-dot {
    width: 9px;
    height: 9px;
    display: inline-block;
    background: #5de1f0;
    border-radius: 50%;
    margin-right: 7px;
}

.eval-note {
    margin-top: 18px;
    padding: 12px 15px;
    background: #edf8fb;
    border: 1px solid #d5edf3;
    border-radius: 10px;
    color: #31536a;
    font-size: 11px;
    line-height: 1.7;
}

.pipeline-section {
    padding: 0 clamp(20px, 6vw, 90px);
}

.pipeline-card {
    background: #ffffff;
    border: 1px solid #e3eaf2;
    border-radius: 15px;
    padding: 23px 20px;
    height: 100%;
    box-shadow: 0 7px 22px rgba(15, 38, 65, 0.04);
}

.pipeline-tag {
    display: inline-block;
    background: #e5f8fb;
    color: #087e96;
    padding: 6px 9px;
    border-radius: 6px;
    font-size: 10px;
    font-weight: 800;
    margin-bottom: 14px;
}

.pipeline-card h3 {
    font-size: 15px;
    color: #142943;
    margin-bottom: 9px;
}

.pipeline-card p {
    font-size: 12px;
    color: #64758a;
    line-height: 1.8;
    margin-bottom: 0;
}

/* Final bottom CTA styling */

.bottom-cta {
    margin-top: 48px;
    padding: 42px 22px;
    background: linear-gradient(120deg, #e7f8fb, #eef2fc);
    border: 1px solid #d8e9f1;
    border-radius: 18px;
    text-align: center;
}

.bottom-cta .section-copy {
    margin-bottom: 10px;
}

@media (max-width: 560px) {
    .eval-panel {
        padding: 20px 16px;
    }

    .eval-check {
        padding: 13px;
    }
}

/* FIVE-AGENT ARCHITECTURE */

.agent-section {
    padding: 0 clamp(20px, 6vw, 90px);
}

.agent-card {
    background: #ffffff;
    border: 1px solid #e0e8f1;
    border-radius: 15px;
    padding: 19px 16px;
    height: 100%;
    box-shadow: 0 6px 22px rgba(15, 38, 65, 0.045);
}

.agent-card .agent-number {
    color: #078eae;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.2px;
    margin-bottom: 13px;
}

.agent-card h3 {
    font-size: 14px;
    line-height: 1.5;
    color: #142943;
    margin: 0 0 9px;
}

.agent-card p {
    color: #63748a;
    font-size: 11px;
    line-height: 1.8;
    margin: 0;
}

.agent-role {
    display: inline-block;
    font-size: 10px;
    font-weight: 700;
    padding: 5px 8px;
    background: #e7f7fb;
    color: #087e96;
    border-radius: 6px;
    margin-bottom: 12px;
}

.agent-connector {
    text-align: center;
    color: #08a5c2;
    font-size: 23px;
    padding: 10px 0;
}

.agent-input-panel {
    padding: 22px;
    background: linear-gradient(120deg, #0b2038, #10445c);
    border-radius: 17px;
    color: white;
}

.agent-input-panel h3,
.agent-verdict h3 {
    color: white;
    font-size: 19px;
    margin: 8px 0;
}

.agent-input-panel p,
.agent-verdict p {
    color: #d1e2ed;
    font-size: 12px;
    line-height: 1.8;
}

.agent-verdict {
    background: linear-gradient(120deg, #102b46, #174c67);
    border: 1px solid #275a72;
    border-radius: 17px;
    padding: 24px;
    color: white;
}

.agent-output {
    background: #edf8fb;
    border: 1px solid #d6edf3;
    border-radius: 13px;
    padding: 18px;
    height: 100%;
}

.agent-output h4 {
    color: #163b54;
    font-size: 13px;
    margin: 0 0 8px;
}

.agent-output p {
    color: #5a7184;
    font-size: 11px;
    line-height: 1.8;
    margin: 0;
}

</style>
""",
    unsafe_allow_html=True,
)



# ---------------- AUTHENTICATION DIALOGS ----------------


def valid_email(email):
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()))


@st.dialog("Log in to EvalAI")
def login_dialog():
    st.write("Access your AI evaluation workspace.")

    with st.form("login_form"):
        email = st.text_input("Work email")
        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button(
            "Log in", type="primary", use_container_width=True
        )

    if submitted:
        if not valid_email(email):
            st.error("Enter a valid email address.")
        elif not password:
            st.error("Enter your password.")
        else:
            st.info(
                "Login form is ready. Connect Supabase Auth " "to enable real sign-in."
            )


@st.dialog("Create your EvalAI account")
def signup_dialog():
    st.write("Create an account to get started.")

    with st.form("signup_form"):
        name = st.text_input("Full name")
        email = st.text_input("Work email")
        password = st.text_input("Create password", type="password")
        confirm = st.text_input("Confirm password", type="password")

        accepted = st.checkbox("I agree to the Terms and Privacy Policy")

        submitted = st.form_submit_button(
            "Create account", type="primary", use_container_width=True
        )

    if submitted:
        if not name.strip():
            st.error("Enter your name.")
        elif not valid_email(email):
            st.error("Enter a valid email address.")
        elif len(password) < 8:
            st.error("Password must contain at least 8 characters.")
        elif password != confirm:
            st.error("Passwords do not match.")
        elif not accepted:
            st.error("Please accept the terms.")
        else:
            st.info(
                "Registration form is ready. Connect "
                "Supabase Auth to create real accounts."
            )


# ---------------- TOP NAVIGATION ----------------

st.html("""
<div class="topbar">
    <div class="brand">Eval<span>AI</span></div>
    <nav class="navlinks">
        <a href="#features">Features</a>
        <a href="#workflow">How it works</a>
    </nav>
</div>
""")

_, login_col, signup_col = st.columns([7, 1.2, 1.7])

with login_col:
    if st.button("Log in", use_container_width=True, key="top_login"):
        login_dialog()

with signup_col:
    if st.button(
        "Create account", type="primary", use_container_width=True, key="top_signup"
    ):
        signup_dialog()



# ---------------- HERO SECTION ----------------

with st.container(key="hero_section"):
    left_col, right_col = st.columns(
        [1.15, 0.85],
        gap="large",
        vertical_alignment="center",
    )

    with left_col:
        hero_html = textwrap.dedent("""
        <div class="hero-content">
            <h1 class="hero-title">
                Evaluate Your AI.<br>
                Ensure <span class="accent">Accuracy.</span>
            </h1>

            <div class="hero-copy">
                A smarter way to evaluate AI-generated responses.
                Review relevance, factual accuracy, completeness
                and unsupported claims with specialized agent judges,
                then turn the findings into a clear quality report.
            </div>

            <div class="pill-row">
                <span class="pill">Evidence-led checks</span>
                <span class="pill">Multi-agent evaluation</span>
                <span class="pill">Clear quality reports</span>
            </div>
        </div>
        """)

        st.html(hero_html)

    with right_col:
        if IMAGE_PATH.exists():
            st.image(
                str(IMAGE_PATH),
                use_container_width=True,
            )
        else:
            st.warning(
                f"Hero image not found: {IMAGE_PATH.name}"
            )

# ---------------- HERO BUTTONS ----------------

with st.container(key="hero_actions"):
    a, b, _ = st.columns([1.15, 1.6, 4.25])

    with a:
        if st.button(
            "Start free",
            type="primary",
            use_container_width=True,
            key="hero_start",
        ):
            signup_dialog()

    with b:
        if st.button(
            "Explore evaluation",
            use_container_width=True,
            key="hero_explore",
        ):
            st.switch_page("pages/2_Evaluation_Hub.py")




# ---------------- FEATURES ----------------

st.html("""
<div id="features" class="section-head">
    <div class="kicker">
        One response. Multiple perspectives.
    </div>

    <div class="section-title">
        Quality checks that work together
    </div>

    <div class="section-copy">
        Review important dimensions of an AI answer
        in one structured workflow, with findings
        that are easier to understand.
    </div>
</div>
""")

with st.container(key="feature_section"):

    cols = st.columns(3, gap="medium")

    cards = [
        (
            "◎",
            "Evidence-led checks",
            "Review AI-generated responses against "
            "the question and trusted reference material.",
        ),
        (
            "✓",
            "Accuracy and coverage",
            "Inspect factual accuracy, relevance and "
            "whether important parts of the question "
            "were addressed.",
        ),
        (
            "⚠",
            "Clear quality reports",
            "Highlight unsupported claims and organize "
            "evaluation findings into a readable report.",
        ),
    ]

    for col, (icon, title, description) in zip(cols, cards):
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

# ---------------- HOW THE FIVE AGENTS WORK ----------------

st.html("""
<div class="section-head" id="workflow">
    <div class="kicker">INSIDE THE EVALAI ENGINE</div>
    <div class="section-title">
        Five AI agents. One quality verdict.
    </div>
    <div class="section-copy">
        Each agent has a specific responsibility.
        Their findings are brought together to produce
        an explainable assessment of an AI-generated response.
    </div>
</div>
""")

# STEP 1: INPUT

st.markdown(
    """
<div class="agent-input-panel">
    <div class="eval-label">STEP 01 · INPUT</div>
    <h3>Start with an AI-generated response</h3>
    <p>
        Submit a question and the AI answer you want to evaluate.
        You can also provide a reference answer or source document
        to help the system assess factual claims.
    </p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="agent-connector">↓</div>', unsafe_allow_html=True)

# STEP 2: KNOWLEDGE BASE AND RAG

st.markdown(
    """
<div class="pipeline-card">
    <div class="pipeline-tag">STEP 02 · EVIDENCE</div>
    <h3>Reference Knowledge Base &amp; RAG</h3>
    <p>
        When reference material is available, the RAG pipeline
        retrieves relevant source content to support grounded
        evaluation and help identify unsupported claims.
    </p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="agent-connector">↓</div>', unsafe_allow_html=True)

st.html("""
<div class="section-head">
    <div class="kicker">STEP 03 · MULTI-AGENT JUDGING</div>
    <div class="section-title">
        Four judges examine different dimensions.
    </div>
    <div class="section-copy">
        Each judge evaluates a separate aspect of response
        quality and provides a score with reasoning.
    </div>
</div>
""")

# FOUR JUDGE AGENTS

agent_cols = st.columns(4, gap="medium")

agents = [
    (
        "AGENT 01",
        "Relevance Judge",
        "Checks how directly and appropriately the answer "
        "addresses the original question.",
    ),
    (
        "AGENT 02",
        "Accuracy Judge",
        "Checks factual correctness against the provided "
        "reference answer or source evidence.",
    ),
    (
        "AGENT 03",
        "Hallucination Detection",
        "Flags claims that are not supported by the available "
        "reference source and identifies relevant evidence.",
    ),
    (
        "AGENT 04",
        "Completeness Judge",
        "Checks whether the answer covers the important aspects "
        "of the question and identifies omissions.",
    ),
]

for col, (number, title, description) in zip(agent_cols, agents):
    with col:
        st.markdown(
            f"""
            <div class="agent-card">
                <div class="agent-number">{number}</div>
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="agent-connector">↓</div>', unsafe_allow_html=True)

# STEP 4: VERDICT AGENT

st.markdown(
    """
<div class="agent-verdict">
    <div class="eval-label">AGENT 05 · FINAL DECISION</div>
    <h3>Verdict Agent</h3>
    <p>
        Combines the four judges' findings using a weighted
        scoring model and produces an overall verdict:
        Pass, Needs Improvement, or Fail.
        The consolidated reasoning explains the assessment.
    </p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="agent-connector">↓</div>', unsafe_allow_html=True)

# STEP 5: RESULTS

st.html("""
<div class="section-head">
    <div class="kicker">STEP 05 · RESULTS</div>
    <div class="section-title">
        Turn individual findings into useful insights.
    </div>
    <div class="section-copy">
        The results interface is designed to make response
        quality easier to inspect, compare and improve.
    </div>
</div>
""")

result_cols = st.columns(3, gap="medium")

outputs = [
    (
        "Per-agent explanations",
        "Inspect individual dimension scores, reasoning "
        "and flagged unsupported claims.",
    ),
    (
        "Batch evaluation",
        "Submit a CSV of question-answer pairs and review "
        "results across an entire dataset.",
    ),
    (
        "Quality analytics",
        "Explore dimension breakdowns, pass/fail rates, "
        "hallucination frequency and quality trends.",
    ),
]

for col, (title, description) in zip(result_cols, outputs):
    with col:
        st.markdown(
            f"""
            <div class="agent-output">
                <h4>{title}</h4>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ---------------- BOTTOM CTA ----------------

st.markdown(
    """
<div class="bottom-cta">
    <div class="kicker">BUILT FOR MORE TRUSTWORTHY AI</div>
    <div class="section-title">
        Bring evidence into every evaluation.
    </div>
    <div class="section-copy">
        Explore a structured approach to response quality,
        with an emphasis on accuracy, relevance and
        transparent evaluation findings.
    </div>
</div>
""",
    unsafe_allow_html=True,
)

_, cta_col, _ = st.columns([1, 1.8, 1])

with cta_col:
    if st.button(
        "Explore evaluation workspace",
        type="primary",
        use_container_width=True,
        key="bottom_signup",
    ):
        st.switch_page("pages/2_Evaluation_Hub.py")


# ---------------- FOOTER ----------------

st.markdown(
    """
<div class="footer">
    <span>
        <strong>EvalAI</strong> · AI Response Quality Platform
    </span>
    <span>
        Evaluate AI with greater clarity and confidence.
    </span>
</div>
""",
    unsafe_allow_html=True,
)