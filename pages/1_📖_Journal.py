import streamlit as st
from utils.pdf_export import add_pdf_export, load_css

st.set_page_config(page_title="Project Journal", page_icon="📖", layout="wide")
load_css()

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
st.header("2. Key Features Implemented")
st.markdown("""
- **Futuristic UI/UX:** The entire interface was designed with a 'glassmorphism' theme, using custom CSS for an animated aurora background, transparent elements, and hover effects.
- **User Data Upload:** The app is a functional tool, allowing users to upload their own CSV data, which dynamically updates all metrics, charts, and models.
- **Personal Profile Cards:** An engaging UI component that generates a visually appealing 'profile card' for each individual in the dataset.
- **Advanced Data Analysis:** The app includes a **Correlation Heatmap** to discover relationships between traits, a core data science visualization.
- **Predictive Machine Learning:** A separate page is dedicated to a **Decision Tree Classifier** that predicts an individual's handedness based on other traits.
- **Explainable AI:** The Decision Tree is visualized, showing the model's internal logic and demonstrating an understanding of 'explainable AI'.
- **Professional Utilities:** The app includes robust export options, allowing users to **Download Data as a CSV** or **Export any Page as a PDF**.
""")

st.header("3. Deployment")
st.markdown("The project is hosted on GitHub and deployed live using **Streamlit Community Cloud**. This enables CI/CD for automatic updates with every `git push`.")
add_pdf_export()
