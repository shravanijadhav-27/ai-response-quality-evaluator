import streamlit as st

st.set_page_config(
    page_title="AI Response Evaluator",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- CSS styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #F5F8FD;
    color: #10264B;
}

.block-container {
    padding: 1.5rem 1.8rem 2rem;
    max-width: 1600px;
}

.project-banner {
    display: flex;
    align-items: center;
    gap: 16px;
    min-height: 112px;
    padding: 22px 28px;
    margin: 32px 0 28px;
    border-radius: 14px;
    background: linear-gradient(100deg, #10264B, #2459A9);
}

.project-banner-icon {
    display: grid;
    place-items: center;
    flex: 0 0 60px;
    height: 60px;
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.14);
    font-size: 38px;
}

.project-banner h1 {
    margin: 0;
    color: #FFFFFF;
    font-size: clamp(20px, 2.2vw, 28px);
    font-weight: 750;
    line-height: 1.3;
}

.project-banner p {
    margin: 5px 0 0;
    color: #D7E5FF;
    font-size: 13px;
}

.hero {
    background: linear-gradient(115deg, #EDF4FF 0%, #DFEBFF 100%);
    border: 1px solid #DFE9FA;
    border-radius: 18px;
    padding: 34px 30px;
    margin-bottom: 25px;
}

.eyebrow {
    display: inline-block;
    background: #D2E3FF;
    color: #1558C0;
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 12px;
}

.hero h1 {
    color: #102B57;
    font-size: clamp(28px, 3vw, 43px);
    font-weight: 800;
    line-height: 1.18;
    margin: 0 0 15px 0;
}

.hero p {
    color: #49648D;
    font-size: 15px;
    line-height: 1.8;
}

.hero-art {
    text-align: center;
    font-size: 100px;
    padding: 10px 0;
}

.section-title {
    font-size: 25px;
    font-weight: 800;
    color: #102B57;
    margin: 18px 0 4px;
}

.section-subtitle {
    color: #657A9B;
    font-size: 13px;
    margin-bottom: 18px;
}

.measure-card {
    background: white;
    border: 1px solid #E0E8F4;
    border-radius: 13px;
    padding: 20px 17px;
    min-height: 265px;
    height: 100%;
    box-shadow: 0 2px 7px rgba(20, 45, 85, 0.025);
}

.measure-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    font-size: 24px;
    margin-bottom: 15px;
}

.measure-card h3 {
    font-size: 16px;
    font-weight: 750;
    color: #102B57;
    margin-bottom: 10px;
}

.measure-card p {
    color: #536987;
    font-size: 12px;
    line-height: 1.8;
    min-height: 65px;
}

.measure-note {
    padding: 11px;
    border-radius: 10px;
    font-size: 11px;
    line-height: 1.7;
    margin-top: 12px;
}

.verdict-panel {
    background: linear-gradient(110deg, #EFF5FF, #F8FAFF);
    border: 1px solid #DFE8F8;
    border-radius: 14px;
    padding: 23px;
    margin-top: 25px;
    margin-bottom: 22px;
}

.verdict-title {
    font-size: 20px;
    font-weight: 750;
    color: #102B57;
}

.verdict-copy {
    font-size: 12px;
    color: #536987;
    line-height: 1.8;
}

.verdict-pill {
    display: inline-block;
    padding: 9px 13px;
    border-radius: 25px;
    font-size: 11px;
    font-weight: 700;
    margin: 4px 2px;
}

.workflow {
    background: #EDF3FC;
    border-radius: 14px;
    padding: 20px 23px;
    margin-top: 15px;
}

.workflow-title {
    font-size: 18px;
    font-weight: 800;
    color: #102B57;
    margin-bottom: 16px;
}

.step-icon {
    font-size: 28px;
    background: #D9E7FF;
    border-radius: 50%;
    width: 53px;
    height: 53px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.step-title {
    font-size: 13px;
    font-weight: 750;
    color: #143565;
}

.step-copy {
    font-size: 11px;
    color: #657A9B;
    line-height: 1.7;
}

.footer {
    color: #7585A0;
    font-size: 10px;
    text-align: center;
    padding: 20px 0 5px;
}

.stButton button[kind="primary"] {
    background: #2867F0;
    border: 1px solid #2867F0;
    border-radius: 9px;
    min-height: 43px;
    font-weight: 650;
}

.stButton button[kind="primary"]:hover {
    background: #174FC8;
    border-color: #174FC8;
}

.stButton button[kind="secondary"] {
    border-radius: 9px;
    border: 1px solid #CBD9EF;
    min-height: 43px;
    color: #17345F;
}

@media (max-width: 700px) {
    .block-container {
        padding: 1rem;
    }
    .project-banner {
        min-height: 100px;
        padding: 18px 16px;
        gap: 12px;
    }
    .project-banner-icon {
        flex-basis: 48px;
        height: 48px;
        font-size: 30px;
    }
    .hero {
        padding: 23px 18px;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="project-banner">
        <div class="project-banner-icon">🛡️</div>
        <div>
            <h1>AI Response Quality Evaluator Agent</h1>
            <p>Intelligent evaluation · Reliable answers · Better AI quality</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Hero section ----------
hero_left, hero_right = st.columns([1.55, 1])

with hero_left:
    st.markdown("""
    <div class="hero">
        <div class="eyebrow">AI Response Evaluator</div>
        <h1>Evaluate AI Responses<br>with Confidence</h1>
        <p>
            Our multi-agent evaluation system assesses AI-generated
            answers for relevance, accuracy, completeness, and
            hallucinations — helping you make better, more informed decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    b1, b2 = st.columns([1, 1.25])

    with b1:
        if st.button(
            "▶  Start Evaluation",
            type="primary",
            use_container_width=True,
        ):
            st.switch_page("pages/evaluation_hub.py")

    with b2:
        if st.button(
            "▦  View Results Dashboard",
            use_container_width=True,
        ):
            st.info("Results & Analytics is still under development.")

with hero_right:
    st.markdown("""
    <div class="hero">
        <div class="hero-art">🤖</div>
        <div style="text-align:center; font-weight:750;
                    font-size:17px; color:#174A99;">
            Better Answers<br>Higher Quality
        </div>
        <div style="background:white; padding:14px 18px;
                    border-radius:12px; margin-top:15px;
                    border:1px solid #DCE7F8; font-size:13px;
                    line-height:2.1; color:#24436E;">
            🔵 &nbsp; Relevance<br>
            🟢 &nbsp; Accuracy<br>
            🟣 &nbsp; Hallucination Detection<br>
            🟠 &nbsp; Completeness
        </div>
    </div>
    """, unsafe_allow_html=True)


# ---------- Evaluation measures ----------
st.markdown(
    '<div class="section-title">Evaluation Measures</div>'
    '<div class="section-subtitle">'
    'Every submitted response will be assessed across these four dimensions.'
    '</div>',
    unsafe_allow_html=True,
)

measures = [
    {
        "icon": "🎯",
        "title": "Relevance",
        "color": "#2671F5",
        "bg": "#EAF2FF",
        "description": (
            "Measures how directly the answer addresses the user's "
            "question and stays on topic."
        ),
        "note": "Evaluation: relevance score and explanation.",
    },
    {
        "icon": "✅",
        "title": "Accuracy",
        "color": "#079768",
        "bg": "#E3F8F0",
        "description": (
            "Checks whether factual claims are correct and consistent "
            "with available reference answers or evidence."
        ),
        "note": "Evaluation: accuracy score and explanation.",
    },
    {
        "icon": "🔎",
        "title": "Hallucination Detection",
        "color": "#7540D8",
        "bg": "#F2EBFF",
        "description": (
            "Identifies claims that are fabricated, unsupported, "
            "or contradicted by the available evidence."
        ),
        "note": "Evaluation: flagged claims and supporting evidence.",
    },
    {
        "icon": "📋",
        "title": "Completeness",
        "color": "#C77712",
        "bg": "#FFF2DF",
        "description": (
            "Checks whether the answer includes all important "
            "points needed to answer the question."
        ),
        "note": "Evaluation: completeness score and missing information.",
    },
]

cols = st.columns(4, gap="medium")

for col, item in zip(cols, measures):
    with col:
        st.markdown(f"""
        <div class="measure-card">
            <div class="measure-icon"
                 style="background:{item['bg']}; color:{item['color']};">
                {item['icon']}
            </div>
            <h3>{item['title']}</h3>
            <p>{item['description']}</p>
            <div class="measure-note"
                 style="background:{item['bg']}; color:{item['color']};">
                {item['note']}
            </div>
        </div>
        """, unsafe_allow_html=True)


# ---------- Overall verdict ----------
st.markdown("""
<div class="verdict-panel">
    <div class="verdict-title">⚖️ &nbsp; Overall Verdict</div>
    <div class="verdict-copy">
        The Verdict Agent combines the evaluation results into one final
        outcome based on predefined thresholds and scoring rules.
    </div>
    <br>
    <span class="verdict-pill"
          style="background:#DDF8EB;color:#087A4B;">
        ● Pass
    </span>
    <span class="verdict-pill"
          style="background:#FFF2CC;color:#986000;">
        ⚠ Needs Improvement
    </span>
    <span class="verdict-pill"
          style="background:#FFE5E8;color:#C22D42;">
        ✕ Fail
    </span>
    <div class="verdict-copy" style="margin-top:12px;">
        Final thresholds and scoring rules will be agreed with the backend team.
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- How it works ----------
st.markdown("""
<div class="workflow">
    <div class="workflow-title">How It Works</div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown("""
    <div class="step-icon">📄</div>
    <br>
    <div class="step-title">1. Submit</div>
    <div class="step-copy">
        Enter a response for individual evaluation or upload a CSV
        file for batch evaluation.
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="step-icon">🧠</div>
    <br>
    <div class="step-title">2. Evaluate</div>
    <div class="step-copy">
        Specialized judge agents score the response using the
        agreed evaluation criteria.
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="step-icon">📊</div>
    <br>
    <div class="step-title">3. Review</div>
    <div class="step-copy">
        Review dimension scores, the final verdict, supporting
        evidence, and downloadable reports.
    </div>
    """, unsafe_allow_html=True)


# ---------- Footer ----------
st.markdown("""
<div class="footer">
    AI Response Quality Evaluator &nbsp; · &nbsp; Built with Streamlit
</div>
""", unsafe_allow_html=True)
