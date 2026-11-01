import streamlit as st
import pandas as pd

from ui import apply_design, render_sidebar

st.set_page_config(
    page_title="CSV Batch Evaluation",
    page_icon="📂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

apply_design()
render_sidebar()

# =========================================================
# SOFT BLUE + NAVY DESIGN
# =========================================================

st.markdown("""
<style>

/* ---------- PAGE BACKGROUND ---------- */

.stApp,
[data-testid="stAppViewContainer"] {
    background: #EAF0F8 !important;
}

[data-testid="stHeader"] {
    background: #EAF0F8 !important;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* ---------- GENERAL TEXT ---------- */

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {
    color: #172B4D !important;
}

.stApp p,
.stApp label,
.stApp .stMarkdown {
    color: #425574;
}

/* ---------- HERO SECTION ---------- */

.batch-hero {
    background: linear-gradient(120deg, #172B4D, #244B78, #247A9B);
    border: 1px solid #3E7099;
    border-radius: 18px;
    padding: 30px;
    margin: 18px 0 28px 0;
    box-shadow: 0 8px 24px rgba(28, 52, 85, 0.12);
}

.batch-hero h1 {
    color: #FFFFFF !important;
    font-size: 32px;
    font-weight: 750;
    margin: 0;
}

.batch-hero p {
    color: #E3EFFB !important;
    font-size: 15px;
    margin: 10px 0 0 0;
}

.hero-tag {
    display: inline-block;
    color: #C8F7FF;
    background: #285475;
    border: 1px solid #5A91AD;
    border-radius: 30px;
    padding: 5px 12px;
    font-size: 12px;
    margin-bottom: 12px;
}

/* ---------- SECTION HEADINGS ---------- */

.section-title {
    color: #172B4D;
    font-size: 21px;
    font-weight: 700;
    margin: 25px 0 14px 0;
}

/* ---------- INFORMATION CARDS ---------- */

.info-card {
    background: #FFFFFF;
    border: 1px solid #D5E1EF;
    border-radius: 15px;
    padding: 22px;
    min-height: 165px;
    box-shadow: 0 5px 16px rgba(30, 55, 90, 0.06);
}

.info-card h4 {
    color: #172B4D !important;
    margin-top: 0;
}

.info-card p {
    color: #526581 !important;
    font-size: 14px;
    line-height: 1.6;
}

.column-chip {
    display: inline-block;
    background: #E5F5FA;
    border: 1px solid #B7DFEB;
    color: #12617A;
    padding: 7px 12px;
    border-radius: 7px;
    margin: 5px 5px 5px 0;
    font-family: monospace;
    font-size: 13px;
}

/* ---------- METRIC CARDS ---------- */

div[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 1px solid #D5E1EF !important;
    border-radius: 14px !important;
    padding: 18px !important;
    box-shadow: 0 5px 15px rgba(30, 55, 90, 0.06);
}

div[data-testid="stMetricLabel"] {
    color: #526581 !important;
}

div[data-testid="stMetricValue"] {
    color: #172B4D !important;
}

div[data-testid="stMetricDelta"] {
    color: #087F9B !important;
}

/* ---------- FILE UPLOADER ---------- */

div[data-testid="stFileUploader"] {
    background: #FFFFFF !important;
    border: 1px dashed #72AFC5 !important;
    border-radius: 14px !important;
    padding: 16px !important;
    box-shadow: 0 4px 12px rgba(30, 55, 90, 0.04);
}

div[data-testid="stFileUploader"] section {
    background: #F1F6FC !important;
    border-radius: 10px !important;
    border: 1px solid #D5E1EF !important;
}

div[data-testid="stFileUploader"] label,
div[data-testid="stFileUploader"] small {
    color: #334967 !important;
}

/* ---------- DATA TABLE ---------- */

div[data-testid="stDataFrame"] {
    border: 1px solid #D5E1EF;
    border-radius: 12px;
    overflow: hidden;
    background: #FFFFFF;
}

/* ---------- EXPANDER ---------- */

div[data-testid="stExpander"] {
    background: #FFFFFF !important;
    border: 1px solid #D5E1EF !important;
    border-radius: 12px !important;
}

/* ---------- DOWNLOAD BUTTONS ---------- */

.stDownloadButton button {
    background: #176B8A !important;
    color: #FFFFFF !important;
    border: 1px solid #176B8A !important;
    border-radius: 9px !important;
    font-weight: 650 !important;
    transition: 0.2s ease;
}

.stDownloadButton button:hover {
    background: #12536F !important;
    border-color: #12536F !important;
    color: #FFFFFF !important;
}

/* ---------- REGULAR BUTTONS ---------- */

.stButton button {
    border-radius: 9px !important;
    font-weight: 600 !important;
}

/* ---------- PROGRESS BAR ---------- */

div[data-testid="stProgressBar"] > div > div {
    background: #159DBB !important;
}

/* ---------- FOOTER ---------- */

.batch-footer {
    color: #71829A;
    text-align: center;
    font-size: 12px;
    padding: 18px 0;
}

/* ===== REQUIRED CSV FORMAT CARD ===== */

.dataset-panel {
    position: relative;
    background: linear-gradient(145deg, #FFFFFF, #F0F7FF);
    border: 1px solid #BBDDF5;
    border-radius: 20px;
    padding: 27px;
    min-height: 250px;
    overflow: hidden;
    box-shadow: 0 10px 28px rgba(30, 65, 105, 0.08);
}

.dataset-panel::before {
    content: "";
    position: absolute;
    width: 150px;
    height: 150px;
    border-radius: 50%;
    background: rgba(55, 174, 230, 0.12);
    top: -75px;
    right: -45px;
}

.dataset-panel h4 {
    color: #172B4D !important;
    font-size: 21px;
    margin: 0 0 12px 0;
    position: relative;
}

.dataset-panel p {
    color: #344D70 !important;
    font-size: 14px;
    line-height: 1.7;
    position: relative;
}

.dataset-panel .panel-icon {
    width: 58px;
    height: 58px;
    border-radius: 17px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #DDF2FF;
    font-size: 27px;
    margin-bottom: 18px;
}

.dataset-panel .column-chip {
    display: inline-block;
    background: #DDF1FF;
    border: 1px solid #B7DFF8;
    color: #145A9C;
    padding: 9px 17px;
    border-radius: 25px;
    margin: 8px 7px 8px 0;
    font-family: monospace;
    font-weight: 700;
    font-size: 14px;
}

/* ===== SAMPLE DATASET CARD ===== */

.sample-panel {
    position: relative;
    background: linear-gradient(135deg, #102C53, #075B85);
    border: 1px solid #159CC7;
    border-radius: 20px;
    padding: 27px;
    min-height: 250px;
    overflow: hidden;
    box-shadow: 0 12px 28px rgba(16, 44, 83, 0.17);
}

.sample-panel::after {
    content: "CSV";
    position: absolute;
    right: 8px;
    bottom: -25px;
    font-size: 85px;
    font-weight: 900;
    color: rgba(255,255,255,0.05);
}

.sample-panel h4 {
    color: #FFFFFF !important;
    font-size: 21px;
    margin: 0 0 12px 0;
    position: relative;
}

.sample-panel p {
    color: #D8EAF7 !important;
    font-size: 14px;
    line-height: 1.7;
    position: relative;
}

.sample-panel .panel-icon {
    width: 58px;
    height: 58px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255,255,255,0.15);
    font-size: 27px;
    margin-bottom: 18px;
}

.sample-panel {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* Download button */
.stDownloadButton button {
    background: linear-gradient(90deg, #65D7F0, #A4EFFF) !important;
    color: #102C53 !important;
    border: none !important;
    border-radius: 25px !important;
    font-weight: 700 !important;
    padding: 11px 20px !important;
    transition: 0.25s ease;
}

.stDownloadButton button:hover {
    background: #FFFFFF !important;
    color: #102C53 !important;
    border: 1px solid #65D7F0 !important;
}


/* ===== CSV UPLOAD SECTION DESIGN ===== */

.upload-section-header {
    background: linear-gradient(110deg, #102C53, #087C9E);
    border: 1px solid #2589AA;
    border-radius: 16px;
    padding: 20px 24px;
    display: flex;
    align-items: center;
    gap: 15px;
    margin: 25px 0 16px 0;
    box-shadow: 0 7px 20px rgba(16, 44, 83, 0.12);
}

.upload-section-icon {
    width: 48px;
    height: 48px;
    min-width: 48px;
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
}

.upload-section-title {
    color: #5DE1F2 !important;
    -webkit-text-fill-color: #5DE1F2 !important;
    font-size: 21px;
    font-weight: 750;
    margin: 0;
}

.upload-section-subtitle {
    color: #D8EAF7 !important;
    font-size: 13px;
    margin-top: 5px;
}

.upload-info {
    background: linear-gradient(120deg, #E4F5FC, #F3FAFF);
    border: 1px solid #B9DFEF;
    border-radius: 12px;
    padding: 13px 17px;
    color: #315873;
    font-size: 13px;
    margin: 12px 0;
}

/* File uploader */
div[data-testid="stFileUploader"] {
    background: linear-gradient(145deg, #F5FBFF, #E5F4FC) !important;
    border: 2px dashed #55B9D5 !important;
    border-radius: 17px !important;
    padding: 22px !important;
    box-shadow: 0 7px 20px rgba(23, 75, 110, 0.07) !important;
    transition: 0.25s ease;
}

div[data-testid="stFileUploader"]:hover {
    border-color: #087C9E !important;
    background: #EAF8FF !important;
}

div[data-testid="stFileUploader"] section {
    background: #FFFFFF !important;
    border: 1px solid #C8E4F2 !important;
    border-radius: 12px !important;
}

div[data-testid="stFileUploader"] button {
    background: #176B8A !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 9px !important;
    font-weight: 650 !important;
}

div[data-testid="stFileUploader"] label {
    color: #173C61 !important;
    font-weight: 650 !important;
}
/* FIX: CSV UPLOAD BROWSE BUTTON COLOR */

div[data-testid="stFileUploader"] button {
    background: linear-gradient(90deg, #087C9E, #176B8A) !important;
    background-color: #087C9E !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    border: 1px solid #087C9E !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    box-shadow: none !important;
}

div[data-testid="stFileUploader"] button:hover {
    background: #102C53 !important;
    background-color: #102C53 !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    border-color: #102C53 !important;
}

div[data-testid="stFileUploader"] button p {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}
span.required-csv-heading {
    color: #5DE1F2 !important;
    -webkit-text-fill-color: #5DE1F2 !important;
    font-size: 21px !important;
    font-weight: 700 !important;
    opacity: 1 !important;
    visibility: visible !important;
    display: inline-block !important;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# NAVIGATION
# =========================================================

if st.button("← Back to Home", key="back_to_home"):
    st.switch_page("app.py")


# =========================================================
# PAGE HEADER
# =========================================================

st.markdown("""
<div class="batch-hero">
<div class="hero-tag">EVALAI · DATASET MANAGEMENT</div>
<h1>📂 CSV Batch Evaluation</h1>
<p>
Validate multiple AI questions and responses in one place.
Prepare clean datasets for reliable AI quality evaluation.
</p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# INTRODUCTION
# =========================================================

st.markdown("### Welcome to Batch Evaluation")

st.write(
    "Upload a CSV dataset containing questions and AI-generated responses. "
    "EvalAI checks the structure, identifies incomplete records, and prepares "
    "valid data for the next evaluation stage."
)

st.info(
    "🧪 **Current mode: CSV Validation** — "
    "This page validates data only. Actual AI evaluation is not connected yet."
)


# =========================================================
# SAMPLE TEMPLATE
# =========================================================

REQUIRED_COLUMNS = ["question", "response"]

st.markdown(
    '<div class="section-title">1. Prepare Your Dataset</div>',
    unsafe_allow_html=True
)

left, right = st.columns([2, 1], gap="large")

sample_data = pd.DataFrame({
    "question": [
        "What is artificial intelligence?",
        "What is machine learning?"
    ],
    "response": [
        "Artificial intelligence enables machines to perform tasks "
        "that usually require human intelligence.",
        "Machine learning is a branch of AI that learns patterns "
        "from data."
    ]
})



with left:
    st.markdown("""
<div style="background:linear-gradient(145deg,#F4FAFF,#E4F3FF);border:1px solid #A9D9F2;border-radius:20px;overflow:hidden;box-shadow:0 10px 25px rgba(23,43,77,0.12);">
<div style="background:linear-gradient(110deg,#102C53,#087C9E);padding:23px 25px;display:flex;align-items:center;gap:15px;">
<div style="background:rgba(255,255,255,0.15);border-radius:14px;padding:12px;font-size:25px;flex-shrink:0;">📄</div>
<span class="required-csv-heading">Required CSV Format</span>
</div>
<div style="padding:25px;">
<p style="color:#405B78 !important;font-size:14px;margin-bottom:18px;">Your dataset must contain the following column names:</p>
<div style="background:#FFFFFF;border:1px solid #C6E4F5;border-radius:12px;padding:13px 16px;margin-bottom:11px;display:flex;align-items:center;gap:14px;">
<span style="background:#D8F0FF;color:#087CA5;padding:7px 10px;border-radius:8px;font-size:12px;font-weight:bold;">01</span>
<span style="color:#17466D;font-family:monospace;font-size:15px;font-weight:bold;">question</span>
<span style="margin-left:auto;color:#159A91;">✓</span>
</div>
<div style="background:#FFFFFF;border:1px solid #C6E4F5;border-radius:12px;padding:13px 16px;display:flex;align-items:center;gap:14px;">
<span style="background:#D8F0FF;color:#087CA5;padding:7px 10px;border-radius:8px;font-size:12px;font-weight:bold;">02</span>
<span style="color:#17466D;font-family:monospace;font-size:15px;font-weight:bold;">response</span>
<span style="margin-left:auto;color:#159A91;">✓</span>
</div>
<div style="background:#D9F0FC;border-left:4px solid #168BB5;border-radius:9px;padding:14px;margin-top:20px;color:#315873;font-size:13px;line-height:1.7;">ℹ️ Each row should contain one question and its corresponding AI response.</div>
</div>
</div>
""", unsafe_allow_html=True)





with right:
    st.markdown("""
<div class="sample-panel">
    <div class="panel-icon">⬇️</div>
    <h4>Sample Dataset</h4>
    <p>
        Download our sample template and use it to prepare
        your dataset.
    </p>
</div>
""", unsafe_allow_html=True)

    st.download_button(
        label="⬇️ Download Sample CSV",
        data=sample_data.to_csv(index=False).encode("utf-8"),
        file_name="batch_evaluation_template.csv",
        mime="text/csv",
        use_container_width=True
    )


# =========================================================
# CSV FILE UPLOAD
# =========================================================

# =========================================================
# CSV FILE UPLOAD
# =========================================================

st.markdown("""
<div class="upload-section-header"><div class="upload-section-icon">📤</div><div><div class="upload-section-title">2. Upload Your CSV</div><div class="upload-section-subtitle">Import your dataset and prepare it for quality validation</div></div></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="upload-info">
📋 <b>Supported format:</b> CSV &nbsp; | &nbsp;
<b>Required columns:</b> question and response
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose a CSV file from your computer",
    type=["csv"],
    help="Upload a CSV containing question and response columns.",
    key="batch_csv_uploader"
)



# =========================================================
# CSV VALIDATION
# =========================================================

if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)

        # Normalize column names
        df.columns = df.columns.str.strip().str.lower()

        missing_columns = [
            col for col in REQUIRED_COLUMNS
            if col not in df.columns
        ]

        if missing_columns:

            st.error(
                "❌ Missing required columns: "
                + ", ".join(missing_columns)
            )

            st.write(
                "Please include both `question` and `response` columns."
            )

        elif df.empty:

            st.warning(
                "⚠️ The uploaded CSV contains no data rows."
            )

        else:

            # Clean required fields
            df["question"] = (
                df["question"].fillna("").astype(str).str.strip()
            )

            df["response"] = (
                df["response"].fillna("").astype(str).str.strip()
            )

            valid_rows = (
                df["question"].ne("")
                & df["response"].ne("")
            )

            valid_df = df.loc[valid_rows].copy()
            invalid_df = df.loc[~valid_rows].copy()

            total_rows = len(df)
            valid_count = len(valid_df)
            invalid_count = len(invalid_df)


            # ---------------------------------------------
            # DATASET OVERVIEW
            # ---------------------------------------------

            st.markdown("---")

            st.markdown(
                '<div class="section-title">3. Dataset Overview</div>',
                unsafe_allow_html=True
            )

            metric1, metric2, metric3 = st.columns(3, gap="medium")

            with metric1:
                st.metric(
                    label="📊 Total Rows",
                    value=total_rows
                )

            with metric2:
                st.metric(
                    label="✅ Valid Rows",
                    value=valid_count
                )

            with metric3:
                st.metric(
                    label="⚠️ Invalid Rows",
                    value=invalid_count
                )


            if invalid_count == 0:

                st.success(
                    "✅ All rows passed the basic validation checks."
                )

            else:

                st.warning(
                    f"{invalid_count} row(s) have an empty question "
                    "or response. These rows are excluded from the valid preview."
                )


            # ---------------------------------------------
            # VALID RECORDS
            # ---------------------------------------------

            st.markdown(
                '<div class="section-title">4. Valid Records</div>',
                unsafe_allow_html=True
            )

            if not valid_df.empty:

                st.caption(
                    "These records contain both a question and a response."
                )

                st.dataframe(
                    valid_df,
                    use_container_width=True,
                    hide_index=True
                )

                st.download_button(
                    label="⬇️ Download Valid Records",
                    data=valid_df.to_csv(index=False).encode("utf-8"),
                    file_name="valid_evaluation_records.csv",
                    mime="text/csv"
                )

            else:

                st.info(
                    "No valid records found. Check that each row has "
                    "both a question and a response."
                )


            # ---------------------------------------------
            # INVALID RECORDS
            # ---------------------------------------------

            if invalid_count > 0:

                with st.expander("🔍 View Invalid Rows"):

                    st.write(
                        "Review these rows and fill in the missing fields "
                        "before using them."
                    )

                    st.dataframe(
                        invalid_df,
                        use_container_width=True,
                        hide_index=True
                    )


            # ---------------------------------------------
            # VALIDATION STATUS
            # ---------------------------------------------

            st.markdown("---")

            st.markdown(
                '<div class="section-title">5. Validation Status</div>',
                unsafe_allow_html=True
            )

            if valid_count > 0:

                st.progress(valid_count / total_rows)

                st.write(
                    f"**{valid_count} of {total_rows} rows** "
                    "passed the basic validation checks."
                )

                st.info(
                    "🚀 Your valid records are ready for the next stage. "
                    "AI scoring, accuracy checks, and hallucination detection "
                    "will be available after backend integration."
                )

    except Exception as e:

        st.error(
            f"Could not read this CSV file: {e}"
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
<div class="batch-footer">
    EvalAI · AI Response Quality Platform<br>
    CSV Batch Validation
</div>
""", unsafe_allow_html=True)
