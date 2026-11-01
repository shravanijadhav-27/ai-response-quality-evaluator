import os
import html
from io import BytesIO
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st
from pymongo import MongoClient
from gridfs import GridFSBucket

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Knowledge Base | EvalAI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep the existing shared navigation. The sidebar itself is intentionally
# not redesigned in this file; we can update ui.py later.
from ui import apply_design, render_sidebar

apply_design()
render_sidebar()

# =========================================================
# CONFIGURATION
# =========================================================
DATABASE_NAME = "evalai"
BUCKET_NAME = "knowledge_documents"
MAX_FILE_SIZE_MB = 10
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024
PAGE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PAGE_DIR.parent
HERO_IMAGE = PROJECT_DIR / "assets" / "Neon AI Knowledge Hub.png"


def render_html(content: str) -> None:
    """Render trusted, locally-authored HTML snippets."""
    st.html(content)


# =========================================================
# AURORA PAGE DESIGN (sidebar intentionally untouched)
# =========================================================
render_html("""
<style>
:root {
  --kb-ink: #17234b;
  --kb-muted: #69769b;
  --kb-line: #e2e7fb;
  --kb-cyan: #22d3ee;
  --kb-violet: #8b5cf6;
}
.stApp {
  background:
    radial-gradient(ellipse at 82% 0%, rgba(139,92,246,.11), transparent 28%),
    radial-gradient(ellipse at 5% 22%, rgba(34,211,238,.08), transparent 25%),
    #f6f7ff;
}
.block-container {max-width: 1460px; padding-top: 1.25rem; padding-bottom: 2.2rem;}

/* HERO */
.kb-hero {
  min-height: 300px; overflow: hidden; position: relative;
  padding: 30px 30px 26px; border-radius: 23px;
  background: radial-gradient(circle at 90% 12%, rgba(139,92,246,.36), transparent 28%),
              radial-gradient(circle at 12% 100%, rgba(34,211,238,.17), transparent 32%),
              linear-gradient(115deg,#09163d 0%,#102b68 55%,#33217b 100%);
  border: 1px solid rgba(132,153,255,.28);
  box-shadow: 0 18px 42px rgba(26,36,100,.17);
  color: white;
}
.kb-eyebrow {display:inline-flex;align-items:center;gap:7px;padding:7px 11px;border-radius:30px;
  background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.2);
  color:#b8f4ff;font-size:10px;font-weight:850;letter-spacing:1.5px;}
.kb-hero h1 {color:#fff!important;font-size:clamp(29px,3.5vw,43px);font-weight:850;line-height:1.12;margin:17px 0 12px;}
.kb-hero p {color:#dce7ff!important;font-size:14px;line-height:1.75;max-width:590px;margin:0;}
.kb-hero-tags {display:flex;flex-wrap:wrap;gap:8px;margin-top:19px;}
.kb-hero-tag {display:inline-flex;padding:7px 10px;border-radius:9px;background:rgba(255,255,255,.10);
  border:1px solid rgba(255,255,255,.15);color:#f0f4ff;font-size:10px;font-weight:700;}
.kb-hero-image {width:100%;height:100%;min-height:245px;object-fit:cover;border-radius:17px;
  border:1px solid rgba(159,185,255,.24);box-shadow:0 12px 30px rgba(0,0,0,.2);}

/* SECTION HEADINGS */
.kb-section-title {color:var(--kb-ink);font-size:21px;font-weight:850;margin:23px 0 4px;}
.kb-section-subtitle {color:var(--kb-muted);font-size:12px;line-height:1.65;margin:0 0 14px;}

/* UPLOAD PANEL */
.kb-upload-panel {padding:21px 23px;border-radius:17px;color:white;
  background:radial-gradient(circle at 95% 0%,rgba(34,211,238,.22),transparent 32%),
             linear-gradient(115deg,#10245a,#263b91 60%,#5433a4);
  border:1px solid rgba(119,146,255,.42);box-shadow:0 10px 26px rgba(40,54,130,.13);margin:0 0 11px;}
.kb-upload-kicker {color:#8df0ff;font-size:10px;font-weight:850;letter-spacing:1.6px;margin-bottom:7px;}
.kb-upload-title {color:#fff;font-size:20px;font-weight:850;margin-bottom:5px;}
.kb-upload-copy {color:#dce6ff;font-size:12px;line-height:1.65;}
.kb-upload-tags {display:flex;flex-wrap:wrap;gap:7px;margin-top:12px;}
.kb-upload-tag {padding:5px 9px;border-radius:30px;background:rgba(255,255,255,.11);border:1px solid rgba(255,255,255,.18);color:#f2f5ff;font-size:9px;font-weight:800;letter-spacing:.5px;}

/* FILE UPLOADER + INPUTS */
div[data-testid="stFileUploader"] {background:#f0f3ff;border:1px dashed #9aa9e8;border-radius:13px;padding:10px;margin-top:7px;}
div[data-testid="stFileUploader"] section {background:#e8edff;border-radius:9px;}
div[data-testid="stTextInput"] label,div[data-testid="stSelectbox"] label {color:#344276!important;font-size:12px!important;font-weight:750!important;}
div[data-testid="stTextInput"] input,div[data-testid="stSelectbox"] div[data-baseweb="select"]>div {background:#fff!important;border:1px solid #dce2fa!important;border-radius:10px!important;}
div[data-testid="stTextInput"] input:focus {border-color:#7c72e8!important;box-shadow:0 0 0 2px rgba(124,114,232,.12)!important;}

/* BUTTONS */
div.stButton>button,div.stDownloadButton>button {border-radius:10px!important;font-size:12px!important;font-weight:750!important;min-height:39px;}
div[data-testid="st-key-kb_save_button"] button {background:linear-gradient(95deg,#5267e8,#7654dc)!important;color:white!important;border:0!important;box-shadow:0 6px 15px rgba(87,91,210,.2);}
div[data-testid="st-key-kb_save_button"] button:hover {background:linear-gradient(95deg,#4055d2,#6440c5)!important;color:white!important;}

/* LIBRARY SUMMARY */
.kb-library-panel {position:relative;overflow:hidden;padding:23px 25px 19px;border-radius:20px;color:white;
  background:radial-gradient(circle at 92% 0%,rgba(34,211,238,.20),transparent 25%),
             radial-gradient(circle at 3% 100%,rgba(139,92,246,.24),transparent 30%),
             linear-gradient(115deg,#0b1b49,#172e70 58%,#3d267e);
  border:1px solid rgba(125,151,255,.3);box-shadow:0 13px 30px rgba(24,37,100,.15);margin:25px 0 14px;}
.kb-library-kicker {color:#9cefff;font-size:10px;font-weight:850;letter-spacing:1.7px;margin-bottom:7px;}
.kb-library-title {color:#fff!important;font-size:clamp(23px,2.7vw,31px);font-weight:850;line-height:1.2;margin:0 0 6px;}
.kb-library-subtitle {color:#d9e4ff!important;font-size:12px;line-height:1.65;margin:0;max-width:690px;}
.kb-library-stats {display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:19px;}
.kb-library-stat {display:flex;align-items:center;gap:10px;min-width:0;padding:11px 12px;border-radius:12px;background:rgba(255,255,255,.09);border:1px solid rgba(222,230,255,.14);}
.kb-stat-icon {display:flex;align-items:center;justify-content:center;flex:0 0 34px;width:34px;height:34px;border-radius:10px;background:rgba(107,224,255,.15);color:#9cefff;font-size:17px;}
.kb-stat-value {color:#fff;font-size:19px;font-weight:850;line-height:1.2;overflow-wrap:anywhere;}
.kb-stat-label {color:#cbd8ff;font-size:10px;font-weight:650;margin-top:3px;}
.kb-library-meta {display:inline-flex;gap:8px;align-items:center;margin-top:13px;padding:6px 10px;border-radius:30px;background:rgba(255,255,255,.08);border:1px solid rgba(222,230,255,.17);color:#e8edff;font-size:9px;font-weight:800;letter-spacing:.5px;}

/* DOCUMENT CARDS */
.kb-document-card {background:linear-gradient(115deg,#fff 0%,#f8f9ff 100%);border:1px solid #e0e5fa;border-radius:14px;padding:14px 15px;margin:13px 0 6px;box-shadow:0 4px 15px rgba(36,47,105,.045);}
.kb-document-row {display:flex;align-items:center;gap:12px;}
.kb-file-icon {display:flex;align-items:center;justify-content:center;width:42px;height:42px;min-width:42px;border-radius:12px;font-size:20px;flex-shrink:0;}
.kb-file-info {flex:1;min-width:0;}
.kb-file-name {color:#1d2c5a;font-size:13px;font-weight:800;line-height:1.45;overflow-wrap:anywhere;}
.kb-file-detail {color:#7b86a7;font-size:10px;line-height:1.55;margin-top:4px;}
.kb-status {display:inline-block;padding:5px 8px;border-radius:30px;background:#fff5e5;color:#94631b;border:1px solid #f1dfb9;font-size:9px;font-weight:800;white-space:nowrap;}
div[class*="st-key-kb_download_"] button {background:#e9edff!important;color:#394da9!important;border:1px solid #d4dcff!important;}
div[class*="st-key-kb_download_"] button:hover {background:#dce3ff!important;}
div[class*="st-key-kb_delete_"] button {background:#fff0ef!important;color:#a94c52!important;border:1px solid #f2d5d5!important;}
div[class*="st-key-kb_delete_"] button:hover {background:#ffe3e2!important;}
div[class*="st-key-kb_refresh"] button {background:#e9edff!important;color:#394da9!important;border:1px solid #d4dcff!important;}

/* EMPTY STATE + FOOTER */
.kb-empty {text-align:center;padding:32px 16px;margin:14px 0;border:1px dashed #b7c2ef;border-radius:16px;background:radial-gradient(circle at 50% 0%,rgba(139,92,246,.08),transparent 55%),#fafaff;}
.kb-empty-icon {width:58px;height:58px;display:flex;align-items:center;justify-content:center;margin:0 auto 11px;border-radius:17px;background:#eceeff;color:#6558c9;font-size:27px;}
.kb-empty-title {color:#202f61;font-size:16px;font-weight:850;margin-bottom:6px;}
.kb-empty-text {color:#7883a4;font-size:11px;line-height:1.65;max-width:490px;margin:0 auto;}
div[data-testid="stExpander"] {border:1px solid #e0e5fa!important;border-radius:13px!important;background:#fafaff!important;overflow:hidden;}
div[data-testid="stExpander"] summary {color:#344276!important;font-weight:750!important;}
.kb-footer {display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px;padding:14px 2px 4px;margin-top:20px;border-top:1px solid #e0e5f5;color:#7883a4;font-size:10px;}

@media(max-width:768px) {
  .block-container {padding: .7rem .7rem 1.5rem;}
  .kb-hero {padding:21px 17px;border-radius:16px;}
  .kb-hero h1 {font-size:28px;}
  .kb-hero p {font-size:12px;}
  .kb-hero-image {min-height:180px;max-height:220px;}
  .kb-section-title {font-size:18px;margin-top:18px;}
  .kb-upload-panel {padding:17px;border-radius:14px;}
  .kb-library-panel {padding:18px 16px 15px;border-radius:16px;}
  .kb-library-stats {gap:6px;margin-top:14px;}
  .kb-library-stat {padding:8px 7px;gap:6px;}
  .kb-stat-icon {width:27px;height:27px;flex-basis:27px;font-size:13px;}
  .kb-stat-value {font-size:15px;}
  .kb-stat-label {font-size:9px;line-height:1.3;}
  .kb-document-card {padding:11px;}
  .kb-file-icon {width:35px;height:35px;min-width:35px;font-size:17px;}
  .kb-file-name {font-size:12px;}
  .kb-status {font-size:8px;padding:4px 6px;white-space:normal;text-align:center;}
}
@media(max-width:420px) {
  .kb-library-stat {display:block;}
  .kb-stat-icon {margin-bottom:6px;}
  .kb-stat-value {font-size:14px;}
}

.kb-hero-single {
    position: relative;
    width: 100%;
    min-height: 340px;
    overflow: hidden;
    display: flex;
    align-items: center;
    padding: 38px 42px;
    box-sizing: border-box;
    border-radius: 24px;

    background:
        radial-gradient(
            ellipse at 82% 50%,
            rgba(30, 115, 190, 0.20),
            transparent 48%
        ),
        linear-gradient(
            115deg,
            #071629 0%,
            #0B1D35 55%,
            #102744 100%
        );

    border: 1px solid rgba(100, 180, 255, 0.15);
}

.kb-hero-content {
    position: relative;
    z-index: 2;
    width: 65%;
}

.kb-hero-single h1 {
    color: #ffffff;
    font-size: clamp(30px, 3.5vw, 43px);
    font-weight: 850;
    line-height: 1.15;
    margin: 18px 0;
}

.kb-hero-single h1 span {
    color: #70D9FF;
}

.kb-hero-single p {
    color: #C1D2E6;
    font-size: 14px;
    line-height: 1.8;
    max-width: 510px;
}

.kb-hero-art {
    position: absolute;
    right: 0;
    top: 0;
    width: 48%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1;
    pointer-events: none;

    background: transparent;

    -webkit-mask-image: linear-gradient(
        to right,
        transparent 0%,
        black 25%,
        black 85%,
        transparent 100%
    );

    mask-image: linear-gradient(
        to right,
        transparent 0%,
        black 25%,
        black 85%,
        transparent 100%
    );
}

.kb-hero-art img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    opacity: 0.62;
    mix-blend-mode: screen;

    filter: drop-shadow(
        0 0 25px rgba(40, 170, 255, 0.22)
    );
}

@media (max-width: 700px) {
    .kb-hero-single {
        min-height: 480px;
        padding: 25px;
        align-items: flex-start;
    }

    .kb-hero-content {
        width: 100%;
    }

    .kb-hero-art {
        top: auto;
        bottom: 0;
        width: 75%;
        height: 48%;
        opacity: 0.55;
    }
}

</style>
""")

# =========================================================

# =========================================================

# =========================================================
# SINGLE AURORA HERO BANNER
# =========================================================

import base64

if HERO_IMAGE.exists():
    with open(HERO_IMAGE, "rb") as image_file:
        hero_image_base64 = base64.b64encode(
            image_file.read()
        ).decode("utf-8")

    hero_image_html = f"""
        <div class="kb-hero-art">
            <img src="data:image/png;base64,{hero_image_base64}">
        </div>
    """
else:
    hero_image_html = """
        <div class="kb-hero-art">
            <div style="font-size:100px;opacity:0.35;">🧠</div>
        </div>
    """

render_html(f"""
<div class="kb-hero-single">

    <div class="kb-hero-content">

        <div class="kb-eyebrow">
            ✦ EVALAI KNOWLEDGE MANAGEMENT
        </div>

        <h1>
            Your AI knowledge.<br>
            <span>One trusted space.</span>
        </h1>

        <p>
            Build a shared library of trusted reference documents
            for your AI response evaluations. Keep important
            knowledge organized, searchable and ready to use.
        </p>

        <div class="kb-hero-tags">
            <span class="kb-hero-tag">✧ Shared document library</span>
            <span class="kb-hero-tag">PDF &amp; TXT support</span>
            <span class="kb-hero-tag">Up to 10 MB per file</span>
        </div>

    </div>

    {hero_image_html}

</div>
""")

# =========================================================
# FLASH MESSAGE
# =========================================================
if st.session_state.pop("kb_flash", False):
    st.success("Your document has been added to the shared Knowledge Base.")

# =========================================================
# MONGODB CONNECTION
# =========================================================
@st.cache_resource(show_spinner=False)
def get_mongodb_connection():
    try:
        mongodb_uri = st.secrets["MONGODB_URI"]
        database_name = st.secrets.get("MONGODB_DATABASE", DATABASE_NAME)
        client = MongoClient(mongodb_uri, serverSelectionTimeoutMS=10000)
        client.admin.command("ping")
        database = client[database_name]
        bucket = GridFSBucket(database, bucket_name=BUCKET_NAME)
        return client, database, bucket, None
    except Exception as exc:
             print("MONGODB CONNECTION ERROR:", repr(exc))
             return None, None, None, str(exc)

mongo_client, database, fs, connection_error = get_mongodb_connection()

if connection_error:
    st.error("We couldn't connect to your shared document library.")
    st.info("Check that MONGODB_URI and, if used, MONGODB_DATABASE are correctly configured in Streamlit Secrets.")
    with st.expander("View technical connection details"):
        st.code(connection_error)
    st.stop()

# =========================================================
# LOAD DOCUMENTS
# =========================================================
def list_documents():
    try:
        docs = list(fs.find({}).sort("uploadDate", -1))
        docs = [doc for doc in docs if str(doc.filename).lower().endswith((".pdf", ".txt"))]
        return docs, None
    except Exception as exc:
        return [], str(exc)

documents, list_error = list_documents()
if list_error:
    st.error("We couldn't load the document list. Use Refresh to try again.")
    with st.expander("View technical details"):
        st.code(list_error)

# =========================================================
# UPLOAD SECTION
# =========================================================
render_html("""
<div class="kb-section-title">Add to your knowledge library</div>
<div class="kb-section-subtitle">Upload trusted reference material so your team can keep useful source documents together.</div>
<div class="kb-upload-panel">
  <div class="kb-upload-kicker">✦ ADD A REFERENCE FILE</div>
  <div class="kb-upload-title">Bring your knowledge into EvalAI.</div>
  <div class="kb-upload-copy">Choose a PDF or plain-text file. Once saved, it will appear in the shared library below and can be downloaded by users with access to this app.</div>
  <div class="kb-upload-tags"><span class="kb-upload-tag">PDF DOCUMENTS</span><span class="kb-upload-tag">TXT FILES</span><span class="kb-upload-tag">MAXIMUM 10 MB</span></div>
</div>
""")

uploaded_file = st.file_uploader(
    "Choose a PDF or TXT document",
    type=["pdf", "txt"],
    help=f"Maximum file size: {MAX_FILE_SIZE_MB} MB.",
    key="kb_upload_file",
)

if st.button("☁️  Save to Knowledge Base", type="primary", use_container_width=True, key="kb_save_button"):
    if uploaded_file is None:
        st.error("Choose a PDF or TXT file before saving.")
    elif uploaded_file.size > MAX_FILE_SIZE_BYTES:
        st.error(f"This file is larger than the {MAX_FILE_SIZE_MB} MB limit.")
    else:
        try:
            original_name = os.path.basename(uploaded_file.name)
            extension = os.path.splitext(original_name)[1].lower()
            if extension not in (".pdf", ".txt"):
                st.error("Only PDF and TXT documents are supported.")
            else:
                content_type = "application/pdf" if extension == ".pdf" else "text/plain"
                file_bytes = uploaded_file.getvalue()
                metadata = {
                    "original_name": original_name,
                    "content_type": content_type,
                    "uploaded_at": datetime.now(timezone.utc).isoformat(),
                    "processing_status": "Not indexed",
                }
                fs.upload_from_stream(original_name, BytesIO(file_bytes), metadata=metadata)
                st.session_state["kb_flash"] = True
                st.rerun()
        except Exception as exc:
            st.error("The document could not be saved. Please try again.")
            with st.expander("View technical details"):
                st.code(str(exc))

# =========================================================
# SUMMARY CALCULATIONS
# =========================================================
total_documents = len(documents)
total_storage = sum(doc.length for doc in documents)
if total_storage < 1024 * 1024:
    storage_label = f"{total_storage / 1024:.1f} KB" if total_storage else "0 KB"
else:
    storage_label = f"{total_storage / (1024 * 1024):.2f} MB"

# =========================================================
# DOCUMENT LIBRARY HEADER
# =========================================================
render_html(f"""
<div class="kb-library-panel">
  <div class="kb-library-kicker">YOUR SHARED KNOWLEDGE SPACE</div>
  <div class="kb-library-title">The document library</div>
  <p class="kb-library-subtitle">Everything your team has added, organized in one place. Search by filename, filter by format, download a source file or remove an outdated document.</p>
  <div class="kb-library-stats">
    <div class="kb-library-stat"><div class="kb-stat-icon">▤</div><div><div class="kb-stat-value">{total_documents}</div><div class="kb-stat-label">Saved documents</div></div></div>
    <div class="kb-library-stat"><div class="kb-stat-icon">✧</div><div><div class="kb-stat-value">—</div><div class="kb-stat-label">Indexed documents</div></div></div>
    <div class="kb-library-stat"><div class="kb-stat-icon">▣</div><div><div class="kb-stat-value">{html.escape(storage_label)}</div><div class="kb-stat-label">Storage used</div></div></div>
  </div>
  <div class="kb-library-meta">PDF &amp; TXT FILES <span>•</span> SHARED LIBRARY</div>
</div>
""")

# =========================================================
# SEARCH + FILTER + REFRESH
# =========================================================
search_col, type_col, refresh_col = st.columns([1.5, 0.8, 0.7], vertical_alignment="bottom")
with search_col:
    search_text = st.text_input("Search documents", placeholder="Type a filename...", key="kb_search")
with type_col:
    type_filter = st.selectbox("File format", ["All files", "PDF", "TXT"], key="kb_type_filter")
with refresh_col:
    if st.button("↻ Refresh", use_container_width=True, key="kb_refresh"):
        st.rerun()

filtered_documents = []
for doc in documents:
    stored_name = str(doc.filename)
    extension = os.path.splitext(stored_name)[1].lower()
    if search_text and search_text.casefold() not in stored_name.casefold():
        continue
    if type_filter == "PDF" and extension != ".pdf":
        continue
    if type_filter == "TXT" and extension != ".txt":
        continue
    filtered_documents.append(doc)

# =========================================================
# DOCUMENT CARDS + DOWNLOAD + DELETE
# =========================================================
if list_error:
    st.caption("The library could not be displayed because the document list failed to load.")
elif not documents:
    render_html("""
    <div class="kb-empty"><div class="kb-empty-icon">📚</div><div class="kb-empty-title">Your library is ready for its first document</div><div class="kb-empty-text">There are no saved documents yet. Upload a PDF or TXT reference file above to start building your shared knowledge space.</div></div>
    """)
elif filtered_documents:
    st.caption(f"Showing {len(filtered_documents)} of {len(documents)} saved documents")
    for doc in filtered_documents:
        stored_name = str(doc.filename)
        metadata = doc.metadata or {}
        display_name = str(metadata.get("original_name", stored_name))
        extension = os.path.splitext(stored_name)[1].lower()
        file_size = int(doc.length)
        size_label = f"{file_size / 1024:.1f} KB" if file_size < 1024 * 1024 else f"{file_size / (1024 * 1024):.2f} MB"
        if extension == ".pdf":
            file_icon, icon_background, format_label = "📕", "#fff0ee", "PDF DOCUMENT"
        else:
            file_icon, icon_background, format_label = "📄", "#e9edff", "TEXT DOCUMENT"
        upload_date = doc.upload_date.strftime("%d %b %Y") if getattr(doc, "upload_date", None) else "Date unavailable"
        processing_status = str(metadata.get("processing_status", "Not indexed"))
        safe_name = html.escape(display_name)
        safe_status = html.escape(processing_status)
        render_html(f"""
        <div class="kb-document-card"><div class="kb-document-row">
          <div class="kb-file-icon" style="background:{icon_background};">{file_icon}</div>
          <div class="kb-file-info"><div class="kb-file-name">{safe_name}</div>
            <div class="kb-file-detail">{format_label} &nbsp;·&nbsp; {size_label} &nbsp;·&nbsp; Added {upload_date}</div>
          </div><div><span class="kb-status">{safe_status}</span></div>
        </div></div>
        """)
        download_col, delete_col = st.columns([1, 1], vertical_alignment="center")
        with download_col:
            try:
                file_data = fs.open_download_stream(doc._id).read()
                mime_type = metadata.get("content_type", "application/pdf" if extension == ".pdf" else "text/plain")
                st.download_button("⬇ Download", data=file_data, file_name=display_name, mime=mime_type,
                                   key=f"kb_download_{doc._id}", use_container_width=True)
            except Exception:
                st.error("This file is currently unavailable for download.")
        with delete_col:
            if st.button("🗑 Delete", key=f"kb_delete_{doc._id}", use_container_width=True):
                st.session_state["kb_confirm_delete"] = str(doc._id)
        if st.session_state.get("kb_confirm_delete") == str(doc._id):
            with st.container(border=True):
                st.warning(f"Permanently delete '{display_name}'?")
                confirm_col, cancel_col = st.columns(2)
                with confirm_col:
                    if st.button("Yes, delete document", key=f"kb_confirm_yes_{doc._id}", type="primary", use_container_width=True):
                        try:
                            fs.delete(doc._id)
                            st.session_state.pop("kb_confirm_delete", None)
                            st.success("Document deleted.")
                            st.rerun()
                        except Exception as exc:
                            st.error("The document could not be deleted.")
                            with st.expander("View technical details"):
                                st.code(str(exc))
                with cancel_col:
                    if st.button("Cancel", key=f"kb_confirm_cancel_{doc._id}", use_container_width=True):
                        st.session_state.pop("kb_confirm_delete", None)
                        st.rerun()
else:
    render_html("""
    <div class="kb-empty"><div class="kb-empty-icon">⌕</div><div class="kb-empty-title">No documents match your search</div><div class="kb-empty-text">Try a different filename or switch the file-format filter to see more of your library.</div></div>
    """)

# =========================================================
# HOW IT WORKS
# =========================================================
with st.expander("✦ What can I do in the Knowledge Base?"):
    st.markdown("""
    **Available now**
    - Upload PDF and TXT reference documents (up to 10 MB per file).
    - Keep documents in the shared library for users of this app.
    - Search by filename, filter by file format, download and delete files.

    **Planned AI capabilities**
    - Extract text from uploaded documents.
    - Split content into smaller chunks and generate embeddings.
    - Retrieve relevant evidence during AI response evaluations.

    *Text extraction, chunking, embeddings and RAG indexing are not implemented yet. The “Indexed documents” metric therefore remains unavailable for now.*
    """)

# =========================================================
# FOOTER
# =========================================================
render_html("""
<div class="kb-footer"><span>✦ <strong>EvalAI</strong> · AI Response Quality Evaluator</span><span>Knowledge Base · Shared reference library</span></div>
""")
st.write("")
