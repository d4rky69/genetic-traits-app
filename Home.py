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

# --- CSS with the alignment fix ---
st.markdown("""
<style>
/* --- Keyframes for Aurora Background --- */
@keyframes aurora {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
/* --- Keyframes for Fade-In Animation --- */
@keyframes fadeInUp {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}
/* --- Main App Styling --- */
.stApp {
    background: linear-gradient(125deg, #0D0520, #241A4D, #0D0520);
    background-size: 400% 400%;
    animation: aurora 15s ease infinite;
}
/* --- Glassmorphism Effect for Cards and Sidebar --- */
[data-testid="stMetric"],
[data-testid="stSidebar"],
.profile-card,
.stTabs,
[data-testid="stExpander"] {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.18);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    animation: fadeInUp 0.5s ease-out forwards;
}
/* --- Hover Animations --- */
[data-testid="stMetric"]:hover,
.profile-card:hover {
    transform: scale(1.03);
    box-shadow: 0 12px 40px 0 rgba(37, 117, 252, 0.5);
    border: 1px solid rgba(37, 117, 252, 0.8);
}
/* Staggered animation for metric cards */
[data-testid="stMetric"]:nth-of-type(1) { animation-delay: 0.1s; }
[data-testid="stMetric"]:nth-of-type(2) { animation-delay: 0.2s; }
[data-testid="stMetric"]:nth-of-type(3) { animation-delay: 0.3s; }

/* --- Profile Card Specifics --- */
.profile-card { animation-delay: 0.4s; }
.profile-name { font-size: 2rem; font-weight: 600; color: #FFFFFF; margin-bottom: 1rem; }
.trait-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem; color: #D1D1E0;
}
.trait-item {
    background-color: rgba(0, 0, 0, 0.2);
    padding: 1rem;
    border-radius: 10px;
    /* --- THIS IS THE FIX --- */
    display: flex;
    justify-content: center;
    align-items: center;
    /* ----------------------- */
}
.trait-label { font-weight: 600; color: #69b3f2; }

/* --- General Text & Title Styling --- */
h1, h2, h3 {
    color: #FFFFFF;
}
</style>
""", unsafe_allow_html=True)

# --- DATA LOADING LOGIC (Remains the same) ---
@st.cache_data
def generate_demo_data():
    names = ["Shreyas", "Arnab", "Aditya", "Arjun", "Krishna", "Rohan", "Ishaan", "Kunal", "Sanya", "Ananya", "Priya", "Kavya", "Ritika", "Nisha", "Meera", "Divya", "Rahul", "Amit", "Sneha", "Pooja", "Varun", "Neha", "Shreya", "Manish", "Akash", "Vikram", "Sunita", "Lakshmi", "Ramesh", "Deepak", "Geeta", "Ajay", "Suresh", "Anjali", "Swati"]
    data = [[i, name, random.randint(18, 25), random.choice(["Brown", "Black"]), random.choice(["Yes", "No"]), random.choice(["Free", "Attached"]), random.choice(["Yes", "No"]), random.choices(["Right", "Left", "Mixed"], weights=[0.89, 0.10, 0.01])[0]] for i, name in enumerate(names, 1)]
    fields = ["S.No", "Name", "Age", "Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Handedness"]
    return pd.DataFrame(data, columns=fields)

REQUIRED_COLS = {"Name", "Age", "Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Handedness"}

uploaded_file = st.sidebar.file_uploader("📂 Upload your own CSV data", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if not REQUIRED_COLS.issubset(df.columns):
        st.error(f"Error: The uploaded CSV must contain these columns: {', '.join(REQUIRED_COLS)}")
        st.stop()
    if 'S.No' not in df.columns:
        df.insert(0, 'S.No', range(1, 1 + len(df)))
else:
    df = generate_demo_data()

# --- SIDEBAR (Remains the same) ---
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

# --- MAIN PAGE (Content remains the same, but will adopt the new style) ---
st.title("🧬 Genetic Traits Dashboard")
st.markdown("An interactive dashboard to explore, visualize, and predict genetic traits.")

st.markdown("### 📊 Quick Stats")
total_individuals = len(df)
right_handed_percentage = (df['Handedness'].value_counts(normalize=True).get('Right', 0)) * 100
dimples_percentage = (df['Dimples'].value_counts(normalize=True).get('Yes', 0)) * 100
col1, col2, col3 = st.columns(3)
with col1: st.metric("Total Individuals", f"{total_individuals}")
with col2: st.metric("Right-Handed", f"{right_handed_percentage:.1f}%")
with col3: st.metric("Have Dimples", f"{dimples_percentage:.1f}%")

st.markdown("<br>", unsafe_allow_html=True)
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
tab1, tab2, tab3 = st.tabs(["🗃️ Dataset Explorer", "📈 Trait Analysis", "🔥 Correlation Analysis"])

with tab1:
    st.header("Full Dataset")
    def highlight_rows(row):
        if row[selected_trait] == selected_value:
            return ['background-color: #2575FC; color: white'] * len(row)
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
            col_chart1, col_chart2 = st.columns(2)
            with col_chart1:
                fig_bar = px.bar(summary_df, x="Value", y="Count", color="Value", title=f"Bar Chart: {trait}")
                st.plotly_chart(fig_bar, use_container_width=True)
            with col_chart2:
                fig_pie = px.pie(summary_df, names="Value", values="Count", title=f"Pie Chart: {trait}", hole=0.3)
                st.plotly_chart(fig_pie, use_container_width=True)
with tab3:
    st.header("Correlation Heatmap")
    st.markdown("Shows the relationship between traits. Values near 1 or -1 show a strong correlation.")
    df_corr = df.drop(columns=['S.No', 'Name']).copy()
    for col in df_corr.columns:
        if df_corr[col].dtype == 'object':
            df_corr[col] = df_corr[col].astype('category').cat.codes
    corr = df_corr.corr()
    fig_heatmap = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r', title="Feature Correlation Heatmap")
    st.plotly_chart(fig_heatmap, use_container_width=True)

st.markdown("---")
st.markdown("<div style='text-align:center; color:grey;'>👨‍💻 Created by Shreyas Sahoo</div>", unsafe_allow_html=True)
