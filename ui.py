
import streamlit as st


def apply_design():
    st.markdown("""
    <style>
    .stApp {
        background: #F3F6FC;
        color: #172B4D;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #10264B, #173C70);
        min-width: 245px;
    }

    [data-testid="stSidebar"] > div {
        background: transparent;
    }

    [data-testid="stSidebar"] * {
        color: #FFFFFF;
    }

    [data-testid="stSidebar"] button {
        background: rgba(255,255,255,0.08) !important;
        border: 1px solid rgba(255,255,255,0.18) !important;
        border-radius: 10px !important;
        min-height: 43px;
        width: 100%;
        transition: 0.2s ease;
    }

    [data-testid="stSidebar"] button:hover {
        background: #2867C7 !important;
        border-color: #8CB9FF !important;
    }

    [data-testid="stSidebar"] button p,
    [data-testid="stSidebar"] button span,
    [data-testid="stSidebar"] button div {
        color: white !important;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 1.8rem;
        padding-bottom: 2.5rem;
    }

    div[data-testid="stForm"] {
        background: white;
        border: 1px solid #DFE7F3;
        border-radius: 16px;
        padding: 22px;
    }

    .stButton button,
    div[data-testid="stFormSubmitButton"] button {
        border-radius: 10px;
        min-height: 43px;
        font-weight: 600;
    }

    div[data-testid="stMetric"] {
        background: white;
        padding: 17px;
        border: 1px solid #DFE7F3;
        border-radius: 13px;
    }

    </style>
    """, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="padding:12px 2px 20px;">
            <div style="font-size:34px;">🧠</div>
            <div style="font-size:20px;font-weight:800;">
                Response Evaluator
            </div>
            <div style="font-size:12px;color:#C7D8F5;margin-top:6px;">
                AI Quality Assurance Platform
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.caption("WORKSPACE")

        pages = [
            ("🏠  Home", "pages/1_Home.py"),
            ("📝  Evaluation Hub", "pages/2_Evaluation_Hub.py"),
            ("📊  Results & Analytics", "pages/3_Results_Analytics.py"),
            ("🗂️  Knowledge Base", "pages/4_Knowledge_Base.py"),
            ("📄  Batch Evaluation", "pages/5_Batch_Evaluation.py"),
        ]

        for label, path in pages:
            if st.button(
                label,
                key=f"navigation_{path}",
                use_container_width=True,
            ):
                st.switch_page(path)

        st.divider()
        st.caption("PROJECT STATUS")
        st.markdown("""
        <div style="
            background:rgba(255,255,255,0.09);
            border:1px solid rgba(255,255,255,0.15);
            border-radius:10px;
            padding:12px;
            font-size:12px;
            line-height:1.7;">
            🟡 Frontend prototype<br>
            Backend integration pending
        </div>
        """, unsafe_allow_html=True)
