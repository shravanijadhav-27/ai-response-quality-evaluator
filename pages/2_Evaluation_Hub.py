
import html
import streamlit as st


# ==================================================
# PAGE CONFIGURATION
# ==================================================
st.set_page_config(
    page_title="Evaluation Hub | EvalAI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

from ui import apply_design, render_sidebar

apply_design()
render_sidebar()


# ==================================================
# HTML RENDERING HELPER
# ==================================================
def render_html(content):
    st.html(content)
# ==================================================
# ICON HELPER
# ==================================================
def icon_svg(name, color="#4775C5", size=25):
    icons = {
        "target": "◎",
        "shield": "⬡",
        "document": "▤",
        "scan": "⌕",
        "upload": "↑",
        "brain": "🧠",
        "chart": "▥",
        "check": "✓",
        "sparkle": "✦",
    }

    return f"""
    <span style="
        color:{color};
        font-size:{size}px;
        font-weight:700;
        line-height:1;
    ">{icons.get(name, "✦")}</span>
    """


# ==================================================
# CUSTOM CSS
# ==================================================
st.markdown(
    """
<style>

/* GENERAL */
.block-container {
    max-width: 1500px;
    padding-top: 1.2rem;
    padding-bottom: 3rem;
}

.stApp,
[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse at 8% 5%, rgba(113, 151, 235, .16) 0%, transparent 34%),
        radial-gradient(ellipse at 92% 14%, rgba(151, 119, 230, .13) 0%, transparent 31%),
        radial-gradient(ellipse at 52% 96%, rgba(91, 160, 205, .10) 0%, transparent 38%),
        linear-gradient(135deg, #F4F7FF 0%, #EEF3FC 48%, #F7F5FF 100%) !important;
    background-attachment: fixed !important;
}

/* Keep the main canvas transparent so the full-page gradient stays visible. */
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
main {
    background: transparent !important;
}

/* A soft divider between the page canvas and the sidebar. */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #F8FAFF 0%, #EEF3FC 100%) !important;
    border-right: 1px solid rgba(127, 151, 190, .16);
}

/* HERO */
.workspace-hero {
    background: linear-gradient(
        115deg,
        #101D38 0%,
        #183C70 52%,
        #5542A5 100%
    );
    border-radius: 23px;
    padding: 34px 38px;
    margin: 8px 0 30px;
    color: white;
    box-shadow: 0 15px 40px rgba(25,45,90,.18);
    overflow: hidden;
}

.hero-layout {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 30px;
}

.hero-copy {
    flex: 1;
    min-width: 0;
}

.hero-topline {
    color: #B8CEFF;
    font-size: 10px;
    font-weight: 850;
    letter-spacing: 2.5px;
    margin-bottom: 15px;
}

.workspace-hero h1 {
    color: white !important;
    font-size: 36px !important;
    font-weight: 850 !important;
    margin: 0 0 12px !important;
}

.workspace-hero p {
    color: #E0E9FF !important;
    font-size: 14px;
    line-height: 1.9;
    max-width: 650px;
    margin: 0;
}

.hero-pill {
    display: inline-block;
    margin-top: 19px;
    padding: 8px 14px;
    border-radius: 30px;
    background: rgba(255,255,255,.13);
    border: 1px solid rgba(255,255,255,.22);
    color: #E7EEFF;
    font-size: 11px;
    font-weight: 700;
}

.hero-art {
    width: 285px;
    min-width: 230px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.illustration-card {
    width: 220px;
    height: 205px;
    position: relative;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,.3);
    background: linear-gradient(
        145deg,
        rgba(255,255,255,.19),
        rgba(255,255,255,.06)
    );
    box-shadow: 0 15px 35px rgba(0,0,0,.15);
    padding: 15px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.illustration-top {
    color: #DCE8FF;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 1.3px;
}

.illustration-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    background: #83E4C4;
    border-radius: 50%;
    margin-right: 7px;
}

.brain-symbol {
    font-size: 75px;
    text-align: center;
}

.illustration-status {
    color: #E4F0FF;
    font-size: 11px;
    background: rgba(255,255,255,.12);
    border-radius: 8px;
    padding: 9px;
    text-align: center;
}

.illustration-status span {
    color: #83E4C4;
    font-weight: 900;
    margin-right: 5px;
}

.floating-check,
.floating-sparkle {
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    font-size: 19px;
    font-weight: 900;
}

.floating-check {
    width: 34px;
    height: 34px;
    background: #83E4C4;
    color: #183C70;
    left: -16px;
    top: 55px;
}

.floating-sparkle {
    width: 38px;
    height: 38px;
    background: #A99BFF;
    color: white;
    right: -15px;
    bottom: 45px;
}

/* SECTION HEADINGS */
.section-kicker {
    color: #4775C5;
    font-size: 10px;
    font-weight: 850;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 5px;
}

.section-title {
    color: #152B4B;
    font-size: 23px;
    font-weight: 850;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #7888A0;
    font-size: 12px;
    line-height: 1.7;
    margin-bottom: 17px;
}

/* PANELS */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFFFF;
    border: 1px solid #E0E7F2;
    border-radius: 17px;
    box-shadow: 0 6px 22px rgba(31,55,95,.045);
}

/* INPUTS */
.field-heading {
    color: #19375F;
    font-size: 14px;
    font-weight: 800;
    margin: 7px 0 4px;
}

.field-help {
    color: #8795AA;
    font-size: 11px;
    margin-bottom: 9px;
}

div[data-testid="stTextArea"] label,
div[data-testid="stFileUploader"] label {
    color: #294467 !important;
    font-weight: 700 !important;
}

div[data-testid="stTextArea"] textarea {
    background: #F8FAFE !important;
    color: #183454 !important;
    -webkit-text-fill-color: #183454 !important;
    caret-color: #183454 !important;
    border: 1px solid #D7E1EF !important;
    border-radius: 10px !important;
    font-size: 13px !important;
}

div[data-testid="stTextArea"] textarea::placeholder {
    color: #91A0B5 !important;
    -webkit-text-fill-color: #91A0B5 !important;
    opacity: 1 !important;
}

div[data-testid="stTextArea"] textarea:focus {
    background: white !important;
    border: 1px solid #5685DA !important;
    box-shadow: 0 0 0 2px rgba(86,133,218,.12) !important;
}

/* BUTTONS */
div[data-testid="stFormSubmitButton"] button {
    min-height: 49px;
    border-radius: 11px;
    background: linear-gradient(100deg,#2859B8,#6549C8) !important;
    color: white !important;
    border: none !important;
    font-weight: 800 !important;
    font-size: 14px !important;
    box-shadow: 0 6px 16px rgba(64,82,180,.20);
}

div[data-testid="stFormSubmitButton"] button:hover {
    background: linear-gradient(100deg,#204C9F,#5439B4) !important;
}

/* PREMIUM EVALUATION CRITERIA */
.criteria-card {
    --criteria-color: #4775C5;
    position: relative;
    display: flex;
    align-items: center;
    gap: 12px;
    background: linear-gradient(115deg, #FFFFFF 0%, #F4F7FF 100%);
    border: 1px solid #E3EAF5;
    border-radius: 15px;
    padding: 14px 13px 14px 15px;
    margin: 0 0 12px;
    overflow: hidden;
    box-shadow: 0 5px 16px rgba(31,55,95,.055);
    transition: transform .18s ease, box-shadow .18s ease;
}

.criteria-card::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 4px;
    background: var(--criteria-color);
}

.criteria-card::after {
    content: "";
    position: absolute;
    width: 76px;
    height: 76px;
    right: -35px;
    top: -38px;
    border-radius: 50%;
    background: var(--criteria-color);
    opacity: .07;
}

.criteria-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 22px rgba(31,55,95,.10);
}

.criteria-icon {
    width: 44px;
    height: 44px;
    min-width: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #FFFFFF;
    border: 1px solid #E6ECF5;
    border-radius: 14px;
    box-shadow: 0 3px 9px rgba(31,55,95,.06);
}

.criteria-copy {
    flex: 1;
    min-width: 0;
    position: relative;
    z-index: 1;
}

.criteria-number {
    display: inline-block;
    color: var(--criteria-color);
    background: #FFFFFF;
    border: 1px solid #E7ECF5;
    border-radius: 20px;
    padding: 3px 8px;
    font-size: 8px;
    font-weight: 900;
    letter-spacing: 1px;
    margin-bottom: 6px;
}

.criteria-name {
    color: #1A3458;
    font-size: 13px;
    font-weight: 850;
    margin-bottom: 4px;
}

.criteria-desc {
    color: #74849B;
    font-size: 10px;
    line-height: 1.55;
}

.criteria-tag {
    position: relative;
    z-index: 1;
    color: var(--criteria-color);
    background: #FFFFFF;
    border: 1px solid #E8EDF5;
    border-radius: 20px;
    padding: 5px 7px;
    font-size: 7px;
    font-weight: 900;
    letter-spacing: .6px;
    white-space: nowrap;
}

.criteria-section-kicker {
    display: inline-block;
    color: #526FB0;
    background: #EDF3FF;
    border: 1px solid #DDE8FC;
    border-radius: 20px;
    padding: 5px 9px;
    font-size: 8px;
    font-weight: 900;
    letter-spacing: 1.1px;
    margin-bottom: 8px;
}

.criteria-section-title {
    color: #19375F;
    font-size: 19px;
    font-weight: 900;
    margin: 0 0 5px;
}

.criteria-section-subtitle {
    color: #8492A8;
    font-size: 10px;
    line-height: 1.65;
    margin: 0 0 17px;
}

/* WORKFLOW — slightly more compact to balance the two columns */
.workflow-step {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 10px 0;
}

.workflow-number {
    background: #E7EEFF;
    color: #315CB0;
    border-radius: 9px;
    min-width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    font-weight: 850;
}

.workflow-text {
    color: #294467;
    font-size: 11px;
    font-weight: 700;
}

/* RESULTS HEADER */
.results-heading {
    background: linear-gradient(110deg,#142C50,#344F91);
    padding: 23px 26px;
    border-radius: 17px;
    margin-top: 32px;
    margin-bottom: 17px;
}

.results-heading h2 {
    color: white !important;
    font-size: 23px !important;
    margin: 0 0 6px !important;
}

.results-heading p {
    color: #D9E5FF !important;
    font-size: 12px;
    margin: 0;
}

/* RESULT CARDS */
.metric-label {
    color: #8290A5;
    font-size: 10px;
    font-weight: 850;
    letter-spacing: 1px;
}

.metric-value {
    color: #193D73;
    font-size: 29px;
    font-weight: 850;
    margin-top: 10px;
}

.metric-caption {
    color: #8795AA;
    font-size: 11px;
    margin-top: 5px;
}

/* SCORE GAUGE */
.score-gauge {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 13px auto;
    position: relative;
}

.score-gauge-inner {
    width: 119px;
    height: 119px;
    border-radius: 50%;
    background: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.score-gauge-number {
    color: #183B70;
    font-size: 34px;
    font-weight: 850;
    line-height: 1.1;
}

.score-gauge-label {
    color: #8290A5;
    font-size: 10px;
    margin-top: 5px;
    font-weight: 700;
}

/* PREMIUM SAMPLE DIMENSION PANEL */
.sample-dimension-panel {
    background: #FFFFFF;
    border: 1px solid #DFE7F2;
    border-radius: 17px;
    padding: 20px;
    box-shadow: 0 8px 24px rgba(31,55,95,.055);
}
.sample-dimension-top {
    background: linear-gradient(112deg, #172E55 0%, #294C83 62%, #51469A 100%);
    border-radius: 13px;
    padding: 18px 19px;
    color: #FFFFFF;
    margin-bottom: 17px;
}
.sample-dimension-eyebrow {
    color: #BFD2F3;
    font-size: 9px;
    font-weight: 850;
    letter-spacing: 1.8px;
    margin-bottom: 7px;
}
.sample-dimension-heading {
    color: #FFFFFF;
    font-size: 17px;
    font-weight: 850;
    margin-bottom: 4px;
}
.sample-dimension-caption {
    color: #D7E3F7;
    font-size: 10px;
    line-height: 1.6;
}
.sample-dimension-stats {
    display: flex;
    gap: 10px;
    margin-top: 15px;
}
.sample-dimension-stat {
    flex: 1;
    background: rgba(255,255,255,.11);
    border: 1px solid rgba(255,255,255,.13);
    border-radius: 10px;
    padding: 9px 11px;
}
.sample-dimension-stat-label {
    color: #C9D8F0;
    font-size: 9px;
    font-weight: 700;
}
.sample-dimension-stat-value {
    color: #FFFFFF;
    font-size: 21px;
    font-weight: 850;
    margin-top: 2px;
}
.sample-dimension-row {
    padding: 13px 2px 14px;
    border-bottom: 1px solid #EDF1F7;
}
.sample-dimension-row:last-of-type {
    border-bottom: none;
}
.sample-dimension-row-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
}
.sample-dimension-row-left {
    display: flex;
    align-items: center;
    gap: 11px;
    min-width: 0;
}
.sample-dimension-index {
    width: 29px;
    height: 29px;
    min-width: 29px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 9px;
    background: #F0F4FB;
    color: #6680A7;
    font-size: 9px;
    font-weight: 850;
}
.sample-dimension-name {
    color: #294467;
    font-size: 12px;
    font-weight: 850;
}
.sample-dimension-desc {
    color: #8A98AB;
    font-size: 9px;
    margin-top: 3px;
    line-height: 1.45;
}
.sample-dimension-score {
    color: #193D73;
    font-size: 19px;
    font-weight: 900;
    white-space: nowrap;
}
.sample-dimension-score small {
    color: #91A0B4;
    font-size: 9px;
    font-weight: 700;
}
.sample-dimension-track {
    height: 7px;
    background: #E9EEF6;
    border-radius: 20px;
    overflow: hidden;
    margin: 10px 0 0 40px;
}
.sample-dimension-fill {
    height: 100%;
    border-radius: 20px;
}
.sample-dimension-note {
    background: #F5F8FD;
    border: 1px solid #E8EEF7;
    border-radius: 10px;
    padding: 10px 12px;
    color: #71839D;
    font-size: 9px;
    line-height: 1.65;
    margin-top: 15px;
}
.sample-demo-label {
    display: inline-block;
    background: #EAF1FF;
    border: 1px solid #D7E4FC;
    color: #4167A7;
    border-radius: 20px;
    padding: 5px 9px;
    font-size: 8px;
    font-weight: 850;
    letter-spacing: .8px;
}
@media (max-width: 760px) {
    .sample-dimension-panel { padding: 13px; }
    .sample-dimension-stats { gap: 7px; }
    .sample-dimension-stat { padding: 8px; }
    .sample-dimension-track { margin-left: 0; }
}

/* FEEDBACK */
.feedback-heading {
    display: flex;
    align-items: center;
    gap: 7px;
    color: #1D3B65;
    font-size: 13px;
    font-weight: 850;
    margin-bottom: 11px;
}

.feedback-panel ul {
    padding-left: 17px;
    color: #687C98;
    font-size: 12px;
    line-height: 1.8;
}

/* SAMPLE PREVIEW */
.sample-banner {
    display: flex;
    align-items: center;
    gap: 10px;
    background: #F0F5FF;
    border: 1px solid #DCE7FA;
    color: #355A94;
    border-radius: 12px;
    padding: 12px 15px;
    font-size: 11px;
    line-height: 1.6;
    margin: 10px 0 17px;
}

.sample-card-title {
    color: #1D3B65;
    font-size: 14px;
    font-weight: 850;
    margin-bottom: 5px;
}

.sample-card-subtitle {
    color: #8492A8;
    font-size: 11px;
    line-height: 1.6;
}

.sample-verdict {
    display: inline-block;
    color: #237A60;
    background: #E8F7F0;
    border: 1px solid #CBEBDD;
    padding: 7px 13px;
    border-radius: 25px;
    font-size: 11px;
    font-weight: 800;
    margin-top: 8px;
}

.sample-dimension {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #294467;
    font-size: 12px;
    font-weight: 750;
    margin: 13px 0 6px;
}

.sample-dimension span:last-child {
    color: #315CB0;
    font-weight: 850;
}

/* EMPTY STATE */
.empty-results {
    background: #F8FAFE;
    border: 1px dashed #C9D6E9;
    border-radius: 16px;
    padding: 30px 20px;
    text-align: center;
    color: #73849C;
    font-size: 13px;
    line-height: 1.8;
}

.status-note {
    background: #FFF8EA;
    border: 1px solid #F0DCA9;
    border-radius: 12px;
    padding: 15px 18px;
    color: #78561A;
    font-size: 12px;
    line-height: 1.8;
    margin-top: 22px;
}

.page-footer {
    text-align: center;
    color: #91A0B4;
    font-size: 11px;
    padding: 30px 0 5px;
}

/* MOBILE */
@media (max-width: 760px) {
    .hero-layout {
        flex-direction: column;
        align-items: flex-start;
    }

    .hero-art {
        width: 100%;
        max-width: 230px;
        margin: 10px auto 0;
    }

    .workspace-hero {
        padding: 26px 22px;
    }

    .workspace-hero h1 {
        font-size: 27px !important;
    }
}




/* ==========================================================
   TARGETED DARK PANELS — keyed Streamlit containers
   ========================================================== */

/* Explicitly keyed container surfaces */
.st-key-evaluation_input_panel,
.st-key-evaluation_criteria_panel {
    border-radius: 20px !important;
    padding: 20px !important;
    overflow: hidden !important;
    box-shadow: 0 16px 38px rgba(13, 28, 58, .20) !important;
}

/* Evaluation Input: deep navy with a blue glow */
.st-key-evaluation_input_panel {
    background:
        radial-gradient(ellipse at 100% 0%, rgba(91, 122, 226, .30) 0%, transparent 42%),
        linear-gradient(145deg, #101B32 0%, #172B4D 55%, #202B55 100%) !important;
    border: 1px solid #40577F !important;
}

/* What We Evaluate: navy with a violet glow */
.st-key-evaluation_criteria_panel {
    background:
        radial-gradient(ellipse at 100% 0%, rgba(139, 104, 230, .34) 0%, transparent 42%),
        linear-gradient(150deg, #111B34 0%, #19294B 58%, #28244F 100%) !important;
    border: 1px solid #514B80 !important;
}

/* Keep nested Streamlit layout wrappers transparent */
.st-key-evaluation_input_panel [data-testid="stVerticalBlock"],
.st-key-evaluation_criteria_panel [data-testid="stVerticalBlock"] {
    background: transparent !important;
}

/* Evaluation Input heading and supporting caption */
.st-key-evaluation_input_panel h3 {
    color: #FFFFFF !important;
    font-size: 22px !important;
    font-weight: 850 !important;
}

.st-key-evaluation_input_panel [data-testid="stCaptionContainer"],
.st-key-evaluation_input_panel [data-testid="stCaptionContainer"] p {
    color: #C8D5EA !important;
}

/* Field labels and helper text */
.st-key-evaluation_input_panel .field-heading {
    color: #FFFFFF !important;
    font-size: 13px !important;
    font-weight: 850 !important;
}

.st-key-evaluation_input_panel .field-help {
    color: #B8C8E1 !important;
}

/* Bright, readable text-entry surfaces */
.st-key-evaluation_input_panel [data-testid="stTextArea"] textarea {
    background: #F8FAFF !important;
    color: #172D4D !important;
    -webkit-text-fill-color: #172D4D !important;
    caret-color: #172D4D !important;
    border: 1px solid #B9CBE8 !important;
    border-radius: 12px !important;
}

.st-key-evaluation_input_panel [data-testid="stTextArea"] textarea::placeholder {
    color: #8192AC !important;
    -webkit-text-fill-color: #8192AC !important;
    opacity: 1 !important;
}

.st-key-evaluation_input_panel [data-testid="stTextArea"] textarea:focus {
    background: #FFFFFF !important;
    border: 1px solid #83AFFF !important;
    box-shadow: 0 0 0 3px rgba(105, 153, 245, .24) !important;
}

/* Reference expander */
.st-key-evaluation_input_panel [data-testid="stExpander"] {
    background: rgba(255,255,255,.075) !important;
    border: 1px solid rgba(190,207,239,.30) !important;
    border-radius: 12px !important;
}

.st-key-evaluation_input_panel [data-testid="stExpander"] summary,
.st-key-evaluation_input_panel [data-testid="stExpander"] summary p {
    color: #F0F4FF !important;
}

/* Document uploader */
.st-key-evaluation_input_panel [data-testid="stFileUploader"] {
    background: rgba(255,255,255,.07) !important;
    border: 1px dashed #8FA7D1 !important;
    border-radius: 12px !important;
}

.st-key-evaluation_input_panel [data-testid="stFileUploader"] label,
.st-key-evaluation_input_panel [data-testid="stFileUploader"] small,
.st-key-evaluation_input_panel [data-testid="stFileUploader"] span {
    color: #EAF1FF !important;
}

/* Quality framework title and subtitle */
.st-key-evaluation_criteria_panel .criteria-section-kicker {
    color: #E1DCFF !important;
    background: rgba(153,132,255,.19) !important;
    border: 1px solid rgba(190,174,255,.38) !important;
}

.st-key-evaluation_criteria_panel .criteria-section-title {
    color: #FFFFFF !important;
    font-size: 21px !important;
}

.st-key-evaluation_criteria_panel .criteria-section-subtitle {
    color: #C7D2E8 !important;
}

/* Colorful glass-style dimension cards */
.st-key-evaluation_criteria_panel .criteria-card {
    background: linear-gradient(115deg, rgba(255,255,255,.12), rgba(255,255,255,.055)) !important;
    border: 1px solid rgba(194,208,239,.24) !important;
    box-shadow: 0 7px 18px rgba(3,12,29,.18) !important;
    backdrop-filter: blur(8px);
}

.st-key-evaluation_criteria_panel .criteria-icon {
    background: rgba(255,255,255,.13) !important;
    border: 1px solid rgba(255,255,255,.22) !important;
}

.st-key-evaluation_criteria_panel .criteria-number {
    color: #FFFFFF !important;
    background: color-mix(in srgb, var(--criteria-color) 28%, #172544) !important;
    border: 1px solid color-mix(in srgb, var(--criteria-color) 68%, transparent) !important;
}

.st-key-evaluation_criteria_panel .criteria-name {
    color: #FFFFFF !important;
}

.st-key-evaluation_criteria_panel .criteria-desc {
    color: #C9D5E9 !important;
}

.st-key-evaluation_criteria_panel .criteria-tag {
    color: #F1F4FF !important;
    background: rgba(255,255,255,.11) !important;
    border: 1px solid rgba(255,255,255,.22) !important;
}

.st-key-evaluation_criteria_panel .criteria-card:hover {
    background: linear-gradient(115deg, rgba(255,255,255,.17), rgba(255,255,255,.08)) !important;
    border-color: color-mix(in srgb, var(--criteria-color) 65%, transparent) !important;
}
/* PREPARE EVALUATION BUTTON */
.st-key-evaluation_input_panel [data-testid="stFormSubmitButton"] button,
.st-key-evaluation_input_panel [data-testid="stFormSubmitButton"] button p,
.st-key-evaluation_input_panel [data-testid="stFormSubmitButton"] button span {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    opacity: 1 !important;
    font-weight: 800 !important;
}

.st-key-evaluation_input_panel [data-testid="stFormSubmitButton"] button {
    background: linear-gradient(100deg, #3975E8, #7655D9) !important;
    border: none !important;
    min-height: 50px !important;
    border-radius: 12px !important;
}
</style>
""",
    unsafe_allow_html=True,
)


# ==================================================
# HERO ILLUSTRATION
# ==================================================
hero_illustration = """
<div class="illustration-card">

    <div class="illustration-top">
        <span class="illustration-dot"></span>
        AI QUALITY ANALYSIS
    </div>

    <div class="brain-symbol">🧠</div>

    <div class="illustration-status">
        <span>✓</span> Response quality analysis
    </div>

    <div class="floating-check">✓</div>
    <div class="floating-sparkle">✦</div>

</div>
"""


# ==================================================
# HERO RENDERING
# ==================================================
render_html(
    f"""
    <div class="workspace-hero">

        <div class="hero-layout">

            <div class="hero-copy">

                <div class="hero-topline">
                    AI RESPONSE QUALITY WORKSPACE
                </div>

                <h1>Evaluate Your AI Responses</h1>

                <p>
                    Ensure accuracy, relevance and completeness with
                    intelligent AI response evaluation.
                </p>

                <div class="hero-pill">
                    Intelligent Quality Assessment
                </div>

            </div>

            <div class="hero-art">
                {hero_illustration}
            </div>

        </div>

    </div>
    """
)


# ==================================================
# WORKSPACE INTRODUCTION
# ==================================================
render_html(
    """
    <div class="section-kicker">WORKSPACE 01</div>

    <div class="section-title">
        Start a new evaluation
    </div>

    <div class="section-subtitle">
        Submit your question and AI response. Add reference information
        when you have a trusted source available.
    </div>
    """
)


# ==================================================
# TWO-COLUMN WORKSPACE
# ==================================================
left_col, right_col = st.columns([1.75, 1], gap="large")


# ==================================================
# LEFT: INPUT FORM
# ==================================================
with left_col:

    with st.container(border=True, key="evaluation_input_panel"):

        st.markdown("### Evaluation Input")

        st.caption(
            "Provide the information required for quality assessment."
        )

        with st.form("evaluation_form", clear_on_submit=False):

            render_html(
                """
                <div class="field-heading">
                    01 · Original Question *
                </div>

                <div class="field-help">
                    Enter the question originally asked by the user.
                </div>
                """
            )

            question = st.text_area(
                "Original question",
                placeholder="Example: Explain how solar panels generate electricity.",
                height=130,
                label_visibility="collapsed",
                key="eval_question",
            )

            render_html(
                """
                <div class="field-heading">
                    02 · AI-Generated Answer *
                </div>

                <div class="field-help">
                    Paste the complete response you want to evaluate.
                </div>
                """
            )

            answer = st.text_area(
                "AI-generated answer",
                placeholder="Paste the complete AI-generated answer here...",
                height=230,
                label_visibility="collapsed",
                key="eval_answer",
            )

            render_html(
                """
                <div class="field-heading">
                    03 · Reference Information
                </div>

                <div class="field-help">
                    Optional · Add trusted information for comparison.
                </div>
                """
            )

            with st.expander(
                "＋ Add reference answer or upload document"
            ):

                reference_answer = st.text_area(
                    "Trusted reference answer",
                    placeholder="Enter a verified answer or supporting facts...",
                    height=140,
                    key="eval_reference",
                )

                reference_document = st.file_uploader(
                    "Upload reference document",
                    type=["pdf", "txt"],
                    accept_multiple_files=False,
                    help="PDF and TXT files are accepted.",
                    key="eval_document",
                )

            render_html(
                """
                <div style="
                    background:#EEF4FF;
                    border:1px solid #DCE7FA;
                    border-radius:10px;
                    padding:12px 14px;
                    color:#466184;
                    font-size:11px;
                    line-height:1.7;
                    margin:12px 0;
                ">
                    <b>TIP</b> · Use the complete AI response and a reliable
                    reference source for a more meaningful evaluation.
                </div>
                """
            )

            submitted = st.form_submit_button(
                "Prepare Evaluation",
                type="primary",
                use_container_width=True,
            )


# ==================================================
# RIGHT: EVALUATION CRITERIA
# ==================================================
with right_col:

    with st.container(border=True, key="evaluation_criteria_panel"):

        render_html(
            """
            <div class="criteria-section-kicker">THE QUALITY FRAMEWORK · 04 CHECKS</div>
            <div class="criteria-section-title">What We Evaluate</div>
            <div class="criteria-section-subtitle">
                Every response is assessed across four important quality dimensions.
            </div>
            """
        )

        criteria = [
            (
                "target",
                "#4775C5",
                "01",
                "Relevance",
                "Does the response answer the original question?",
            ),
            (
                "shield",
                "#269B79",
                "02",
                "Accuracy",
                "Are the statements factually correct?",
            ),
            (
                "document",
                "#8062C9",
                "03",
                "Completeness",
                "Does the answer cover the important information?",
            ),
            (
                "scan",
                "#D18B36",
                "04",
                "Hallucination Detection",
                "Does the response contain unsupported claims?",
            ),
        ]

        for icon, color, number, name, description in criteria:

            render_html(
                f"""
                <div class="criteria-card" style="--criteria-color:{color};">

                    <div class="criteria-icon">
                        {icon_svg(icon, color, 24)}
                    </div>

                    <div class="criteria-copy">
                        <div class="criteria-number">
                            DIMENSION {number}
                        </div>

                        <div class="criteria-name">
                            {html.escape(name)}
                        </div>

                        <div class="criteria-desc">
                            {html.escape(description)}
                        </div>
                    </div>

                    <div class="criteria-tag">QUALITY CHECK</div>

                </div>
                """
            )

    # WORKFLOW PANEL — kept in the right column below the criteria
    with st.container(border=True):

        st.markdown("### Evaluation Workflow")

        workflow = [
            ("upload", "Submit question and AI response"),
            ("brain", "Send input to evaluation backend"),
            ("scan", "Run quality assessment agents"),
            ("chart", "Display scores and explanations"),
        ]

        for index, (icon, step) in enumerate(workflow, start=1):

            render_html(
                f"""
                <div class="workflow-step">

                    <div class="workflow-number">
                        {index:02}
                    </div>

                    <div>
                        {icon_svg(icon, "#4775C5", 18)}
                    </div>

                    <div class="workflow-text">
                        {html.escape(step)}
                    </div>

                </div>
                """
            )

        st.caption(
            "Backend processing is not connected yet. "
            "These steps describe the planned workflow."
        )


# ==================================================
# INPUT VALIDATION
# ==================================================
if submitted:

    if not question.strip():

        st.error("Please enter the original question.")

    elif not answer.strip():

        st.error("Please enter the AI-generated answer.")

    else:

        st.session_state.pop("evaluation_result", None)

        st.session_state["evaluation_input_valid"] = True

        st.success("Input validation completed successfully.")

        st.markdown("### Submission Overview")

        metric1, metric2, metric3 = st.columns(3)

        metric1.metric(
            "Question Length",
            f"{len(question.strip())} characters",
        )

        metric2.metric(
            "Answer Length",
            f"{len(answer.strip())} characters",
        )

        has_reference = bool(
            reference_answer.strip() or reference_document
        )

        metric3.metric(
            "Reference Information",
            "Provided" if has_reference else "Not provided",
        )

        st.warning(
            "Your input has been validated, but no evaluation has been "
            "performed. The backend API is not connected yet."
        )


# ==================================================
# ACTUAL BACKEND RESULTS
# ==================================================
result = st.session_state.get("evaluation_result")


# ==================================================
# RESULTS SECTION HEADING — ALWAYS VISIBLE
# ==================================================
render_html(
    """
    <div class="results-heading">
        <h2>Evaluation Results</h2>
        <p>
            Explore overall quality, individual dimensions,
            verdict and detailed feedback.
        </p>
    </div>
    """
)


if isinstance(result, dict):

    overall_score = result.get("overall_score")

    verdict = str(
        result.get("verdict", "Not provided")
    )

    dimensions = result.get("dimensions", {})

    summary = str(
        result.get("summary", "No summary provided.")
    )

    # OVERALL SCORE AND VERDICT
    score_col, verdict_col = st.columns([1, 1])

    with score_col:

        with st.container(border=True):

            render_html(
                '<div class="metric-label">OVERALL QUALITY SCORE</div>'
            )

            if isinstance(overall_score, (int, float)):

                safe_score = max(
                    0,
                    min(100, float(overall_score))
                )

                gauge_degrees = safe_score * 3.6

                render_html(
                    f"""
                    <div class="score-gauge"
                         style="background:conic-gradient(
                         #4775C5 {gauge_degrees}deg,
                         #E7EDF7 {gauge_degrees}deg);">

                        <div class="score-gauge-inner">

                            <div class="score-gauge-number">
                                {safe_score:g}
                            </div>

                            <div class="score-gauge-label">
                                OUT OF 100
                            </div>

                        </div>
                    </div>
                    """
                )

            else:

                st.info("Overall score is unavailable.")

    with verdict_col:

        with st.container(border=True):

            render_html(
                '<div class="metric-label">FINAL VERDICT</div>'
            )

            render_html(
                f"""
                <div class="metric-value" style="font-size:25px;">
                    {html.escape(verdict)}
                </div>

                <div class="metric-caption">
                    Verdict returned by the evaluation system
                </div>
                """
            )

    # DIMENSION SCORES
    st.markdown("### Dimension-wise Assessment")

    if isinstance(dimensions, dict) and dimensions:

        dimension_items = list(dimensions.items())

        dimension_columns = st.columns(2, gap="medium")

        for index, (dimension, score) in enumerate(dimension_items):

            with dimension_columns[index % 2]:

                with st.container(border=True):

                    dimension_name = (
                        str(dimension)
                        .replace("_", " ")
                        .title()
                    )

                    st.markdown(
                        f"**{html.escape(dimension_name)}**"
                    )

                    if isinstance(score, (int, float)):

                        safe_score = max(
                            0,
                            min(100, float(score))
                        )

                        st.progress(safe_score / 100)

                        st.caption(f"{score}/100")

                    else:

                        st.write(str(score))

    else:

        st.info("No dimension-wise scores were returned.")

    # SUMMARY
    st.markdown("### Evaluation Summary")

    with st.container(border=True):

        st.write(summary)

    # FEEDBACK PANELS
    feedback_sections = [
        ("Strengths", "strengths"),
        ("Identified Issues", "issues"),
        ("Improvement Suggestions", "suggestions"),
    ]

    feedback_columns = st.columns(3, gap="medium")

    for column, (heading, key) in zip(
        feedback_columns,
        feedback_sections
    ):

        with column:

            with st.container(border=True):

                st.markdown(f"**{heading}**")

                feedback = result.get(key, [])

                if isinstance(feedback, str):
                    feedback = [feedback]

                if isinstance(feedback, list) and feedback:

                    for item in feedback:

                        st.markdown(
                            f"- {html.escape(str(item))}"
                        )

                else:

                    st.caption("No feedback returned.")

else:

    # ==================================================
    # SAMPLE EVALUATION PREVIEW
    # ==================================================
    st.markdown("---")

    render_html(
        """
        <div class="section-kicker">
            DEMO REPORT
        </div>

        <div class="section-title">
            Explore a sample evaluation
        </div>

        <div class="section-subtitle">
            This example demonstrates how an evaluation report could look
            after the backend returns its scores and explanations.
        </div>

        <div class="sample-banner">
            <span style="font-size:20px;">ⓘ</span>

            <span>
                <b>Demonstration data only.</b>
                The following scores are illustrative and are not generated
                by your evaluation agents or backend.
            </span>
        </div>
        """
    )


    # SAMPLE VALUES - DEMONSTRATION ONLY
    sample_metrics = {
        "Relevance": 95,
        "Accuracy": 85,
        "Completeness": 88,
        "Hallucination Control": 80,
    }


    sample_left, sample_right = st.columns(
        [0.85, 1.5],
        gap="large"
    )


    # ==================================================
    # SAMPLE SCORE
    # ==================================================
    with sample_left:

        with st.container(border=True):

            render_html(
                """
                <div class="sample-card-title">
                    Overall quality score
                </div>

                <div class="sample-card-subtitle">
                    Illustrative combined assessment
                </div>
                """
            )

            render_html(
                """
                <div style="text-align:center;padding:18px 0;">

                    <div class="score-gauge"
                         style="background:conic-gradient(
                         #4775C5 313.2deg,
                         #E7EDF7 313.2deg);">

                        <div class="score-gauge-inner">

                            <div class="score-gauge-number">
                                87
                            </div>

                            <div class="score-gauge-label">
                                OUT OF 100
                            </div>

                        </div>
                    </div>

                    <div class="sample-verdict">
                        GOOD QUALITY
                    </div>

                </div>
                """
            )

            st.caption(
                "Sample verdict shown for interface demonstration."
            )


    # ==================================================
    # PREMIUM SAMPLE DIMENSION BREAKDOWN
    # ==================================================
    with sample_right:

        dimension_details = [
            ("01", "Relevance", "How closely the answer addresses the question", 95, "#4775C5"),
            ("02", "Accuracy", "Factual correctness of the response", 85, "#269B79"),
            ("03", "Completeness", "Coverage of essential information", 88, "#8062C9"),
            ("04", "Hallucination Control", "Avoidance of unsupported claims", 80, "#D18B36"),
        ]

        dimension_rows = []

        for number, name, description, score, color in dimension_details:
            dimension_rows.append(
                f"""
                <div class="sample-dimension-row">
                    <div class="sample-dimension-row-top">
                        <div class="sample-dimension-row-left">
                            <div class="sample-dimension-index">{number}</div>
                            <div>
                                <div class="sample-dimension-name">{html.escape(name)}</div>
                                <div class="sample-dimension-desc">{html.escape(description)}</div>
                            </div>
                        </div>
                        <div class="sample-dimension-score">
                            {score}<small> / 100</small>
                        </div>
                    </div>
                    <div class="sample-dimension-track">
                        <div class="sample-dimension-fill"
                             style="width:{score}%;background:{color};"></div>
                    </div>
                </div>
                """
            )

        render_html(
            f"""
            <div class="sample-dimension-panel">
                <div class="sample-dimension-top">
                    <div style="display:flex;align-items:center;justify-content:space-between;gap:10px;">
                        <div class="sample-dimension-eyebrow">EVALUATION ANALYTICS</div>
                        <span class="sample-demo-label">SAMPLE DATA</span>
                    </div>
                    <div class="sample-dimension-heading">Quality Assessment</div>
                    <div class="sample-dimension-caption">
                        Detailed overview of the four AI response quality dimensions
                    </div>
                    <div class="sample-dimension-stats">
                        <div class="sample-dimension-stat">
                            <div class="sample-dimension-stat-label">DIMENSIONS ASSESSED</div>
                            <div class="sample-dimension-stat-value">04</div>
                        </div>
                        <div class="sample-dimension-stat">
                            <div class="sample-dimension-stat-label">AVERAGE SCORE</div>
                            <div class="sample-dimension-stat-value">87<span style="font-size:10px;font-weight:650;"> / 100</span></div>
                        </div>
                    </div>
                </div>

                {''.join(dimension_rows)}

                <div class="sample-dimension-note">
                    <b>Scoring note:</b> Hallucination Control represents the ability
                    to avoid unsupported claims. A higher score indicates better
                    control; it is not a hallucination-risk percentage.
                </div>
            </div>
            """
        )


    # ==================================================
    # SAMPLE REPORT INSIGHTS
    # ==================================================
    st.markdown("### Sample Report Insights")

    feedback_col1, feedback_col2, feedback_col3 = st.columns(
        3,
        gap="medium"
    )


    # STRENGTHS
    with feedback_col1:

        with st.container(border=True):

            render_html(
                f"""
                <div class="feedback-heading">
                    {icon_svg("check", "#269B79", 21)}
                    <span>Strengths</span>
                </div>
                """
            )

            st.markdown(
                """
                - Directly addresses the question.
                - Mostly accurate information.
                - Clear and understandable explanation.
                """
            )


    # AREAS TO REVIEW
    with feedback_col2:

        with st.container(border=True):

            render_html(
                f"""
                <div class="feedback-heading">
                    {icon_svg("scan", "#D18B36", 21)}
                    <span>Areas to Review</span>
                </div>
                """
            )

            st.markdown(
                """
                - Some supporting details are missing.
                - A few claims need stronger evidence.
                - Reference comparison can be improved.
                """
            )


    # SUGGESTIONS
    with feedback_col3:

        with st.container(border=True):

            render_html(
                f"""
                <div class="feedback-heading">
                    {icon_svg("sparkle", "#8062C9", 21)}
                    <span>Suggestions</span>
                </div>
                """
            )

            st.markdown(
                """
                - Add reliable supporting sources.
                - Explain important details more fully.
                - Verify claims against reference material.
                """
            )



# ==================================================
# DEVELOPMENT STATUS
# ==================================================
render_html(
    """
    <div class="status-note">

        <b>Development Status</b><br>

        Frontend input fields, validation and results layout are implemented.
        Actual evaluation, API communication and reference-document processing
        still require backend integration. Sample results above are only for
        demonstrating the interface.

    </div>
    """
)


# ==================================================
# FOOTER
# ==================================================
render_html(
    """
    <div class="page-footer">

        EVALAI · AI RESPONSE QUALITY PLATFORM

        <br>

        Evaluate with clarity. Build with confidence.

    </div>
    """
)
