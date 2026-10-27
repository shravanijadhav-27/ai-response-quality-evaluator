
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CSV Batch Evaluation",
    page_icon="📂",
    layout="wide"
)

st.title("📂 CSV Batch Evaluation")
st.write(
    "Upload multiple questions and AI responses for batch evaluation."
)

st.info(
    "Demo mode: This page validates your CSV file. "
    "Actual AI evaluation will be added after backend integration."
)

# Expected CSV columns
REQUIRED_COLUMNS = ["question", "response"]

st.subheader("1. Upload CSV File")

st.write(
    "Your CSV must contain two columns: "
    "`question` and `response`."
)

# Downloadable sample template
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

st.download_button(
    label="📥 Download Sample CSV Template",
    data=sample_data.to_csv(index=False).encode("utf-8"),
    file_name="batch_evaluation_template.csv",
    mime="text/csv"
)

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
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
                "Missing required columns: "
                + ", ".join(missing_columns)
            )
            st.write(
                "Required columns are: question, response."
            )

        elif df.empty:
            st.warning("The uploaded CSV contains no rows.")

        else:
            # Check for empty questions or responses
            df["question"] = df["question"].fillna("").astype(str).str.strip()
            df["response"] = df["response"].fillna("").astype(str).str.strip()

            valid_rows = (
                df["question"].ne("")
                & df["response"].ne("")
            )

            valid_df = df.loc[valid_rows].copy()
            invalid_count = int((~valid_rows).sum())

            st.subheader("2. Upload Summary")

            col1, col2, col3 = st.columns(3)
            col1.metric("Total Rows", len(df))
            col2.metric("Valid Rows", len(valid_df))
            col3.metric("Invalid Rows", invalid_count)

            if invalid_count:
                st.warning(
                    f"{invalid_count} row(s) have an empty question "
                    "or response and will be excluded from the valid preview."
                )

            st.subheader("3. Preview Valid Evaluations")

            st.dataframe(
                valid_df,
                use_container_width=True,
                hide_index=True
            )

            if not valid_df.empty:
                st.success(
                    f"{len(valid_df)} row(s) are ready for evaluation."
                )

                st.caption(
                    "This is validation only. No AI responses have "
                    "been evaluated yet."
                )

    except Exception as e:
        st.error(f"Could not read this CSV file: {e}")

if st.button("← Back to Home"):
    st.switch_page("pages/1_Home.py")
