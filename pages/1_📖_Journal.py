import streamlit as st
from utils.pdf_export import add_pdf_export

st.set_page_config(page_title="Project Journal", page_icon="📖", layout="wide")
st.title("📖 Project Documentation")
st.markdown("This page serves as the complete technical documentation for the Genetic Traits Data Science Application.")
st.markdown("---")
st.header("1. Project Architecture")
st.markdown("The application is structured as a multi-page Streamlit app for clarity and modularity.")
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
st.markdown("---")
st.header("2. Code Implementation")
st.markdown("Below is a representation of the source code for each file in the project.")
st.info("Note: The full, working code is in the actual project files. This is for documentation purposes.")

with st.expander("requirements.txt"):
    st.code("streamlit\npandas\nplotly\nscikit-learn\ngraphviz", language="text")
with st.expander("utils/pdf_export.py"):
    st.code("# Contains a helper function to add a 'Download as PDF' button.", language="python")
with st.expander("Home.py (Main Dashboard)"):
    st.code("# The landing page. Handles data loading (demo or user-uploaded), displays metrics, profile cards, and analysis tabs.", language="python")
with st.expander("pages/2_🤖_Trait_Prediction.py (ML Model)"):
    st.code("# Allows users to interact with a Decision Tree model trained on the data and view the model's structure.", language="python")

add_pdf_export()
