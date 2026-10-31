import streamlit as st
import pandas as pd

from ui import apply_design, render_sidebar

st.set_page_config(
    page_title="CSV Batch Evaluation",
    page_icon="📂",
    layout="wide"
)
st.button(
    "← Back to Home",
    on_click=lambda: st.switch_page("app.py"),
    key="back_to_home"
)
apply_design()
render_sidebar()

# ---------------- PAGE HEADER ----------------
st.markdown("""
<div style="
    padding: 28px;
    border-radius: 18px;
    background: linear-gradient(120deg, #172554, #4338ca, #6366f1);
    color: white;
    margin-bottom: 25px;
">
    <h1 style="margin: 0; color: white;">
        📂 CSV Batch Evaluation
    </h1>
    <p style="margin-top: 10px; font-size: 16px; color: #e0e7ff;">
        Validate multiple AI questions and responses in one place.
        Prepare your dataset for batch evaluation.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- INTRODUCTION ----------------
st.markdown("### Welcome to Batch Evaluation")
st.write(
    "Upload a CSV file containing questions and AI-generated responses. "
    "The system checks your file structure, identifies incomplete rows, "
    "and prepares valid records for evaluation."
)

st.info(
    "🧪 **Current mode: CSV Validation** — "
    "This page validates data only. Actual AI evaluation is not connected yet."
)

# ---------------- SAMPLE TEMPLATE ----------------
REQUIRED_COLUMNS = ["question", "response"]

st.markdown("### 1. Prepare Your Dataset")

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
    <div style="
        padding: 20px;
        border: 1px solid rgba(128,128,128,0.3);
        border-radius: 14px;
        min-height: 150px;
    ">
        <h4>📄 Required CSV Format</h4>
        <p>Your CSV file must include these two column names:</p>
        <p><code>question</code> &nbsp; and &nbsp; <code>response</code></p>
        <p>Each row should contain one question and its AI response.</p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("#### Need a template?")
    st.write("Download a sample file to get started.")
    st.download_button(
        label="⬇️ Download Sample CSV",
        data=sample_data.to_csv(index=False).encode("utf-8"),
        file_name="batch_evaluation_template.csv",
        mime="text/csv",
        use_container_width=True
    )

# ---------------- FILE UPLOAD ----------------
st.markdown("### 2. Upload Your CSV")

uploaded_file = st.file_uploader(
    "Choose a CSV file from your computer",
    type=["csv"],
    help="Upload a CSV containing question and response columns."
)

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
            st.write("Please include both `question` and `response` columns.")

        elif df.empty:
            st.warning("⚠️ The uploaded CSV contains no data rows.")

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

            # ---------------- SUMMARY ----------------
            st.markdown("---")
            st.markdown("### 3. Dataset Overview")

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

            # ---------------- VALID PREVIEW ----------------
            st.markdown("### 4. Valid Records")

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
                    mime="text/csv",
                    use_container_width=False
                )
            else:
                st.info(
                    "No valid records found. Check that each row has "
                    "both a question and a response."
                )

            # ---------------- INVALID ROWS ----------------
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

            # ---------------- STATUS ----------------
            st.markdown("---")
            st.markdown("### 5. Validation Status")

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
        st.error(f"Could not read this CSV file: {e}")

# ---------------- NAVIGATION ----------------
st.markdown("---")

if st.button("← Back to Home", use_container_width=False):
    st.switch_page("pages/1_Home.py")

st.caption("AI Response Quality Evaluator · CSV Batch Validation")
