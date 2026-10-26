
import streamlit as st

st.set_page_config(
    page_title="Knowledge Base",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Knowledge Base")
st.write("Manage reusable reference documents for AI response evaluation.")

st.info(
    "This is the document library interface. "
    "Permanent storage and document indexing are not connected yet."
)

# Summary cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Documents in Library", "0")

with col2:
    st.metric("Indexed Documents", "0")

with col3:
    st.metric("Pending Processing", "0")

st.divider()

# Document library
st.subheader("📁 Document Library")
st.write(
    "Trusted documents can be stored here for reuse across multiple evaluations."
)

search_text = st.text_input(
    "Search documents",
    placeholder="Search by document name..."
)

category = st.selectbox(
    "Filter by document type",
    ["All Documents", "PDF", "TXT"]
)

if search_text or category != "All Documents":
    st.caption("Search and filtering will work when document storage is connected.")

st.divider()

st.subheader("📋 Saved Documents")

st.write("No saved documents yet.")

st.caption(
    "Once permanent storage is implemented, saved documents will appear here "
    "with their file names, upload dates, and processing status."
)

st.divider()

st.subheader("ℹ️ How the Knowledge Base works")

st.markdown(
    """
    - **Reusable references:** Keep trusted information for future evaluations.
    - **Document processing:** Prepare documents for searching and retrieval.
    - **Evidence retrieval:** Help the evaluation backend find relevant information.
    """
)

if st.button("← Back to Home"):
    st.switch_page("pages/1_Home.py")
