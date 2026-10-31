
import streamlit as st
import pandas as pd

from ui import apply_design, render_sidebar


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="EvalAI | Results Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_design()
render_sidebar()


# =========================================================
# CUSTOM DESIGN
# =========================================================

st.markdown("""
<style>

/* ===== FIXED PAGE BACKGROUND ===== */

html,
body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.stApp {
    background: linear-gradient(
        135deg,
        #F2F6FD 0%,
        #EAF1FC 50%,
        #F3F5FC 100%
    ) !important;

    background-attachment: fixed !important;
    background-size: cover !important;
}

[data-testid="stHeader"],
[data-testid="stMain"] > div,
[data-testid="stMainBlockContainer"] {
    background: transparent !important;
}

/* ===== PAGE SPACING ===== */

.block-container {
    max-width: 1480px;
    padding-top: 1.8rem;
    padding-bottom: 3rem;
}

/* ===== TYPOGRAPHY ===== */

h1, h2, h3, h4 {
    color: #172E50 !important;
    font-weight: 700 !important;
}

p {
    color: #536985;
}

/* ===== HERO HEADER ===== */

.analytics-hero {
    position: relative;
    overflow: hidden;
    background: linear-gradient(
        115deg,
        #142B4A 0%,
        #1C477F 55%,
        #315FA8 100%
    );
    padding: 34px 36px;
    border-radius: 19px;
    margin-bottom: 22px;
    box-shadow: 0 10px 28px rgba(28, 58, 100, 0.13);
}

.analytics-hero:after {
    content: "";
    position: absolute;
    width: 230px;
    height: 230px;
    right: -75px;
    top: -110px;
    border: 1px solid rgba(255,255,255,0.13);
    border-radius: 50%;
    box-shadow:
        0 0 0 28px rgba(255,255,255,0.035),
        0 0 0 58px rgba(255,255,255,0.025);
}

.analytics-hero h1 {
    color: #FFFFFF !important;
    font-size: 32px !important;
    margin: 0 0 9px 0;
}

.analytics-hero p {
    color: #DCE8FA !important;
    font-size: 15px;
    margin: 0;
    max-width: 750px;
}

.hero-tag {
    display: inline-block;
    background: rgba(255,255,255,0.13);
    color: #EAF2FF;
    border: 1px solid rgba(255,255,255,0.18);
    padding: 6px 12px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.8px;
    margin-bottom: 15px;
}

/* ===== SECTION HEADINGS ===== */

.section-heading {
    color: #172E50;
    font-size: 21px;
    font-weight: 750;
    margin-bottom: 5px;
}

.section-description {
    color: #71839C;
    font-size: 13px;
    margin-bottom: 18px;
}

/* ===== KPI CARDS ===== */

.kpi-card {
    background: #FFFFFF;
    border: 1px solid #DFE7F3;
    border-radius: 15px;
    padding: 21px 20px;
    min-height: 142px;
    box-shadow: 0 5px 16px rgba(34, 62, 103, 0.055);
    position: relative;
    overflow: hidden;
}

.kpi-card:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
}

.kpi-blue:before {
    background: #3478D4;
}

.kpi-purple:before {
    background: #8064D8;
}

.kpi-green:before {
    background: #20A486;
}

.kpi-orange:before {
    background: #E69A45;
}

.kpi-label {
    color: #71829A;
    font-size: 11px;
    font-weight: 750;
    letter-spacing: 0.7px;
}

.kpi-value {
    color: #172E50;
    font-size: 31px;
    font-weight: 800;
    margin-top: 12px;
    line-height: 1.2;
}

.kpi-description {
    color: #8A9AB0;
    font-size: 11px;
    margin-top: 7px;
}

/* ===== WHITE CHART PANELS ===== */

.chart-panel {
    background: #FFFFFF;
    border: 1px solid #DFE7F3;
    border-radius: 16px;
    padding: 20px 21px;
    box-shadow: 0 5px 17px rgba(34, 62, 103, 0.045);
    margin-bottom: 8px;
}

.panel-title {
    color: #1B3457;
    font-size: 16px;
    font-weight: 750;
    margin-bottom: 4px;
}

.panel-subtitle {
    color: #8A99AD;
    font-size: 12px;
    margin-bottom: 12px;
}

/* ===== INSIGHT CARDS ===== */

.insight-card {
    border-radius: 15px;
    padding: 21px;
    min-height: 170px;
    border: 1px solid transparent;
}

.insight-strength {
    background: #EAF6F2;
    border-color: #CBE9DD;
}

.insight-improve {
    background: #FFF4E9;
    border-color: #F3DFC4;
}

.insight-risk {
    background: #F0EEFC;
    border-color: #DDD8F6;
}

.insight-kicker {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.8px;
    margin-bottom: 10px;
}

.insight-strength .insight-kicker {
    color: #188365;
}

.insight-improve .insight-kicker {
    color: #B87527;
}

.insight-risk .insight-kicker {
    color: #7057B8;
}

.insight-title {
    color: #203958;
    font-size: 19px;
    font-weight: 750;
    margin-bottom: 8px;
}

.insight-description {
    color: #60738B;
    font-size: 13px;
    line-height: 1.55;
}

/* ===== FILTERS ===== */

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background: #FFFFFF !important;
    border-color: #D7E1EF !important;
    border-radius: 9px !important;
}

/* ===== TABLE ===== */

div[data-testid="stDataFrame"] {
    background: #FFFFFF !important;
    border: 1px solid #DFE7F3;
    border-radius: 13px;
    overflow: hidden;
}

/* ===== BUTTONS ===== */

.stButton > button {
    background: #2459A9 !important;
    color: #FFFFFF !important;
    border: 1px solid #2459A9 !important;
    border-radius: 9px !important;
    font-weight: 650 !important;
}

.stButton > button:hover {
    background: #173C70 !important;
    border-color: #173C70 !important;
    color: #FFFFFF !important;
}

/* ===== DIVIDERS AND ALERTS ===== */

hr {
    border-color: #D8E2F0 !important;
}

[data-testid="stAlert"] {
    border-radius: 11px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO HEADER
# =========================================================

st.markdown("""
<div class="analytics-hero">
    <div class="hero-tag">EVALAI ANALYTICS</div>
    <h1>Results Analytics</h1>
    <p>
        Turn evaluation results into meaningful insights.
        Monitor AI response quality, compare performance,
        and identify opportunities for improvement.
    </p>
</div>
""", unsafe_allow_html=True)

st.warning(
    "DEMO MODE — The records shown are illustrative sample data, "
    "not actual evaluations from your backend."
)


# =========================================================
# SAMPLE DATA
# Replace with actual backend records after integration.
# =========================================================

data = {
    "Evaluation ID": ["EV001", "EV002", "EV003", "EV004", "EV005"],
    "Evaluation Date": pd.to_datetime([
        "2026-10-20",
        "2026-10-22",
        "2026-10-24",
        "2026-10-27",
        "2026-10-29"
    ]),
    "Accuracy": [90, 75, 95, 60, 85],
    "Relevance": [85, 80, 90, 70, 88],
    "Completeness": [80, 70, 95, 65, 82],
    "Hallucination Risk": [10, 25, 5, 40, 15],
    "Verdict": ["PASS", "PASS", "PASS", "FAIL", "PASS"]
}

df = pd.DataFrame(data)

df["Quality Score"] = (
    df[["Accuracy", "Relevance", "Completeness"]]
    .mean(axis=1)
    .round(1)
)

df["Hallucination Control"] = 100 - df["Hallucination Risk"]


# =========================================================
# FILTERS
# =========================================================

st.markdown(
    '<div class="section-heading">Filter Evaluations</div>'
    '<div class="section-description">'
    'Choose a date range and evaluation outcome to customise your dashboard.'
    '</div>',
    unsafe_allow_html=True
)

filter_col1, filter_col2 = st.columns([1.5, 1])

minimum_date = df["Evaluation Date"].min().date()
maximum_date = df["Evaluation Date"].max().date()

with filter_col1:
    selected_dates = st.date_input(
        "Evaluation date range",
        value=(minimum_date, maximum_date),
        min_value=minimum_date,
        max_value=maximum_date
    )

with filter_col2:
    selected_verdict = st.selectbox(
        "Evaluation outcome",
        ["All outcomes", "PASS", "FAIL"]
    )

filtered_df = df.copy()

if isinstance(selected_dates, tuple) and len(selected_dates) == 2:
    start_date, end_date = selected_dates

    filtered_df = filtered_df[
        filtered_df["Evaluation Date"].dt.date.between(
            start_date, end_date
        )
    ]

if selected_verdict != "All outcomes":
    filtered_df = filtered_df[
        filtered_df["Verdict"] == selected_verdict
    ]


# =========================================================
# 1. EVALUATION OVERVIEW
# =========================================================

st.divider()

st.markdown(
    '<div class="section-heading">Performance Overview</div>'
    '<div class="section-description">'
    'A snapshot of your AI response evaluation performance.'
    '</div>',
    unsafe_allow_html=True
)

total = len(filtered_df)
average = filtered_df["Quality Score"].mean() if total else 0
passed = int((filtered_df["Verdict"] == "PASS").sum())
failed = int((filtered_df["Verdict"] == "FAIL").sum())

kpis = [
    ("TOTAL EVALUATIONS", str(total), "Records matching selected filters", "kpi-blue"),
    ("AVERAGE QUALITY", f"{average:.1f}%", "Average overall quality score", "kpi-purple"),
    ("PASSED", str(passed), "Evaluations meeting demo criteria", "kpi-green"),
    ("NEEDS IMPROVEMENT", str(failed), "Evaluations requiring review", "kpi-orange")
]

kpi_columns = st.columns(4)

for col, (label, value, description, style) in zip(kpi_columns, kpis):
    with col:
        st.markdown(f"""
        <div class="kpi-card {style}">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-description">{description}</div>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# EMPTY STATE
# =========================================================

if filtered_df.empty:

    st.write("")
    st.info(
        "No evaluation records match your selected filters. "
        "Try another date range or evaluation outcome."
    )

else:

    # =====================================================
    # 2. QUALITY BY DIMENSION
    # =====================================================

    st.write("")
    st.divider()

    st.markdown(
        '<div class="section-heading">Quality by Dimension</div>'
        '<div class="section-description">'
        'Understand how AI responses perform across the four quality dimensions.'
        '</div>',
        unsafe_allow_html=True
    )

    dimension_df = pd.DataFrame({
        "Dimension": [
            "Accuracy",
            "Relevance",
            "Completeness",
            "Hallucination Control"
        ],
        "Average Score": [
            filtered_df["Accuracy"].mean(),
            filtered_df["Relevance"].mean(),
            filtered_df["Completeness"].mean(),
            filtered_df["Hallucination Control"].mean()
        ]
    }).set_index("Dimension")

    st.markdown("""
    <div class="chart-panel">
        <div class="panel-title">Dimension Performance</div>
        <div class="panel-subtitle">
            Average score across the selected evaluation records
        </div>
    """, unsafe_allow_html=True)

    st.bar_chart(
        dimension_df,
        y="Average Score",
        color="#527FE0",
        height=310
    )

    st.caption(
        "Higher scores indicate better performance. "
        "Hallucination Control = 100 minus hallucination risk."
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # =====================================================
    # 3. QUALITY TRENDS
    # =====================================================

    st.write("")
    st.divider()

    st.markdown(
        '<div class="section-heading">Quality Trends</div>'
        '<div class="section-description">'
        'Observe how average response quality changes over evaluation dates.'
        '</div>',
        unsafe_allow_html=True
    )

    trend_df = (
        filtered_df
        .groupby("Evaluation Date")["Quality Score"]
        .mean()
        .to_frame()
        .sort_index()
    )

    st.markdown("""
    <div class="chart-panel">
        <div class="panel-title">Quality Score Over Time</div>
        <div class="panel-subtitle">
            Average quality score grouped by evaluation date
        </div>
    """, unsafe_allow_html=True)

    st.line_chart(
        trend_df,
        color="#8064D8",
        height=290
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # =====================================================
    # 4. EVALUATION HISTORY
    # =====================================================

    st.write("")
    st.divider()

    st.markdown(
        '<div class="section-heading">Evaluation History</div>'
        '<div class="section-description">'
        'Review completed evaluations and compare their quality scores.'
        '</div>',
        unsafe_allow_html=True
    )

    history_df = filtered_df[
        [
            "Evaluation ID",
            "Evaluation Date",
            "Accuracy",
            "Relevance",
            "Completeness",
            "Hallucination Risk",
            "Quality Score",
            "Verdict"
        ]
    ].copy()

    history_df["Evaluation Date"] = (
        history_df["Evaluation Date"].dt.strftime("%d %b %Y")
    )

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Accuracy": st.column_config.ProgressColumn(
                "Accuracy (%)",
                min_value=0,
                max_value=100,
                format="%d%%"
            ),
            "Relevance": st.column_config.ProgressColumn(
                "Relevance (%)",
                min_value=0,
                max_value=100,
                format="%d%%"
            ),
            "Completeness": st.column_config.ProgressColumn(
                "Completeness (%)",
                min_value=0,
                max_value=100,
                format="%d%%"
            ),
            "Hallucination Risk": st.column_config.ProgressColumn(
                "Hallucination Risk (%)",
                min_value=0,
                max_value=100,
                format="%d%%"
            ),
            "Quality Score": st.column_config.ProgressColumn(
                "Quality Score (%)",
                min_value=0,
                max_value=100,
                format="%.1f%%"
            )
        }
    )


    # =====================================================
    # 5. QUALITY INSIGHTS
    # =====================================================

    st.write("")
    st.divider()

    st.markdown(
        '<div class="section-heading">Quality Insights</div>'
        '<div class="section-description">'
        'Identify strengths, areas for improvement, and reliability concerns.'
        '</div>',
        unsafe_allow_html=True
    )

    dimension_averages = {
        "Accuracy": filtered_df["Accuracy"].mean(),
        "Relevance": filtered_df["Relevance"].mean(),
        "Completeness": filtered_df["Completeness"].mean(),
        "Hallucination Control": filtered_df["Hallucination Control"].mean()
    }

    strongest = max(dimension_averages, key=dimension_averages.get)
    weakest = min(dimension_averages, key=dimension_averages.get)

    strongest_score = dimension_averages[strongest]
    weakest_score = dimension_averages[weakest]

    average_risk = filtered_df["Hallucination Risk"].mean()

    insight_col1, insight_col2, insight_col3 = st.columns(3, gap="medium")

    with insight_col1:
        st.markdown(f"""
        <div class="insight-card insight-strength">
            <div class="insight-kicker">✦ STRONGEST DIMENSION</div>
            <div class="insight-title">{strongest}</div>
            <div class="insight-description">
                Average score: <b>{strongest_score:.1f}%</b><br>
                This is currently the strongest-performing quality dimension.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with insight_col2:
        st.markdown(f"""
        <div class="insight-card insight-improve">
            <div class="insight-kicker">↗ AREA FOR IMPROVEMENT</div>
            <div class="insight-title">{weakest}</div>
            <div class="insight-description">
                Average score: <b>{weakest_score:.1f}%</b><br>
                Focus on improving this dimension in future evaluations.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with insight_col3:
        st.markdown(f"""
        <div class="insight-card insight-risk">
            <div class="insight-kicker">◎ RELIABILITY INDICATOR</div>
            <div class="insight-title">{average_risk:.1f}% Risk</div>
            <div class="insight-description">
                Average hallucination risk across the selected records.
                Review unsupported claims and source evidence.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    if failed > 0:
        st.info(
            f"{failed} evaluation(s) need improvement. "
            "Review their individual reports in the Evaluation Hub."
        )
    else:
        st.success(
            "No failed evaluations were found in the selected records."
        )


# =========================================================
# FOOTER
# =========================================================

st.write("")
st.markdown("""
<div style="
    border-top: 1px solid #D9E3F0;
    padding-top: 15px;
    text-align: center;
    color: #8191A7;
    font-size: 12px;
">
    EvalAI &nbsp;|&nbsp; AI Response Quality Evaluator
    &nbsp;|&nbsp; Analytics Preview
</div>
""", unsafe_allow_html=True)
