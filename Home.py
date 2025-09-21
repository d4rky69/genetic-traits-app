import pandas as pd
import random
import streamlit as st
import plotly.express as px
from utils.pdf_export import add_pdf_export

st.set_page_config(
    page_title="Genetic Traits Dashboard",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    [data-testid="stMetric"] {
        background-color: #262730; border: 1px solid #3A3A4E; border-radius: 10px;
        padding: 20px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;
    }
    [data-testid="stMetric"]:hover { box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2); }
    .footer { text-align: center; color: grey; padding-top: 2rem; }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def generate_data():
    names = [
        "Shreyas", "Arnab", "Aditya", "Arjun", "Krishna", "Rohan", "Ishaan", "Kunal",
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
            random.choices(["Right", "Left", "Mixed"], weights=[0.89, 0.10, 0.01])[0]
        ])
    fields = ["S.No", "Name", "Age", "Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Handedness"]
    return pd.DataFrame(data, columns=fields)

df = generate_data()

with st.sidebar:
    st.header("🔬 Filter Controls")
    trait_options = ["Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Handedness"]
    selected_trait = st.selectbox("Choose a trait to filter by:", trait_options)
    unique_values = df[selected_trait].unique()
    selected_value = st.radio(f"Select a value for {selected_trait}:", unique_values, horizontal=True)
    st.markdown("---")
    st.header("📤 Export Options")
    @st.cache_data
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')
    csv = convert_df_to_csv(df)
    st.download_button("Download data as CSV", csv, "genetic_traits_data.csv", "text/csv")
    add_pdf_export()

st.title("🧬 Genetic Traits Dashboard")
st.markdown("An interactive dashboard to explore genetic traits across 35 individuals.")
st.markdown("### 📊 Quick Stats")
total_individuals = len(df)
right_handed_percentage = (df['Handedness'].value_counts(normalize=True).get('Right', 0)) * 100
dimples_percentage = (df['Dimples'].value_counts(normalize=True).get('Yes', 0)) * 100
col1, col2, col3 = st.columns(3)
with col1: st.metric("Total Individuals", f"{total_individuals}")
with col2: st.metric("Right-Handed", f"{right_handed_percentage:.1f}%")
with col3: st.metric("Have Dimples", f"{dimples_percentage:.1f}%")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["🗃️ Dataset Explorer", "📈 Trait Analysis", "🔥 Correlation Analysis"])

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
    with st.expander("🎂 Analysis for: Age"):
        fig_hist = px.histogram(df, x="Age", nbins=8, title="Age Distribution of Individuals")
        st.plotly_chart(fig_hist, use_container_width=True)
    for trait in trait_options:
        with st.expander(f"🔬 Analysis for: **{trait}**"):
            counts = df[trait].value_counts()
            summary_df = pd.DataFrame({"Value": counts.index, "Count": counts.values}).reset_index(drop=True)
            st.dataframe(summary_df, use_container_width=True, hide_index=True)
            col_chart1, col_chart2 = st.columns(2)
            with col_chart1:
                fig_bar = px.bar(summary_df, x="Value", y="Count", color="Value", title=f"Bar Chart: {trait}")
                st.plotly_chart(fig_bar, use_container_width=True)
            with col_chart2:
                fig_pie = px.pie(summary_df, names="Value", values="Count", title=f"Pie Chart: {trait}", hole=0.3)
                st.plotly_chart(fig_pie, use_container_width=True)

with tab3:
    st.header("Correlation Heatmap")
    st.markdown("This heatmap shows the relationship between different traits. A value close to **1** (light color) means the traits are positively correlated (e.g., as one appears, the other tends to appear). A value close to **-1** (dark color) means they are negatively correlated. Values near **0** show little to no relationship.")
    df_corr = df.drop(columns=['S.No', 'Name']).copy()
    for col in df_corr.columns:
        if df_corr[col].dtype == 'object':
            df_corr[col] = df_corr[col].astype('category').cat.codes
    corr = df_corr.corr()
    fig_heatmap = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r', title="Feature Correlation Heatmap")
    st.plotly_chart(fig_heatmap, use_container_width=True)
    st.warning("Note: As this is random data, the correlations are coincidental and do not reflect real biological relationships.", icon="⚠️")

st.markdown("---")
st.markdown("<div class='footer'>👨‍💻 Created by <b>Shreyas Sahoo</b></div>", unsafe_allow_html=True)
