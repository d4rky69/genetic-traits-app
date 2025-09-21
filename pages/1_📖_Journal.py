import streamlit as st
from utils.pdf_export import add_pdf_export

st.set_page_config(page_title="Project Journal", page_icon="📖", layout="wide")
st.title("📖 Project Journal: Building the Genetic Traits App")

st.markdown("This journal documents the process and key decisions made during the development of this Data Science Application.")
st.markdown("---")

st.header("1. Project Goal & Core Technologies")
st.markdown("""
The objective was to build a web application for a B.Tech CSE project that went beyond a simple dashboard. The goal was to demonstrate skills in UI/UX design, data analysis, and machine learning.

**Core Technologies:**
- **Streamlit:** For the web application framework.
- **Pandas:** For data generation and manipulation.
- **Plotly:** For interactive data visualizations.
- **Scikit-learn:** For building and evaluating the predictive machine learning model.
""")

st.header("2. Key Features Implemented")
st.markdown("""
- **Interactive Dashboard:** The main page features metric cards for a quick overview, a filterable and highlightable data table, and detailed charts for each trait.
- **Data Science Visualizations:** To add analytical depth, I included a **Histogram** for age distribution and a **Correlation Heatmap** to discover potential relationships between traits in the dataset.
- **Predictive Machine Learning Model:** The app's most advanced feature is a separate page where a **Decision Tree Classifier**, trained on the dataset, predicts an individual's handedness based on other traits.
- **Model Explainability:** Crucially, the Decision Tree is visualized, showing the model's internal logic. This demonstrates an understanding of 'explainable AI', a key concept in modern computer science.
- **Utility Features:** For a professional finish, I added options to **Download the Data as a CSV** and **Export any Page as a PDF**.
""")

st.header("3. Deployment")
st.markdown("The project is hosted on GitHub and deployed live using **Streamlit Community Cloud**. The continuous integration/continuous deployment (CI/CD) feature automatically updates the live app with every `git push` to the main branch.")

st.info("This project demonstrates a complete workflow: from data generation and UI design to implementing and explaining a machine learning model, and finally deploying it on a live server.", icon="🚀")
add_pdf_export()
