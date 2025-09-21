import streamlit as st
from utils.pdf_export import add_pdf_export

st.set_page_config(page_title="Project Journal", page_icon="📖", layout="wide")
st.title("📖 Project Journal: Building the Genetic Traits App")

st.markdown("This journal documents the process and key decisions made during the development of this Data Science Application, designed to be a standout B.Tech CSE project.")
st.markdown("---")

st.header("1. Core Philosophy: From Demo to Tool")
st.markdown("""
The primary goal was to evolve the application from a static demonstration into a dynamic, user-centric tool. This was achieved by implementing a key feature: **User Data Upload**. The app now allows users to upload their own CSV files, and all visualizations, metrics, and even the machine learning model will adapt and run on their data. This demonstrates the ability to handle dynamic data sources, a crucial skill in software engineering.
""")

st.header("2. Key Features Implemented")
st.markdown("""
- **Futuristic UI/UX:** The entire interface was redesigned with a 'cozy futuristic' theme, using custom CSS to introduce a modern font, a refined color palette, and subtle hover animations on interactive elements.
- **Personal Profile Cards:** To make the data more engaging, a feature was added to generate visually appealing 'profile cards' for each individual, presenting their traits in a more personal and accessible format.
- **Interactive Dashboard:** The main page features metric cards, a filterable data table, and detailed charts, all of which now dynamically update based on the user's uploaded data or the default demo set.
- **Advanced Data Analysis:** The app includes a **Correlation Heatmap** to discover relationships between traits, a core data science visualization.
- **Predictive Machine Learning:** A separate page is dedicated to a **Decision Tree Classifier** that predicts an individual's handedness. This model also adapts to user-uploaded data.
- **Explainable AI:** Crucially, the Decision Tree is visualized, showing the model's internal logic. This demonstrates an understanding of 'explainable AI'.
- **Professional Utilities:** The app includes robust export options, allowing users to **Download Data as a CSV** or **Export any Page as a PDF**.
""")

st.header("3. Deployment")
st.markdown("The project is hosted on GitHub and deployed live using **Streamlit Community Cloud**, with CI/CD for automatic updates.")
add_pdf_export()
