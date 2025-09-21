import pandas as pd
import random
import streamlit as st
import plotly.express as px

# ------------------------------
# Page Configuration
# ------------------------------
# Use st.set_page_config() as the first Streamlit command.
st.set_page_config(
    page_title="Genetic Traits Dashboard",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------
# Data Generation (Cached for performance)
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
            i,
            name,
            random.randint(18, 25),
            random.choice(["Brown", "Black"]),
            random.choice(["Yes", "No"]),
            random.choice(["Free", "Attached"]),
            random.choice(["Yes", "No"]),
            random.choices(["Yes", "No"], weights=[0.9, 0.1])[0]
        ])
    
    fields = ["S.No", "Name", "Age", "Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Right Handed"]
    return pd.DataFrame(data, columns=fields)

df = generate_data()

# ------------------------------
# Sidebar for Controls
# ------------------------------
with st.sidebar:
    st.header("🔬 Filter Controls")
    
    # Trait selection for filtering
    trait_options = ["Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Right Handed"]
    selected_trait = st.selectbox(
        "Choose a trait to filter by:",
        trait_options
    )
    
    # Value selection based on the chosen trait
    unique_values = df[selected_trait].unique()
    selected_value = st.radio(
        f"Select a value for {selected_trait}:",
        unique_values,
        horizontal=True
    )

# ------------------------------
# Main Page Content
# ------------------------------

# --- HEADER ---
st.title("🧬 Genetic Traits Dashboard")
st.markdown("An interactive dashboard to explore genetic traits across 35 individuals.")

# --- QUICK STATS ---
st.markdown("### 📊 Quick Stats")
total_individuals = len(df)
right_handed_percentage = (df['Right Handed'].value_counts(normalize=True).get('Yes', 0)) * 100
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

    # Function to highlight rows based on selection
    def highlight_rows(row):
        if row[selected_trait] == selected_value:
            return ['background-color: #2E4C6D; color: white'] * len(row)
        return [''] * len(row)

    # Display the styled DataFrame
    st.dataframe(
        df.style.apply(highlight_rows, axis=1),
        use_container_width=True,
        height=500
    )

with tab2:
    st.header("Detailed Summary for Each Trait")
    
    # Loop through traits to create summary sections
    for trait in trait_options:
        with st.expander(f"🔬 Analysis for: **{trait}**"):
            # --- Summary Table ---
            counts = df[trait].value_counts()
            percentages = round((counts / len(df)) * 100, 2)
            summary_df = pd.DataFrame({
                "Value": counts.index,
                "Count": counts.values,
                "Percentage (%)": percentages.values
            }).reset_index(drop=True)
            
            st.dataframe(summary_df, use_container_width=True, hide_index=True)
            
            # --- Charts ---
            col_chart1, col_chart2 = st.columns(2)
            
            with col_chart1:
                # Bar Chart with Plotly
                fig_bar = px.bar(
                    summary_df,
                    x="Value",
                    y="Count",
                    color="Value",
                    title=f"Bar Chart: {trait} Distribution",
                    labels={'Count': 'Number of Individuals', 'Value': trait}
                )
                st.plotly_chart(fig_bar, use_container_width=True)

            with col_chart2:
                # Pie Chart with Plotly
                fig_pie = px.pie(
                    summary_df,
                    names="Value",
                    values="Count",
                    title=f"Pie Chart: {trait} Proportions",
                    hole=0.3 # Creates a donut chart effect
                )
                st.plotly_chart(fig_pie, use_container_width=True)

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown(
    """
    <p style='text-align: center; color: grey;'>
        👨‍💻 Created by <b>Shreyas Sahoo</b>
    </p>
    """,
    unsafe_allow_html=True
)
