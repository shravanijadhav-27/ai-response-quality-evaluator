
import streamlit as st
from pymongo import MongoClient
from gridfs import GridFSBucket
from datetime import datetime, timezone
import os
import html
from io import BytesIO
# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Knowledge Base | EvalAI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

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

# =========================================================
# HTML RENDERING HELPER
# =========================================================

def render_html(content):
    """Render HTML directly using Streamlit's HTML renderer."""
    st.html(content)


# =========================================================
# MONGODB CONNECTION
# =========================================================

@st.cache_resource
def get_mongodb_connection():
    try:
        mongodb_uri = st.secrets["MONGODB_URI"]

        database_name = st.secrets.get(
            "MONGODB_DATABASE",
            DATABASE_NAME
        )

        client = MongoClient(
            mongodb_uri,
            serverSelectionTimeoutMS=10000,
        )

        client.admin.command("ping")

        database = client[database_name]

        bucket = GridFSBucket(
            database,
            bucket_name=BUCKET_NAME,
        )

        return client, database, bucket, None

    except Exception as exc:
        return None, None, None, str(exc)


mongo_client, database, fs, connection_error = (
    get_mongodb_connection()
)

# =========================================================
# CUSTOM CSS
# =========================================================

render_html("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 90% 2%,
            rgba(80,125,220,0.08),
            transparent 28%
        ),
        #F3F6FC;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* HERO */

.kb-hero {
    padding: 36px 38px;
    border-radius: 23px;
    background:
        radial-gradient(
            circle at 90% 10%,
            rgba(148,115,255,0.45),
            transparent 28%
        ),
        linear-gradient(
            115deg,
            #101B35,
            #183D75 55%,
            #315DC2
        );
    box-shadow: 0 15px 38px rgba(24,52,105,0.19);
    margin-bottom: 25px;
    color: white;
}

.kb-eyebrow {
    display: inline-block;
    padding: 7px 13px;
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 30px;
    background: rgba(255,255,255,0.10);
    color: #DCE8FF;
    font-size: 12px;
    font-weight: 750;
    letter-spacing: 1.2px;
    margin-bottom: 15px;
}

.kb-hero h1 {
    color: #FFFFFF !important;
    font-size: clamp(30px,4vw,44px);
    font-weight: 850;
    line-height: 1.15;
    margin: 0 0 12px 0;
}

.kb-hero p {
    color: #D5E2FF !important;
    font-size: 16px;
    line-height: 1.7;
    max-width: 690px;
    margin: 0;
}

.kb-hero-bottom {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 24px;
}

.kb-hero-tag {
    padding: 8px 12px;
    border-radius: 9px;
    background: rgba(255,255,255,0.11);
    border: 1px solid rgba(255,255,255,0.12);
    color: #F1F5FF;
    font-size: 12px;
    font-weight: 600;
}

/* SECTION HEADINGS */

.kb-section-heading {
    color: #142C50;
    font-size: 22px;
    font-weight: 800;
    margin: 24px 0 5px 0;
}

.kb-section-description {
    color: #718096;
    font-size: 14px;
    margin-bottom: 17px;
}

/* METRIC CARDS */

.kb-metric {
    background: #FFFFFF;
    border: 1px solid #E3EAF5;
    border-radius: 17px;
    padding: 20px;
    min-height: 135px;
    box-shadow: 0 5px 18px rgba(28,54,100,0.045);
}

.kb-metric-icon {
    width: 40px;
    height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 12px;
    font-size: 20px;
    margin-bottom: 12px;
}

.kb-metric-value {
    font-size: 30px;
    font-weight: 850;
    color: #142C50;
}

.kb-metric-label {
    color: #74839A;
    font-size: 13px;
    font-weight: 600;
    margin-top: 4px;
}

/* PANELS */

.kb-panel-dark .kb-panel-title {
    color: #FFFFFF;
    font-size: 19px;
    font-weight: 800;
}

.kb-panel-dark .kb-panel-description {
    color: #DEDFFF;
}
.kb-panel-dark {
    background:
        radial-gradient(
            circle at 100% 0%,
            rgba(157, 115, 255, 0.32),
            transparent 42%
        ),
        linear-gradient(
            145deg,
            #171A3B 0%,
            #292B59 60%,
            #39366F 100%
        );

    border: 1px solid #55558F;
    border-radius: 20px;
    padding: 25px;
    color: white;
    box-shadow: 0 12px 28px rgba(30, 30, 75, 0.20);
}

.kb-panel-dark .kb-panel-title {
    color: white;
}

.kb-panel-dark .kb-panel-description {
    color: #CEDCF3;
}

.kb-feature {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 17px 0;
    color: #E6EEFF;
    font-size: 13px;
    line-height: 1.6;
}

.kb-feature-icon {
    width: 35px;
    height: 35px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255,255,255,0.12);
    border-radius: 10px;
    flex-shrink: 0;
}

.kb-upload-hint {
    padding: 14px;
    border-radius: 12px;
    background: #F0F5FF;
    border: 1px dashed #A9BFE8;
    color: #48638A;
    font-size: 13px;
    line-height: 1.8;
    margin-top: 12px;
}

/* DOCUMENT CARDS */

.kb-document-card {
    background: #FFFFFF;
    border: 1px solid #E2EAF5;
    border-radius: 16px;
    padding: 18px;
    margin: 12px 0 7px 0;
    box-shadow: 0 4px 15px rgba(20,45,90,0.035);
}

.kb-document-row {
    display: flex;
    align-items: center;
    gap: 15px;
}

.kb-file-icon {
    display: flex;
    width: 47px;
    height: 47px;
    align-items: center;
    justify-content: center;
    border-radius: 13px;
    font-size: 23px;
    flex-shrink: 0;
}

.kb-file-info {
    flex: 1;
    min-width: 0;
}

.kb-file-name {
    color: #19365F;
    font-size: 15px;
    font-weight: 750;
    overflow-wrap: anywhere;
}

.kb-file-detail {
    color: #8290A4;
    font-size: 12px;
    margin-top: 5px;
}

.kb-status {
    display: inline-block;
    padding: 6px 10px;
    border-radius: 20px;
    background: #FFF4E5;
    color: #A96B15;
    font-size: 11px;
    font-weight: 750;
    white-space: nowrap;
}

/* EMPTY STATE */

.kb-empty {
    text-align: center;
    padding: 38px 20px;
    border: 1px dashed #B8C9E2;
    background: #F8FAFE;
    border-radius: 18px;
}

.kb-empty-icon {
    font-size: 40px;
    margin-bottom: 10px;
}

.kb-empty-title {
    color: #1C365C;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 7px;
}

.kb-empty-text {
    color: #7B8BA2;
    font-size: 13px;
}

/* CONTROLS */

div.stButton > button,
div.stDownloadButton > button {
    border-radius: 10px !important;
    font-weight: 700 !important;
    min-height: 40px;
}

div[data-testid="stFileUploader"] {
    background: #F7F9FE;
    border: 1px dashed #A9BFE8;
    border-radius: 14px;
    padding: 12px;
}

</style>
""")

# =========================================================
# HERO
# =========================================================

render_html("""
<div class="kb-hero">

    <div class="kb-eyebrow">
        ✦ KNOWLEDGE MANAGEMENT
    </div>

    <h1>Your AI Knowledge Center.</h1>

    <p>
        One library. Smarter evaluations.
        Organize trusted reference documents and make
        them accessible across your AI response evaluations.
    </p>

    <div class="kb-hero-bottom">
        <span class="kb-hero-tag">📚 Shared document library</span>
        <span class="kb-hero-tag">📄 PDF &amp; TXT support</span>
        <span class="kb-hero-tag">🔐 MongoDB GridFS</span>
    </div>

</div>
""")

# =========================================================
# FLASH MESSAGE
# =========================================================

if st.session_state.pop("kb_flash", False):
    st.success("Document saved successfully to the Knowledge Base.")

# =========================================================
# CONNECTION STATUS
# =========================================================

if connection_error:
    st.error("MongoDB Atlas connection failed.")

    with st.expander("View connection details"):
        st.code(connection_error)

    st.info(
        "Check MONGODB_URI and MONGODB_DATABASE in "
        ".streamlit/secrets.toml and verify Atlas Network Access."
    )

    st.stop()

st.success("MongoDB Atlas connected successfully.")

# =========================================================
# LOAD DOCUMENTS
# =========================================================

def list_documents():
    try:
        docs = list(fs.find({}).sort("uploadDate", -1))

        docs = [
            doc for doc in docs
            if doc.filename.lower().endswith((".pdf", ".txt"))
        ]

        return docs, None

    except Exception as exc:
        return [], str(exc)


documents, list_error = list_documents()

if list_error:
    st.error("Could not retrieve documents from MongoDB.")
    st.code(list_error)

# =========================================================
# SUMMARY METRICS
# =========================================================

total_documents = len(documents)

total_storage = sum(doc.length for doc in documents)

if total_storage < 1024 * 1024:
    storage_label = f"{total_storage / 1024:.1f} KB"
else:
    storage_label = f"{total_storage / (1024 * 1024):.2f} MB"

metric_cols = st.columns(3)

metrics = [
    ("📁", "#EAF1FF", total_documents, "Total Documents"),
    ("🧠", "#F0EAFF", "—", "Indexed Documents"),
    ("💾", "#E5F8F4", storage_label, "Storage Used"),
]

for col, metric in zip(metric_cols, metrics):
    icon, background, value, label = metric

    with col:
        render_html(f"""
        <div class="kb-metric">

            <div class="kb-metric-icon"
                 style="background:{background};">
                {icon}
            </div>

            <div class="kb-metric-value">
                {html.escape(str(value))}
            </div>

            <div class="kb-metric-label">
                {html.escape(label)}
            </div>

        </div>
        """)

st.write("")

# =========================================================
# UPLOAD SECTION
# =========================================================

render_html("""
<div class="kb-section-heading">
    Add to your knowledge library
</div>

<div class="kb-section-description">
    Upload trusted reference material and keep it
    available for future evaluations.
</div>
""")

upload_col, storage_col = st.columns(
    [1.35, 0.85],
    gap="large"
)

# ---------------- UPLOAD PANEL ----------------
st.html("""
<style>
/* UPLOAD CARD */
.kb-upload-card {
    background:
        radial-gradient(
            circle at 100% 0%,
            rgba(65, 220, 255, 0.22),
            transparent 38%
        ),
        linear-gradient(
            135deg,
            #102747 0%,
            #164B82 60%,
            #087EAA 100%
        );

    border: 1px solid #2878B9;
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 12px 28px rgba(13, 55, 100, 0.20);
    margin-bottom: 15px;
}

.kb-upload-eyebrow {
    color: #6ce4ff;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 12px;
}

.kb-upload-title {
    color: #ffffff;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 8px;
}

.kb-upload-description {
    color: #d1e5fa;
    font-size: 13px;
    line-height: 1.7;
    margin-bottom: 20px;
}

.kb-drop-zone {
    background: rgba(255,255,255,0.09);
    border: 2px dashed #67dcf6;
    border-radius: 16px;
    padding: 23px 12px;
    text-align: center;
}

.kb-upload-icon {
    width: 58px;
    height: 58px;
    background: linear-gradient(135deg, #2786f4, #16c3d8);
    border-radius: 17px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 29px;
    margin: 0 auto 12px auto;
    box-shadow: 0 7px 18px rgba(0,0,0,0.2);
}

.kb-drop-title {
    color: white;
    font-size: 17px;
    font-weight: 750;
}

.kb-drop-description {
    color: #d1e7ff;
    font-size: 12px;
    margin-top: 6px;
}

.kb-upload-tags {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 15px;
}

.kb-upload-tag {
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.24);
    color: white;
    border-radius: 20px;
    padding: 6px 11px;
    font-size: 10px;
    font-weight: 750;
}

.kb-upload-security {
    color: #d9f5ff;
    font-size: 11px;
    margin-top: 18px;
}

/* STREAMLIT UPLOADER */
div[data-testid="stFileUploader"] {
    background: #f0f7ff;
    border: 1px solid #c8ddf5;
    border-radius: 13px;
    padding: 12px;
    margin-top: 10px;
}

div[data-testid="stFileUploader"] section {
    background: #e3f0ff;
    border: 1px dashed #3988d9;
    border-radius: 10px;
}

/* SAVE BUTTON */
div[data-testid="st-key-kb_save_button"] button {
    background: linear-gradient(90deg, #1768d5, #078eaf);
    color: white;
    border: none;
    border-radius: 11px;
    font-weight: 750;
    padding: 12px;
    box-shadow: 0 5px 15px rgba(23,104,213,0.22);
    transition: all 0.2s ease;
}

div[data-testid="st-key-kb_save_button"] button:hover {
    background: linear-gradient(90deg, #1054b4, #05728e);
    color: white;
    border: none;
    transform: translateY(-2px);
}

/* UPLOAD STATUS */
div[data-testid="stFileUploader"] small {
    color: #42678f;
}
</style>
""")

# ---------------- UPLOAD PANEL ----------------

with upload_col:

    render_html("""
    <div class="kb-upload-card">

        <div class="kb-upload-eyebrow">
            ✦ DOCUMENT MANAGEMENT
        </div>

        <div class="kb-upload-title">
            Upload your knowledge.
        </div>

        <div class="kb-upload-description">
            Bring trusted information into your AI evaluation
            workspace. Your documents will be available in
            the shared knowledge library.
        </div>

        <div class="kb-drop-zone">

            <div class="kb-upload-icon">☁️</div>

            <div class="kb-drop-title">
                Add documents to your library
            </div>

            <div class="kb-drop-description">
                Select a PDF or TXT document below.
            </div>

            <div class="kb-upload-tags">
                <span class="kb-upload-tag">PDF DOCUMENTS</span>
                <span class="kb-upload-tag">TXT FILES</span>
                <span class="kb-upload-tag">MAX 10 MB</span>
            </div>

        </div>

        <div class="kb-upload-security">
            ✓ Private MongoDB Atlas storage
            &nbsp; | &nbsp; ✓ Shared document collection
        </div>

    </div>
    """)

    uploaded_file = st.file_uploader(
        "Choose a document",
        type=["pdf", "txt"],
        help="Maximum file size: 10 MB.",
        key="kb_upload_file",
    )

    if st.button(
        "☁️ Save to Knowledge Base",
        type="primary",
        use_container_width=True,
        key="kb_save_button",
    ):

        if uploaded_file is None:
            st.error("Please choose a PDF or TXT file first.")

        elif uploaded_file.size > MAX_FILE_SIZE_BYTES:
            st.error(
                f"File exceeds the {MAX_FILE_SIZE_MB} MB limit."
            )

        else:
            try:
                original_name = os.path.basename(
                    uploaded_file.name
                )

                extension = os.path.splitext(
                    original_name
                )[1].lower()

                if extension not in [".pdf", ".txt"]:
                    st.error("Only PDF and TXT files are allowed.")

                else:
                    content_type = (
                        "application/pdf"
                        if extension == ".pdf"
                        else "text/plain"
                    )

                    file_bytes = uploaded_file.getvalue()

                    metadata = {
                        "original_name": original_name,
                        "content_type": content_type,
                        "uploaded_at": datetime.now(
                            timezone.utc
                        ).isoformat(),
                        "processing_status": "Not indexed",
                    }

                    fs.upload_from_stream(
                        original_name,
                        BytesIO(file_bytes),
                        metadata=metadata,
                    )

                    st.session_state["kb_flash"] = True
                    st.rerun()

            except Exception as exc:
                st.error(f"Could not save document: {exc}")



# ---------------- STORAGE PANEL ----------------

with storage_col:

    render_html("""
    <div class="kb-panel-dark">

        <div class="kb-panel-title">
            🔐 Secure cloud storage
        </div>

        <div class="kb-panel-description">
            Your reference documents are stored
            in MongoDB Atlas GridFS.
        </div>

        <div class="kb-feature">
            <div class="kb-feature-icon">🟢</div>
            <div>
                <b>Database connection</b><br>
                MongoDB Atlas connected
            </div>
        </div>

        <div class="kb-feature">
            <div class="kb-feature-icon">🗄️</div>
            <div>
                <b>Database</b><br>
                evalai
            </div>
        </div>

        <div class="kb-feature">
            <div class="kb-feature-icon">📦</div>
            <div>
                <b>GridFS bucket</b><br>
                knowledge_documents
            </div>
        </div>

        <div class="kb-feature">
            <div class="kb-feature-icon">📄</div>
            <div>
                <b>Accepted formats</b><br>
                PDF and TXT
            </div>
        </div>

    </div>
    """)

    st.write("")

    with st.container(border=True):

        st.markdown("**⚙️ Document processing**")

        st.caption(
            "Currently, the Knowledge Base supports "
            "document storage and retrieval."
        )

        st.info(
            "Text extraction, chunking, embeddings "
            "and RAG indexing are not implemented yet."
        )

# =========================================================
# DOCUMENT LIBRARY
# =========================================================

render_html("""
<div class="kb-section-heading">
    📂 Your document library
</div>

<div class="kb-section-description">
    Explore, search, download and manage your saved
    reference documents.
</div>
""")

# =========================================================
# SEARCH AND FILTER
# =========================================================

search_col, type_col, refresh_col = st.columns(
    [1.6, 0.8, 0.7],
    vertical_alignment="bottom"
)

with search_col:
    search_text = st.text_input(
        "🔍 Search documents",
        placeholder="Search by document name...",
        key="kb_search",
    )

with type_col:
    type_filter = st.selectbox(
        "📑 File format",
        ["All files", "PDF", "TXT"],
        key="kb_type_filter",
    )

with refresh_col:
    if st.button(
        "↻ Refresh",
        use_container_width=True,
        key="kb_refresh",
    ):
        st.rerun()

# =========================================================
# FILTER DOCUMENTS
# =========================================================

filtered_documents = []

for doc in documents:

    stored_name = doc.filename
    extension = os.path.splitext(stored_name)[1].lower()

    if (
        search_text
        and search_text.casefold() not in stored_name.casefold()
    ):
        continue

    if type_filter == "PDF" and extension != ".pdf":
        continue

    if type_filter == "TXT" and extension != ".txt":
        continue

    filtered_documents.append(doc)

# =========================================================
# DISPLAY DOCUMENTS
# =========================================================

if not documents and not list_error:

    render_html("""
    <div class="kb-empty">
        <div class="kb-empty-icon">📚</div>

        <div class="kb-empty-title">
            Your knowledge library is waiting!
        </div>

        <div class="kb-empty-text">
            No documents have been uploaded yet.
            Upload your first PDF or TXT reference file
            to get started.
        </div>
    </div>
    """)

elif filtered_documents:

    st.caption(
        f"Showing {len(filtered_documents)} "
        f"of {len(documents)} documents"
    )

    for doc in filtered_documents:

        stored_name = doc.filename
        metadata = doc.metadata or {}

        display_name = metadata.get(
            "original_name",
            stored_name
        )

        extension = os.path.splitext(
            stored_name
        )[1].lower()

        file_size = doc.length

        if file_size < 1024 * 1024:
            size_label = f"{file_size / 1024:.1f} KB"
        else:
            size_label = f"{file_size / (1024 * 1024):.2f} MB"

        if extension == ".pdf":
            file_icon = "📕"
            icon_background = "#FDEBEC"
            format_label = "PDF DOCUMENT"
        else:
            file_icon = "📄"
            icon_background = "#EAF2FF"
            format_label = "TEXT DOCUMENT"

        upload_date = doc.upload_date.strftime("%d %b %Y")

        processing_status = metadata.get(
            "processing_status",
            "Not indexed"
        )

        render_html(f"""
        <div class="kb-document-card">

            <div class="kb-document-row">

                <div class="kb-file-icon"
                     style="background:{icon_background};">
                    {file_icon}
                </div>

                <div class="kb-file-info">

                    <div class="kb-file-name">
                        {html.escape(str(display_name))}
                    </div>

                    <div class="kb-file-detail">
                        {format_label}
                        &nbsp; · &nbsp;
                        {size_label}
                        &nbsp; · &nbsp;
                        Uploaded {upload_date}
                    </div>

                </div>

                <div>
                    <span class="kb-status">
                        {html.escape(str(processing_status))}
                    </span>
                </div>

            </div>

        </div>
        """)

        download_col, delete_col, spacer_col = st.columns(
            [0.19, 0.19, 0.62],
            vertical_alignment="center"
        )

        with download_col:

            try:
                file_data = fs.open_download_stream(
                    doc._id
                ).read()

                mime_type = metadata.get(
                    "content_type",
                    "application/pdf"
                    if extension == ".pdf"
                    else "text/plain"
                )

                st.download_button(
                    "⬇️ Download",
                    data=file_data,
                    file_name=display_name,
                    mime=mime_type,
                    key=f"kb_download_{doc._id}",
                    use_container_width=True,
                )

            except Exception as exc:
                st.error(f"Download unavailable: {exc}")

        with delete_col:

            if st.button(
                "🗑️ Delete",
                key=f"kb_delete_{doc._id}",
                use_container_width=True,
            ):
                st.session_state["kb_confirm_delete"] = str(
                    doc._id
                )

        # DELETE CONFIRMATION

        if (
            st.session_state.get("kb_confirm_delete")
            == str(doc._id)
        ):

            with st.container(border=True):

                st.warning(
                    f"Delete '{display_name}' permanently?"
                )

                confirm_col, cancel_col = st.columns(2)

                with confirm_col:

                    if st.button(
                        "Yes, delete document",
                        key=f"kb_confirm_yes_{doc._id}",
                        type="primary",
                    ):

                        try:
                            fs.delete(doc._id)

                            st.session_state.pop(
                                "kb_confirm_delete",
                                None
                            )

                            st.success(
                                "Document deleted successfully."
                            )

                            st.rerun()

                        except Exception as exc:
                            st.error(f"Delete failed: {exc}")

                with cancel_col:

                    if st.button(
                        "Cancel",
                        key=f"kb_confirm_cancel_{doc._id}",
                    ):

                        st.session_state.pop(
                            "kb_confirm_delete",
                            None
                        )

                        st.rerun()

elif not list_error:

    render_html("""
    <div class="kb-empty">

        <div class="kb-empty-icon">🔎</div>

        <div class="kb-empty-title">
            No matching documents found
        </div>

        <div class="kb-empty-text">
            Try another filename or change the file format filter.
        </div>

    </div>
    """)

# =========================================================
# HOW IT WORKS
# =========================================================

st.write("")

with st.expander("✨ How your Knowledge Base works"):

    info_col1, info_col2 = st.columns(2)

    with info_col1:

        st.markdown("""
        **📚 Shared document library**

        - Upload reusable PDF and TXT files.
        - Store files in MongoDB Atlas GridFS.
        - Retrieve and download saved documents.
        - Search by filename and filter by file type.
        """)

    with info_col2:

        st.markdown("""
        **🧠 Future RAG processing**

        - Extract text from uploaded documents.
        - Split text into smaller chunks.
        - Generate vector embeddings.
        - Retrieve relevant evidence during evaluations.

        *These processing features are not implemented yet.*
        """)

# =========================================================
# FOOTER
# =========================================================

st.divider()

footer_left, footer_right = st.columns([1, 1])

with footer_left:
    st.caption("✦ EvalAI · AI Response Quality Evaluator")

with footer_right:
    st.caption("Knowledge Management · MongoDB Atlas GridFS")

st.write("")

if st.button(
    "← Back to Home",
    key="kb_back_home",
):
    st.switch_page("pages/1_Home.py")
