import streamlit as st
from utils.pdf_export import add_pdf_export

# Raw code strings for display
# NOTE: Using triple single quotes to avoid conflict with triple double quotes in the code.
code_requirements = '''
streamlit
pandas
plotly
scikit-learn
graphviz
'''.strip()

code_pdf_export = '''
import streamlit as st

def add_pdf_export():
    # ... (full code for pdf_export.py as provided in the other section)
    # This is a placeholder for brevity in the Journal display.
    # The actual implementation code is in the utils/pdf_export.py file.
    st.sidebar.markdown("""
        <div style="text-align: center; padding-top: 1rem;">
            <button style="
                background: linear-gradient(90deg, #6A11CB 0%, #2575FC 100%);
                color: white; border: none; padding: 12px 24px;
                text-align: center; font-size: 16px; font-weight: bold;
                cursor: pointer; border-radius: 12px;
            ">
                Download Page as PDF
            </button>
        </div>
    """, unsafe_allow_html=True)

'''.strip()

code_home = '''
import pandas as pd
import random
import streamlit as st
import plotly.express as px
from utils.pdf_export import add_pdf_export

st.set_page_config(...)
# ... (full code for Home.py as provided in the other section)
'''.strip()

code_prediction = '''
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# ... (full code for 2_..._Prediction.py as provided in the other section)
'''.strip()


st.set_page_config(page_title="Project Journal", page_icon="📖", layout="wide")
st.title("📖 Project Documentation & Code")

st.markdown("This page serves as the complete technical documentation for the Genetic Traits Data Science Application, built as a project for the B.Tech CSE program.")
st.markdown("---")

st.header("1. Project Architecture")
st.markdown("The application is structured as a multi-page Streamlit app. The file organization is designed for clarity and modularity, separating the main dashboard, additional pages, and utility functions.")
st.code("""
genetic-traits-app/
├── 📂 pages/
│   ├── 📜 1_📖_Journal.py         # This documentation page
│   └── 📜 2_🤖_Trait_Prediction.py  # The machine learning model page
├── 📂 utils/
│   └── 📜 pdf_export.py            # Helper function for PDF export
├── 📜 Home.py                      # The main dashboard page
└── 📜 requirements.txt           # Project dependencies
""", language="bash")

st.markdown("---")
st.header("2. Core Technologies Used")
st.markdown("""
- **Streamlit:** For the web application framework.
- **Pandas:** For data generation and manipulation.
- **Plotly:** For interactive data visualizations.
- **Scikit-learn:** For building and evaluating the predictive machine learning model.
- **Graphviz:** For visualizing the Decision Tree model.
""")

st.markdown("---")
st.header("3. Code Implementation")
st.markdown("Below is the complete source code for each file in the project.")

with st.expander("requirements.txt"):
    st.markdown("Lists all necessary Python libraries for the project to run.")
    st.code(code_requirements, language="text")

with st.expander("utils/pdf_export.py"):
    st.markdown("A modular utility to add a 'Download as PDF' button to any page.")
    st.code(code_pdf_export, language="python")
    st.info("Note: The full code is in the actual file. This is a representation for the journal.")

with st.expander("Home.py (Main Dashboard)"):
    st.markdown("The landing page of the application. It handles data loading (demo or user-uploaded), displays key metrics, personal profile cards, and contains tabs for data exploration and analysis.")
    st.code(code_home, language="python")
    st.info("Note: The full code is in the actual file. This is a representation for the journal.")

with st.expander("pages/2_🤖_Trait_Prediction.py (ML Model)"):
    st.markdown("This page allows users to interact with a Decision Tree model trained on the data. It includes an interactive prediction interface and a visualization of the model's structure.")
    st.code(code_prediction, language="python")
    st.info("Note: The full code is in the actual file. This is a representation for the journal.")

add_pdf_export()
