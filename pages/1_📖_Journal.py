import streamlit as st
from utils.pdf_export import add_pdf_export, load_css

st.set_page_config(page_title="Project Journal", page_icon="📖", layout="wide")
load_css()

st.title("📖 Project Documentation")
# (The rest of this file's content is the same as the previous correct version)
st.markdown("This page serves as the complete technical documentation for the Genetic Traits Data Science Application.")
st.markdown("---")
st.header("1. Project Architecture")
st.code("""
genetic-traits-app/
├── 📂 pages/
│   ├── 📜 1_📖_Journal.py
│   └── 📜 2_🤖_Trait_Prediction.py
├── 📂 utils/
│   └── 📜 pdf_export.py
├── 📜 Home.py
└── 📜 requirements.txt
""", language="bash")
# ... etc.

add_pdf_export()
