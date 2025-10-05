import streamlit as st

# --- Optional: Import custom CSS if you want to keep your previous style ---
from utils.pdf_export import load_css

st.set_page_config(
    page_title="Genetic Traits Projects Hub",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# --- Custom CSS for buttons and centering ---
st.markdown("""
<style>
.centered-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 85vh;
}
.welcome-title {
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 0.5em;
    text-align: center;
    color: #222A3F;
}
.welcome-desc {
    font-size: 1.23rem;
    text-align: center;
    color: #69738b;
    margin-bottom: 2.5em;
}
.choice-row {
    display: flex;
    gap: 2em;
}
.btn-project {
    font-size: 1.18rem;
    font-weight: 600;
    padding: 1em 2.2em;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    transition: box-shadow 0.2s, transform 0.2s;
    box-shadow: 0 2px 24px 0 rgba(37,117,252,0.08);
}
.btn-project-yellow {
    background: #FFD43B;
    color: #222A3F;
}
.btn-project-yellow:hover {
    background: #FFEA85;
    color: #222A3F;
    transform: scale(1.03);
    box-shadow: 0 8px 28px 0 rgba(255,212,67,0.18);
}
.btn-project-blue {
    background: #B6C7E6;
    color: #222A3F;
}
.btn-project-blue:hover {
    background: #D3E2FF;
    color: #222A3F;
    transform: scale(1.03);
    box-shadow: 0 8px 28px 0 rgba(37,117,252,0.13);
}
</style>
""", unsafe_allow_html=True)

# --- Main Welcome Layout ---
st.markdown('<div class="centered-container">', unsafe_allow_html=True)
st.markdown('<div class="welcome-title">Welcome</div>', unsafe_allow_html=True)
st.markdown('<div class="welcome-desc">You have two projects available. Please choose one to explore.</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1], gap="large")
with col1:
    dominant_clicked = st.button("Dominant Traits Analyzer", key="dominant", use_container_width=True)
with col2:
    genome_clicked = st.button("Human Genome Explorer", key="genome", use_container_width=True)

# --- Navigation logic: Jump to page when button is clicked ---
if dominant_clicked:
    st.experimental_set_query_params(page="Journal")
    st.switch_page("pages/1_📖_Journal.py")
elif genome_clicked:
    st.experimental_set_query_params(page="GenomeExplorer")
    st.switch_page("pages/3_🌐_Human_Genome_Explorer.py")

st.markdown('</div>', unsafe_allow_html=True)
