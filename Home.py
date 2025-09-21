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

# --- NEW: Futuristic & Cozy CSS with Hover Animations ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

html, body, [class*="st-"] {
    font-family: 'Poppins', sans-serif;
}
/* Main background */
.stApp {
    background-color: #0E1117;
}
/* Metric card styling */
[data-testid="stMetric"] {
    background-color: #1E1E2D;
    border: 1px solid #4A4A6A;
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 4px 15px 0 rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease-in-out;
}
[data-testid="stMetric"]:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 20px 0 rgba(37, 117, 252, 0.4);
    border: 1px solid #2575FC;
}
/* Profile Card Styling */
.profile-card {
    background: linear-gradient(135deg, #1E1E2D 0%, #2C2C4D 100%);
    padding: 2rem;
    border-radius: 15px;
    border: 1px solid #4A4A6A;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    text-align: center;
    transition: all 0.3s ease-in-out;
}
.profile-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(106, 17, 203, 0.5);
}
.profile-name {
    font-size: 2rem;
    font-weight: 600;
    color: #FFFFFF;
    margin-bottom: 1rem;
}
.trait-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    color: #D1D1E0;
}
.trait-item {
    background-color: #2C2C4D;
    padding: 1rem;
    border-radius: 10px;
}
.trait-label {
    font-weight: 600;
    color: #2575FC;
}
</style>
""", unsafe_allow_html=True)

# --- DATA LOADING LOGIC (with new Uploader) ---
@st.cache_data
def generate_demo_data():
    # (The data generation code is the same as before)
    names = [
        "Shreyas", "Arnab", "Aditya", "Arjun", "Krishna", "Rohan", "Ishaan", "Kunal", "Sanya", "Ananya",
        "Priya", "Kavya", "Ritika", "Nisha", "Meera", "Divya", "Rahul", "Amit", "Sneha", "Pooja",
        "Varun", "Neha", "Shreya", "Manish", "Akash", "Vikram", "Sunita", "Lakshmi", "Ramesh",
        "Deepak", "Geeta", "Ajay", "Suresh", "Anjali", "Swati"
    ]
    data = [[i, name, random.randint(18, 25), random.choice(["Brown", "Black"]), random.choice(["Yes", "No"]),
             random.choice(["Free", "Attached"]), random.choice(["Yes", "No"]),
             random.choices(["Right", "Left", "Mixed"], weights=[0.89, 0.10, 0.01])[0]]
            for i, name in enumerate(names, 1)]
    fields = ["S.No", "Name", "Age", "Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Handedness"]
    return pd.DataFrame(data, columns=fields)

REQUIRED_COLS = {"Name", "Age", "Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Handedness"}

uploaded_file = st.sidebar.file_uploader("📂 Upload your own CSV data", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if not REQUIRED_COLS.issubset(df.columns):
        st.error(f"Error: The uploaded CSV must contain the following columns: {', '.join(REQUIRED_COLS)}")
        st.stop()
    if 'S.No' not in df.columns:
        df.insert(0, 'S.No', range(1, 1 + len(df)))
else:
    df = generate_demo_data()

# --- SIDEBAR ---
with st.sidebar:
    st.header("🔬 Filter & Display Controls")
    trait_options = ["Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Handedness"]
    selected_trait = st.selectbox("Highlight trait:", trait_options)
    unique_values = df[selected_trait].unique()
    selected_value = st.radio(f"Highlight value for {selected_trait}:", unique_values, horizontal=True)
    st.markdown("---")
    st.header("📤 Export Options")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Data as CSV", csv, "genetic_traits_data.csv", "text/csv")
    add_pdf_export()

# --- MAIN PAGE ---
st.title("🧬 Genetic Traits Dashboard")
st.markdown("An interactive dashboard to explore, visualize, and predict genetic traits.")

# --- QUICK STATS ---
st.markdown("### 📊 Quick Stats")
total_individuals = len(df)
right_handed_percentage = (df['Handedness'].value_counts(normalize=True).get('Right', 0)) * 100
dimples_percentage = (df['Dimples'].value_counts(normalize=True).get('Yes', 0)) * 100
col1, col2, col3 = st.columns(3)
with col1: st.metric("Total Individuals", f"{total_individuals}")
with col2: st.metric("Right-Handed", f"{right_handed_percentage:.1f}%")
with col3: st.metric("Have Dimples", f"{dimples_percentage:.1f}%")

st.markdown("<br>", unsafe_allow_html=True)

# --- NEW: PERSONAL PROFILE CARD ---
st.markdown("### 👤 Personal Trait Profile")
person_name = st.selectbox("Select an individual to view their profile:", df['Name'].unique())
if person_name:
    person_data = df[df['Name'] == person_name].iloc[0]
    st.markdown(f"""
    <div class="profile-card">
        <div class="profile-name">{person_data['Name']}</div>
        <div class="trait-grid">
            <div class="trait-item"><span class="trait-label">Age:</span> {person_data['Age']}</div>
            <div class="trait-item"><span class="trait-label">Eye Colour:</span> {person_data['Eye Colour']}</div>
            <div class="trait-item"><span class="trait-label">Dimples:</span> {person_data['Dimples']}</div>
            <div class="trait-item"><span class="trait-label">Earlobe:</span> {person_data['Earlobe']}</div>
            <div class="trait-item"><span class="trait-label">Tongue Roll:</span> {person_data['Tongue Roll']}</div>
            <div class="trait-item"><span class="trait-label">Handedness:</span> {person_data['Handedness']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- TABS FOR ANALYSIS ---
tab1, tab2, tab3 = st.tabs(["🗃️ Dataset Explorer", "📈 Trait Analysis", "🔥 Correlation Analysis"])
# (All tab content remains the same as before)
with tab1:
    st.header("Full Dataset")
    def highlight_rows(row):
        if row[selected_trait] == selected_value:
            return ['background-color: #2575FC; color: white'] * len(row)
        return [''] * len(row)
    st.dataframe(df.style.apply(highlight_rows, axis=1), use_container_width=True, height=500)
with tab2:
    st.header("Detailed Summary for Each Trait")
    # (Age Histogram and Trait Expanders code remains the same)
    with st.expander("🎂 Analysis for: Age"):
        fig_hist = px.histogram(df, x="Age", nbins=8, title="Age Distribution of Individuals")
        st.plotly_chart(fig_hist, use_container_width=True)
    for trait in trait_options:
        with st.expander(f"🔬 Analysis for: **{trait}**"):
            #... (charting code is the same)
            counts = df[trait].value_counts()
            summary_df = pd.DataFrame({"Value": counts.index, "Count": counts.values}).reset_index(drop=True)
            col_chart1, col_chart2 = st.columns(2)
            with col_chart1:
                fig_bar = px.bar(summary_df, x="Value", y="Count", color="Value", title=f"Bar Chart: {trait}")
                st.plotly_chart(fig_bar, use_container_width=True)
            with col_chart2:
                fig_pie = px.pie(summary_df, names="Value", values="Count", title=f"Pie Chart: {trait}", hole=0.3)
                st.plotly_chart(fig_pie, use_container_width=True)
with tab3:
    st.header("Correlation Heatmap")
    # (Correlation Heatmap code remains the same)
    df_corr = df.drop(columns=['S.No', 'Name']).copy()
    for col in df_corr.columns:
        if df_corr[col].dtype == 'object':
            df_corr[col] = df_corr[col].astype('category').cat.codes
    corr = df_corr.corr()
    fig_heatmap = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r', title="Feature Correlation Heatmap")
    st.plotly_chart(fig_heatmap, use_container_width=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align:center; color:grey;'>👨‍💻 Created by Shreyas Sahoo</div>", unsafe_allow_html=True)
