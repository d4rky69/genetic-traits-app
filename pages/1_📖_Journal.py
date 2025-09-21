import streamlit as st

st.set_page_config(page_title="Project Journal", page_icon="📖", layout="wide")

st.title("📖 Project Journal: Building the Genetic Traits App")

st.markdown("""
This journal documents the process and key decisions made during the development of the Genetic Traits Dashboard.
""")

st.markdown("---")

# --- Project Goal ---
st.header("1. Project Goal & Core Technologies")
st.markdown("""
The primary objective was to create a dynamic, interactive web application to visualize a small dataset of human genetic traits. The app needed to be user-friendly, visually appealing, and easily shareable.

The project was built using the following core Python libraries:
- **Streamlit:** For creating the web application UI, handling user interactions, and structuring the content.
- **Pandas:** For data manipulation, including creating the initial dataset and performing calculations like counts and percentages.
- **Plotly:** For generating interactive and modern-looking charts (bar and pie charts) to visualize the data distributions.
""")

# --- Development Journey ---
st.header("2. The Development Journey")

st.subheader("Data Generation")
st.markdown("""
The first step was to create a realistic dataset. Since no external data was provided, I used Python's `random` library and Pandas to generate a DataFrame with 35 individuals. Key traits like eye color, dimples, and handedness were included. I assigned a higher probability (90%) to being right-handed to reflect real-world distributions. This entire data generation process was wrapped in a function with Streamlit's `@st.cache_data` decorator to ensure it only runs once, improving app performance.
""")
st.code("""
@st.cache_data
def generate_data():
    # ... code to create and return a Pandas DataFrame ...
    return pd.DataFrame(data, columns=fields)
""", language="python")

st.subheader("Building the UI and Interactivity")
st.markdown("""
I chose a multi-page layout with a persistent sidebar for controls. This provides a clean user experience.
- **Dashboard Metrics:** I added a 'Quick Stats' section at the top using `st.metric` to provide an immediate, high-level overview of the data.
- **Live Filtering:** The core interactive feature is the live filter. A user selects a trait and a value from the sidebar. Instead of creating a new, smaller table, the app uses a custom function with `df.style.apply()` to highlight the matching rows in the main dataframe. This is more intuitive as it provides context within the full dataset.
- **Tabbed Content:** The main page is split into two tabs: one for exploring the raw data (`Dataset Explorer`) and another for a deep dive into each trait's statistics (`Trait Analysis`). This keeps the interface organized.
""")

st.subheader("Data Visualization with Plotly")
st.markdown("""
Initially, I could have used `matplotlib`, but I chose `plotly.express` for its superior interactivity and modern aesthetic. When a user hovers over a bar or a pie slice, they get a tooltip with precise information. This small feature significantly enhances the user experience. The analysis for each trait is neatly tucked into an `st.expander` to avoid cluttering the page.
""")
st.code("""
# Example of creating an interactive Plotly pie chart
fig_pie = px.pie(
    summary_df,
    names="Value",
    values="Count",
    title=f"Pie Chart: {trait} Proportions",
    hole=0.3 # Creates a donut chart
)
st.plotly_chart(fig_pie, use_container_width=True)
""", language="python")

# --- Deployment ---
st.header("3. Deployment")
st.markdown("""
The final step was to make the app publicly accessible. The entire project is hosted on GitHub. I connected the repository to **Streamlit Community Cloud**, which automates the deployment process. 
1.  **Repository Setup:** The repo contains the app file (`Home.py`), the journal page (`pages/1_📖_Journal.py`), and a `requirements.txt` file.
2.  **`requirements.txt`:** This file is crucial. It lists the necessary libraries (`streamlit`, `pandas`, `plotly`) for Streamlit Cloud to install.
3.  **Automation:** Any `git push` to the main branch on GitHub automatically triggers a redeployment, ensuring the live app is always up-to-date with the latest code.
""")

st.info("This project demonstrates a complete workflow: from data generation and interactive UI design to final deployment on a live server.", icon="🚀")
