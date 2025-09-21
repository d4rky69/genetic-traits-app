import pandas as pd
import random
import streamlit as st
import plotly.express as px

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Genetic Traits Dashboard",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------
# Custom CSS for UI Enhancement
# ------------------------------
st.markdown("""
<style>
    /* Style for metric cards */
    [data-testid="stMetric"] {
        background-color: #262730;
        border: 1px solid #3A3A4E;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
    }
    [data-testid="stMetric"]:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    /* Center-align the footer */
    .footer {
        text-align: center;
        color: grey;
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)


# ------------------------------
# Data Generation (Cached)
# ------------------------------
@st.cache_data
def generate_data():
    """Generates and returns a DataFrame with random genetic trait data."""
    names = [
        "Aarav", "Vihaan", "Aditya", "Arjun", "Krishna", "Rohan", "Ishaan", "Kunal",
        "Sanya", "Ananya", "Priya", "Kavya", "Ritika", "Nisha", "Meera", "Divya",
        "Rahul", "Amit", "Sneha", "Pooja", "Varun", "Neha", "Shreya", "Manish",
        "Akash", "Vikram", "Sunita", "Lakshmi", "Ramesh", "Deepak", "Geeta", "Ajay",
        "Suresh", "Anjali", "Swati"
    ]
    
    data = []
    for i, name in enumerate(names, 1):
        data.append([
            i, name, random.randint(18, 25), random.choice(["Brown", "Black"]),
            random.choice(["Yes", "No"]), random.choice(["Free", "Attached"]),
            random.choice(["Yes", "No"]),
            # --- MODIFIED LINE: Updated handedness to be more realistic ---
            random.choices(["Right", "Left", "Mixed"], weights=[0.89, 0.10, 0.01])[0]
        ])
    
    # --- MODIFIED LINE: Changed column name from "Right Handed" ---
    fields = ["S.No", "Name", "Age", "Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Handedness"]
    return pd.DataFrame(data, columns=fields)

df = generate_data()

# ------------------------------
# Sidebar for Controls
# ------------------------------
with st.sidebar:
    st.header("🔬 Filter Controls")
    # --- MODIFIED LINE: Updated trait options list ---
    trait_options = ["Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Handedness"]
    selected_trait = st.selectbox("Choose a trait to filter by:", trait_options)
    unique_values = df[selected_trait].unique()
    selected_value = st.radio(f"Select a value for {selected_trait}:", unique_values, horizontal=True)

# ------------------------------
# Main Page Content
# ------------------------------
st.title("🧬 Genetic Traits Dashboard")
st.markdown("An interactive dashboard to explore genetic traits across 35 individuals.")

# --- QUICK STATS ---
st.markdown("### 📊 Quick Stats")
total_individuals = len(df)
# --- MODIFIED LINE: Updated calculation for right-handedness percentage ---
right_handed_percentage = (df['Handedness'].value_counts(normalize=True).get('Right', 0)) * 100
dimples_percentage = (df['Dimples'].value_counts(normalize=True).get('Yes', 0)) * 100

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Individuals", f"{total_individuals}")
with col2:
    st.metric("Right-Handed", f"{right_handed_percentage:.1f}%")
with col3:
    st.metric("Have Dimples", f"{dimples_percentage:.1f}%")

st.markdown("---")

# --- DATA & ANALYSIS TABS ---
tab1, tab2 = st.tabs(["🗃️ Dataset Explorer", "📈 Trait Analysis"])

with tab1:
    st.header("Full Dataset with Live Filter")
    st.info(f"Highlighting individuals where **{selected_trait}** is **{selected_value}**.")
    
    def highlight_rows(row):
        if row[selected_trait] == selected_value:
            return ['background-color: #3A3A4E; color: white'] * len(row)
        return [''] * len(row)

    st.dataframe(df.style.apply(highlight_rows, axis=1), use_container_width=True, height=500)

with tab2:
    st.header("Detailed Summary for Each Trait")
    for trait in trait_options:
        with st.expander(f"🔬 Analysis for: **{trait}**"):
            counts = df[trait].value_counts()
            summary_df = pd.DataFrame({
                "Value": counts.index, "Count": counts.values
            }).reset_index(drop=True)
            
            st.dataframe(summary_df, use_container_width=True, hide_index=True)
            
            col_chart1, col_chart2 = st.columns(2)
            with col_chart1:
                fig_bar = px.bar(summary_df, x="Value", y="Count", color="Value", title=f"Bar Chart: {trait}")
                st.plotly_chart(fig_bar, use_container_width=True)
            with col_chart2:
                fig_pie = px.pie(summary_df, names="Value", values="Count", title=f"Pie Chart: {trait}", hole=0.3)
                st.plotly_chart(fig_pie, use_container_width=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("<div class='footer'>👨‍💻 Created by <b>Shreyas Sahoo</b></div>", unsafe_allow_html=True)
