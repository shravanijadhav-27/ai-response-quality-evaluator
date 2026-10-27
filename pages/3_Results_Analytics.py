
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Quality Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------- PROFESSIONAL STYLING ----------
st.markdown("""
<style>
    .stApp {
        background-color: #F4F7FC;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1450px;
    }

    h1, h2, h3 {
        color: #142B4A;
    }

    .dashboard-header {
        background: linear-gradient(120deg, #142B4A, #2459A9);
        padding: 28px 30px;
        border-radius: 16px;
        color: white;
        margin-bottom: 22px;
    }

    .dashboard-header h1 {
        color: white;
        font-size: 30px;
        margin-bottom: 8px;
    }

    .dashboard-header p {
        color: #E3ECFA;
        margin-bottom: 0;
        font-size: 15px;
    }

    .metric-card {
        background: white;
        padding: 20px;
        border: 1px solid #E1E8F2;
        border-radius: 14px;
        min-height: 125px;
        box-shadow: 0 3px 12px rgba(24, 53, 91, 0.05);
    }

    .metric-label {
        color: #687991;
        font-size: 14px;
        font-weight: 600;
    }

    .metric-value {
        color: #142B4A;
        font-size: 29px;
        font-weight: 700;
        margin-top: 9px;
    }

    .section-caption {
        color: #687991;
        font-size: 14px;
        margin-top: -8px;
        margin-bottom: 18px;
    }

    div[data-testid="stDataFrame"] {
        background: white;
        border-radius: 12px;
    }

    div.stDownloadButton > button {
        background-color: #2459A9;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 18px;
    }

    div.stDownloadButton > button:hover {
        background-color: #142B4A;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.markdown("""
<div class="dashboard-header">
    <h1>AI Response Quality Dashboard</h1>
    <p>Monitor evaluation performance, response quality and AI reliability.</p>
</div>
""", unsafe_allow_html=True)

st.warning(
    "DEMO MODE — The results below are sample data, not real evaluations."
)

# ---------- SAMPLE DATA ----------

data = {
    "Evaluation ID": ["EV001", "EV002", "EV003", "EV004", "EV005"],
    "Accuracy": [90, 75, 95, 60, 85],
    "Relevance": [85, 80, 90, 70, 88],
    "Completeness": [80, 70, 95, 65, 82],
    "Hallucination": [10, 25, 5, 40, 15],
    "Verdict": ["PASS", "PASS", "PASS", "FAIL", "PASS"],
    "Evidence": [
        "Supported by the retrieved source.",
        "Mostly relevant; one detail needs verification.",
        "Claims supported by retrieved documents.",
        "Several claims lack supporting evidence.",
        "Answer aligns with the available evidence."
    ]
}

df = pd.DataFrame(data)

df["Quality Score"] = df[
    ["Accuracy", "Relevance", "Completeness"]
].mean(axis=1).round(1)


df = pd.DataFrame(data)

df["Quality Score"] = df[
    ["Accuracy", "Relevance", "Completeness"]
].mean(axis=1).round(1)

# ---------- KPI CARDS ----------
st.subheader("Performance Overview")
st.markdown(
    '<p class="section-caption">A quick snapshot of evaluation performance.</p>',
    unsafe_allow_html=True
)

total = len(df)
average = df["Quality Score"].mean()
passed = int((df["Verdict"] == "PASS").sum())
failed = int((df["Verdict"] == "FAIL").sum())

cards = [
    ("TOTAL EVALUATIONS", str(total), "📋"),
    ("AVERAGE QUALITY", f"{average:.1f}%", "🎯"),
    ("PASSED", str(passed), "✅"),
    ("FAILED", str(failed), "⚠️"),
]

columns = st.columns(4)

for column, (label, value, emoji) in zip(columns, cards):
    with column:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{emoji} &nbsp; {label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.divider()

# ---------- CHARTS ----------
st.subheader("Quality Insights")
st.markdown(
    '<p class="section-caption">Compare quality dimensions and individual evaluations.</p>',
    unsafe_allow_html=True
)

left, right = st.columns(2)

with left:
    st.markdown("#### Quality by Dimension")

    dimension_df = pd.DataFrame({
        "Dimension": ["Accuracy", "Relevance", "Completeness"],
        "Average Score": [
            df["Accuracy"].mean(),
            df["Relevance"].mean(),
            df["Completeness"].mean()
        ]
    }).set_index("Dimension")

    st.bar_chart(
        dimension_df,
        y="Average Score",
        color="#3478D4",
        height=300
    )

with right:
    st.markdown("#### Quality Score by Evaluation")

    score_df = df.set_index("Evaluation ID")[["Quality Score"]]

    st.bar_chart(
        score_df,
        y="Quality Score",
        color="#20A486",
        height=300
    )

st.divider()

# ---------- VERDICT SUMMARY ----------
st.subheader("Evaluation Outcomes")

outcome_col1, outcome_col2 = st.columns([1, 2])

with outcome_col1:
    st.markdown("#### Pass vs Fail")
    outcome_df = pd.DataFrame({
        "Outcome": ["Pass", "Fail"],
        "Evaluations": [passed, failed]
    }).set_index("Outcome")

    st.bar_chart(outcome_df, color="#3478D4", height=220)

with outcome_col2:
    st.markdown("#### Dimension Score Summary")

    summary = pd.DataFrame({
        "Dimension": ["Accuracy", "Relevance", "Completeness"],
        "Average Score": [
            round(df["Accuracy"].mean(), 1),
            round(df["Relevance"].mean(), 1),
            round(df["Completeness"].mean(), 1)
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Average Score": st.column_config.ProgressColumn(
                "Average Score (%)",
                min_value=0,
                max_value=100,
                format="%.1f%%"
            )
        }
    )

st.divider()

# ---------- HISTORY TABLE ----------
st.subheader("Evaluation History")
st.markdown(
    '<p class="section-caption">Review individual evaluation results.</p>',
    unsafe_allow_html=True
)

display_df = df.copy()

display_df["Verdict"] = display_df["Verdict"].map({
    "PASS": "✅ PASS",
    "FAIL": "❌ FAIL"
})

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Accuracy": st.column_config.ProgressColumn(
            "Accuracy (%)", min_value=0, max_value=100, format="%d%%"
        ),
        "Relevance": st.column_config.ProgressColumn(
            "Relevance (%)", min_value=0, max_value=100, format="%d%%"
        ),
        "Completeness": st.column_config.ProgressColumn(
            "Completeness (%)", min_value=0, max_value=100, format="%d%%"
        ),
        "Quality Score": st.column_config.ProgressColumn(
            "Quality Score (%)",
            min_value=0,
            max_value=100,
            format="%.1f%%"
        ),
        "Hallucination": st.column_config.ProgressColumn(
            "Hallucination Risk (%)",
            min_value=0,
            max_value=100,
            format="%d%%"
        )
    }
)

# ---------- INDIVIDUAL EVALUATION DETAILS ----------
st.divider()
st.subheader("🔍 Individual Evaluation Details")

selected_id = st.selectbox(
    "Select an Evaluation",
    df["Evaluation ID"]
)

selected = df[df["Evaluation ID"] == selected_id].iloc[0]

score1, score2, score3, score4 = st.columns(4)

score1.metric("Accuracy Judge", f"{selected['Accuracy']}%")
score2.metric("Relevance Judge", f"{selected['Relevance']}%")
score3.metric("Completeness Judge", f"{selected['Completeness']}%")
score4.metric("Hallucination Risk", f"{selected['Hallucination']}%")

st.markdown("#### Final Verdict")

if selected["Verdict"] == "PASS":
    st.success("PASS — Sample evaluation meets the demo criteria.")
else:
    st.error("FAIL — Sample evaluation requires further review.")

st.markdown("#### Supporting Evidence")

st.info(selected["Evidence"])

st.caption(
    "Demo evidence only. Replace this text with actual retrieved "
    "document excerpts and citations when backend integration is ready."
)

# ---------- CSV REPORT ----------
csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Evaluation Report (CSV)",
    data=csv_data,
    file_name="ai_evaluation_report.csv",
    mime="text/csv"
)

st.write("")

if st.button("← Back to Home"):
    st.switch_page("pages/1_Home.py")

st.caption(
    "AI Response Quality Evaluator | Analytics Preview | Sample Data"
)
