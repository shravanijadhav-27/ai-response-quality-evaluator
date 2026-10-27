import streamlit as st
import os
import re
import uuid
BUCKET_NAME = "knowledge-documents"
from datetime import datetime, timezone

import streamlit as st

try:
    from supabase import create_client
except ImportError:
    create_client = None


st.set_page_config(
    page_title="Knowledge Base | AI Response Quality Evaluator",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)
from ui import apply_design, render_sidebar

apply_design()
render_sidebar()
BUCKET_NAME = "knowledge-documents"
MAX_FILE_SIZE_MB = 10

# ---------- Styling ----------
st.markdown(
    """
    <style>
    .kb-hero {
        padding: 1.6rem 1.8rem;
        border-radius: 18px;
        background: linear-gradient(115deg, #10264b 0%, #2459a9 100%);
        color: white; margin: .3rem 0 1.2rem 0;
    }
    .kb-hero h1 { color: white; margin: 0 0 .4rem 0; font-size: 2rem; }
    .kb-hero p { color: #dce8ff; margin: 0; font-size: 1rem; }
    .kb-section-note { color: #64748b; margin-top: -.35rem; }
    .kb-card {
        border: 1px solid #dbe5f3;
        background: #ffffff;
        border-radius: 14px;
        padding: 1rem 1.1rem;
        min-height: 105px;
        box-shadow: 0 4px 14px rgba(15, 35, 75, .04);
    }
    .kb-card-label { color: #64748b; font-size: .85rem; margin-bottom: .45rem; }
    .kb-card-value { color: #10264b; font-size: 1.75rem; font-weight: 750; }
    .kb-doc {
        border: 1px solid #dbe5f3;
        border-radius: 13px;
        padding: .9rem 1rem;
        background: #fff;
        margin-bottom: .55rem;
    }
    div.stButton > button, div.stDownloadButton > button,
    div[data-testid="stFormSubmitButton"] > button {
        border-radius: 9px;
        font-weight: 650;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- Supabase configuration ----------
def get_secret(name: str, default: str = "") -> str:
    """Read a value from Streamlit secrets first, then environment variables."""
    try:
        value = st.secrets.get(name, default)
    except Exception:
        value = default
    return str(value or os.getenv(name, default)).strip()


def get_supabase_client():
    url = get_secret("SUPABASE_URL")
    key = get_secret("SUPABASE_SERVICE_ROLE_KEY") or get_secret("SUPABASE_KEY")
    if not url or not key:
        return None, "Supabase credentials are not configured yet."
    if create_client is None:
        return (
            None,
            "The `supabase` package is missing. Add `supabase` to requirements.txt and redeploy.",
        )
    try:
        return create_client(url, key), None
    except Exception as exc:
        return None, f"Could not connect to Supabase: {exc}"


client, connection_error = get_supabase_client()


# ---------- Header ----------
st.markdown(
    """
    <div class="kb-hero">
        <h1>📚 Knowledge Base</h1>
        <p>Store trusted reference documents and reuse them across AI response evaluations.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("Shared document library · PDF and TXT files · Private Supabase Storage")

if st.session_state.pop("kb_flash", None):
    st.success("Document saved to the shared Knowledge Base.")

if connection_error:
    st.warning(
        "Online storage is not connected yet. The page will still open, but saving and listing shared documents require Supabase credentials."
    )


# ---------- Load stored documents ----------
def list_documents():
    if client is None:
        return [], None
    try:
        response = client.storage.from_(BUCKET_NAME).list(
            "",
            {"limit": 100, "offset": 0, "sortBy": {"column": "name", "order": "asc"}},
        )
        docs = []
        for item in response or []:
            name = item.get("name", "") if isinstance(item, dict) else ""
            # Ignore folder placeholders and only show supported document types.
            if not name or name.startswith("."):
                continue
            ext = os.path.splitext(name)[1].lower()
            if ext not in {".pdf", ".txt"}:
                continue
            docs.append(item)
        docs.sort(
            key=lambda x: x.get("created_at") or x.get("updated_at") or "", reverse=True
        )
        return docs, None
    except Exception as exc:
        return [], str(exc)


documents, list_error = list_documents()

if list_error:
    st.error("Supabase Storage error")
    st.code(str(list_error))

# ---------- Summary cards ----------
indexed_count = 0  # Text extraction / indexing is not implemented on this page yet.
pending_count = 0
summary_cols = st.columns(3)
summary_values = [
    ("📄", "Documents in Library", str(len(documents))),
    ("🔎", "Indexed Documents", str(indexed_count)),
    ("⏳", "Pending Processing", str(pending_count)),
]
for col, (icon, label, value) in zip(summary_cols, summary_values):
    with col:
        st.markdown(
            f'<div class="kb-card"><div class="kb-card-label">{icon} &nbsp; {label}</div>'
            f'<div class="kb-card-value">{value}</div></div>',
            unsafe_allow_html=True,
        )
    
st.write("")

# ---------- Upload / Save ----------
left, right = st.columns([1.08, 0.92], gap="large")
with left:
    st.subheader("⬆️ Add a reference document")
    st.markdown(
        '<p class="kb-section-note">Upload a PDF or text file to make it available in the shared library.</p>',
        unsafe_allow_html=True,
    )
    uploaded_file = st.file_uploader(
        "Choose a document",
        type=["pdf", "txt"],
        help=f"Maximum file size: {MAX_FILE_SIZE_MB} MB. Only PDF and TXT files are accepted.",
        key="kb_upload_file",
    )
    if st.button(
        "💾 Save to Knowledge Base",
        type="primary",
        use_container_width=True,
        key="kb_save_button",
    ):
        if uploaded_file is None:
            st.error("Please choose a PDF or TXT file first.")
        elif uploaded_file.size > MAX_FILE_SIZE_MB * 1024 * 1024:
            st.error(
                f"This file is larger than {MAX_FILE_SIZE_MB} MB. Please choose a smaller file."
            )
        elif client is None:
            st.error(
                "Save is not available because Supabase is not configured. Follow the setup instructions below first."
            )
        else:
            original_name = os.path.basename(uploaded_file.name)
            safe_name = (
                re.sub(r"[^A-Za-z0-9._-]+", "_", original_name).strip("._")
                or "document"
            )
            object_path = f"{uuid.uuid4().hex}_{safe_name}"
            mime_type = (
                "application/pdf"
                if safe_name.lower().endswith(".pdf")
                else "text/plain"
            )
            try:
                file_bytes = uploaded_file.getvalue()
                upload_result = client.storage.from_(BUCKET_NAME).upload(
                    object_path,
                    file_bytes,
                    file_options={"content-type": mime_type, "upsert": "false"},
                )
                st.session_state["kb_flash"] = True
                st.rerun()
            except Exception as exc:
                st.error(f"Could not save the document: {exc}")

with right:
    st.subheader("🔐 Storage status")
    if client is not None and not list_error:
        st.success("Supabase connection configured")
        st.write(f"**Bucket:** `{BUCKET_NAME}`")
        st.write("**Access:** Private bucket")
        st.write("**Allowed files:** PDF, TXT")
        st.write(f"**Upload limit on this page:** {MAX_FILE_SIZE_MB} MB per file")
    else:
        st.info("Connect Supabase to enable shared uploads and document listing.")
    st.markdown("""
        **What happens when you save?**

        1. The file is uploaded to Supabase Storage.
        2. The library refreshes from the cloud bucket.
        3. Other people using this deployed app can see the uploaded file list.

        *Document text extraction and indexing are not implemented here yet.*
        """)

st.divider()

# ---------- Browse / Search saved documents ----------
st.subheader("📂 Saved Documents")
st.markdown(
    '<p class="kb-section-note">Search and download documents already stored in the shared bucket.</p>',
    unsafe_allow_html=True,
)
filter_cols = st.columns([1.5, 0.75, 0.75])
with filter_cols[0]:
    search_text = st.text_input(
        "Search by file name",
        placeholder="Type part of a document name...",
        key="kb_search",
    )
with filter_cols[1]:
    type_filter = st.selectbox("File type", ["All", "PDF", "TXT"], key="kb_type_filter")
with filter_cols[2]:
    st.write("")
    st.write("")
    if st.button("↻ Refresh library", use_container_width=True, key="kb_refresh"):
        st.rerun()

filtered_documents = []
for doc in documents:
    name = doc.get("name", "")
    ext = os.path.splitext(name)[1].lower()
    if search_text and search_text.casefold() not in name.casefold():
        continue
    if type_filter == "PDF" and ext != ".pdf":
        continue
    if type_filter == "TXT" and ext != ".txt":
        continue
    filtered_documents.append(doc)

if not documents and not list_error:
    st.info(
        "No saved documents yet. Upload a PDF or TXT file above and click **Save to Knowledge Base**."
    )
elif filtered_documents:
    for index, doc in enumerate(filtered_documents):
        stored_name = doc.get("name", "document")
        # Object path is randomized at upload; display the original-looking part after the first underscore.
        display_name = (
            stored_name.split("_", 1)[1] if "_" in stored_name else stored_name
        )
        metadata = doc.get("metadata") or {}
        size_bytes = metadata.get("size") or metadata.get("contentLength")
        if not isinstance(size_bytes, (int, float)):
            size_label = "Size not provided"
        else:
            size_label = (
                f"{size_bytes / 1024:.1f} KB"
                if size_bytes < 1024 * 1024
                else f"{size_bytes / (1024 * 1024):.2f} MB"
            )
        ext_label = (
            "PDF document" if stored_name.lower().endswith(".pdf") else "Text document"
        )
        with st.container(border=True):
            name_col, info_col, action_col = st.columns(
                [2.2, 1.2, 0.9], vertical_alignment="center"
            )
            with name_col:
                st.markdown(
                    f"**{'📕' if stored_name.lower().endswith('.pdf') else '📄'} {display_name}**"
                )
                st.caption(f"{ext_label} · {size_label}")
            with info_col:
                created = doc.get("created_at") or doc.get("updated_at")
                st.caption(
                    f"Uploaded: {created[:10] if isinstance(created, str) and len(created) >= 10 else 'Date unavailable'}"
                )
            with action_col:
                if st.button(
                    "⬇️ Download", key=f"kb_download_{index}", use_container_width=True
                ):
                    if client is None:
                        st.error("Supabase is not configured.")
                    else:
                        try:
                            content = client.storage.from_(BUCKET_NAME).download(
                                stored_name
                            )
                            mime_type = (
                                "application/pdf"
                                if stored_name.lower().endswith(".pdf")
                                else "text/plain"
                            )
                            st.download_button(
                                "Save file",
                                data=content,
                                file_name=display_name,
                                mime=mime_type,
                                key=f"kb_download_file_{index}",
                                use_container_width=True,
                            )
                        except Exception as exc:
                            st.error(f"Download failed: {exc}")
                if st.button(
                    "🗑️ Delete",
                    key=f"kb_delete_{index}",
                    use_container_width=True,
                ):
                    st.session_state["kb_confirm_delete"] = stored_name

            if st.session_state.get("kb_confirm_delete") == stored_name:
                st.warning(f"Are you sure you want to delete {display_name}?")

                confirm_col, cancel_col = st.columns(2)

                with confirm_col:
                    if st.button(
                        "Yes, delete",
                        key=f"kb_confirm_yes_{index}",
                        type="primary",
                    ):
                        try:
                            client.storage.from_(BUCKET_NAME).remove([stored_name])
                            st.session_state.pop("kb_confirm_delete", None)
                            st.success("Document deleted successfully.")
                            st.rerun()
                        except Exception as exc:
                            st.error(f"Delete failed: {exc}")

                with cancel_col:
                    if st.button("Cancel", key=f"kb_confirm_cancel_{index}"):
                        st.session_state.pop("kb_confirm_delete", None)
                        st.rerun()
elif not list_error:
    st.info("No documents match your search and filter.")              
st.divider()
with st.expander("ℹ️ How the Knowledge Base works"):
    st.markdown("""
        - **Reusable references:** Save trusted PDFs and text files for future evaluations.
        - **Shared storage:** The files live in the Supabase bucket, not only on this laptop.
        - **Processing and indexing:** Not implemented yet; files are stored and listed, but are not yet parsed for retrieval by an evaluation agent.
        """)

if st.button("← Back to Home", key="kb_back_home"):
    st.switch_page("pages/1_Home.py")

st.caption("AI Response Quality Evaluator · Knowledge Base")
