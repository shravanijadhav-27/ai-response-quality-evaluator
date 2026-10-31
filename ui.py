
import streamlit as st


# =========================================================
# SHARED DESIGN
# =========================================================

def apply_shared_design():
    """Shared styling for all EvalAI pages."""

    st.markdown(
        """
        <style>

        /* MAIN APPLICATION */

        .stApp {
            background: #F4F7FC;
            color: #172B45;
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        h1, h2, h3, h4 {
            color: #142842;
        }

        p, label {
            color: #43546B;
        }


        /* SIDEBAR */

        section[data-testid="stSidebar"] {
            background: linear-gradient(
                180deg,
                #102747 0%,
                #173F6B 55%,
                #102747 100%
            ) !important;

            border-right: 1px solid #294E78 !important;
            min-width: 250px;
        }

        section[data-testid="stSidebar"] > div {
            background: transparent !important;
        }

        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
            color: #D9E8F8 !important;
        }

        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] label {
            color: #E5F0FF !important;
        }

        section[data-testid="stSidebar"] hr {
            border-color: rgba(255,255,255,0.16) !important;
        }


        /* SIDEBAR NAVIGATION LINKS */

        section[data-testid="stSidebar"] [data-testid="stPageLink"] a {
            display: flex;
            align-items: center;
            padding: 11px 13px;
            border-radius: 9px;
            color: #EAF3FF !important;
            background: rgba(255,255,255,0.06) !important;
            border: 1px solid rgba(255,255,255,0.08);
            text-decoration: none !important;
            font-weight: 650;
            transition: 0.2s ease;
        }

        section[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
            background: rgba(58,166,232,0.22) !important;
            border-color: rgba(100,190,255,0.35) !important;
            color: #FFFFFF !important;
        }


        /* SIDEBAR COLLAPSE BUTTON */

        [data-testid="stSidebarCollapsedControl"] {
            display: flex !important;
            visibility: visible !important;
            opacity: 1 !important;
        }

        button[data-testid="stBaseButton-header"] {
            color: #FFFFFF !important;
        }


        /* GENERAL BUTTONS */

        div.stButton > button {
            border-radius: 9px;
            min-height: 40px;
            font-weight: 650;
        }

        div.stButton > button[kind="primary"] {
            background: #10BED8 !important;
            color: #062B40 !important;
            border-color: #10BED8 !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# SINGLE SHARED SIDEBAR
# =========================================================

def render_sidebar():
    """One consistent EvalAI sidebar across all pages."""

    with st.sidebar:

        # BRAND
        st.html("""
            <div style="
                padding: 15px 8px 20px;
                border-bottom: 1px solid rgba(255,255,255,0.16);
                margin-bottom: 20px;
            ">
                <div style="
                    font-size: 29px;
                    font-weight: 850;
                    color: #FFFFFF;
                    letter-spacing: -1px;
                ">
                    Eval<span style="color:#39C8E9;">AI</span>
                </div>

                <div style="
                    color: #B9D0E9;
                    font-size: 11px;
                    margin-top: 4px;
                    letter-spacing: 0.5px;
                ">
                    AI RESPONSE QUALITY PLATFORM
                </div>
            </div>
        """)

        # MENU HEADING
        st.html("""
            <div style="
                color: #8EACCC;
                font-size: 10px;
                font-weight: 800;
                letter-spacing: 1.5px;
                padding: 0 8px 10px;
            ">
                MAIN MENU
            </div>
        """)

        # HOME
        st.page_link(
            "app.py",
            label="Home",
            icon=":material/home:",
            use_container_width=True,
        )

        # EVALUATION HUB
        st.page_link(
            "pages/2_Evaluation_Hub.py",
            label="Evaluation Hub",
            icon=":material/analytics:",
            use_container_width=True,
        )

        # RESULTS ANALYTICS
        st.page_link(
            "pages/3_Results_Analytics.py",
            label="Results Analytics",
            icon=":material/insert_chart:",
            use_container_width=True,
        )

        # KNOWLEDGE BASE
        st.page_link(
            "pages/4_Knowledge_Base.py",
            label="Knowledge Base",
            icon=":material/library_books:",
            use_container_width=True,
        )

        # BATCH EVALUATION
        st.page_link(
            "pages/5_Batch_Evaluation.py",
            label="Batch Evaluation",
            icon=":material/table_chart:",
            use_container_width=True,
        )

        st.divider()

        # WORKSPACE FOOTER
        st.html("""
            <div style="
                padding: 12px 9px;
                background: rgba(255,255,255,0.07);
                border: 1px solid rgba(255,255,255,0.10);
                border-radius: 10px;
            ">
                <div style="
                    color: #FFFFFF;
                    font-size: 12px;
                    font-weight: 750;
                ">
                    EvalAI Workspace
                </div>

                <div style="
                    color: #B9D0E9;
                    font-size: 10px;
                    margin-top: 5px;
                    line-height: 1.5;
                ">
                    AI response evaluation
                    and knowledge management
                </div>
            </div>
        """)


# =========================================================
# COMPATIBILITY FUNCTION
# =========================================================

def apply_design():
    apply_shared_design()
