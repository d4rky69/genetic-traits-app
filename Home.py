import streamlit as st
import pandas as pd
import plotly.express as px
import random

from utils.pdf_export import add_pdf_export, load_css

st.set_page_config(
    page_title="Genetic Traits Projects Hub",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)
load_css()

if "project_choice" not in st.session_state:
    st.session_state["project_choice"] = None

if st.session_state["project_choice"] is None:
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 70vh;">
            <h1 style="font-size: 3rem; margin-bottom: 0.4em;">Welcome</h1>
            <div style="font-size: 1.23rem; color: #69738b; margin-bottom: 2.5em; text-align:center;">
                You have two projects available. Please choose one to explore.
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1,1], gap="large")
    with col1:
        dominant_clicked = st.button("Dominant Traits Analyzer →", key="dominant_real", use_container_width=True)
    with col2:
        genome_clicked = st.button("Human Genome Explorer →", key="genome_real", use_container_width=True)

    if dominant_clicked:
        st.session_state["project_choice"] = "dominant"
    elif genome_clicked:
        st.session_state["project_choice"] = "genome"

elif st.session_state["project_choice"] == "genome":
    st.switch_page("pages/3_🌐_Human_Genome_Explorer.py")

elif st.session_state["project_choice"] == "dominant":
    # (Insert your dashboard code here, as previously)
    @st.cache_data
    def generate_demo_data():
        names = ["Shreyas", "Arnab", "Aditya", "Arjun", "Krishna", "Rohan", "Ishaan", "Kunal", "Sanya", "Ananya", "Priya", "Kavya", "Ritika", "Nisha", "Meera", "Divya", "Rahul", "Amit", "Sneha", "Pooja",
                 "Rahul", "Tanvi", "Kabir", "Riya", "Anvi", "Aarav", "Aanya", "Vihaan", "Sara", "Om", "Neha", "Nitin", "Akash"]
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
            st.error(f"Error: The uploaded CSV must contain these columns: {', '.join(REQUIRED_COLS)}")
            st.stop()
        if 'S.No' not in df.columns:
            df.insert(0, 'S.No', range(1, 1 + len(df)))
    else:
        df = generate_demo_data()

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
                <div class="trait-item"><span class="trait-label">Age:</span><span class="trait-value">{person_data['Age']}</span></div>
                <div class="trait-item"><span class="trait-label">Eye Colour:</span><span class="trait-value">{person_data['Eye Colour']}</span></div>
                <div class="trait-item"><span class="trait-label">Dimples:</span><span class="trait-value">{person_data['Dimples']}</span></div>
                <div class="trait-item"><span class="trait-label">Earlobe:</span><span class="trait-value">{person_data['Earlobe']}</span></div>
                <div class="trait-item"><span class="trait-label">Tongue Roll:</span><span class="trait-value">{person_data['Tongue Roll']}</span></div>
                <div class="trait-item"><span class="trait-label">Handedness:</span><span class="trait-value">{person_data['Handedness']}</span></div>
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
                col1, col2 = st.columns(2)
                with col1:
                    fig_bar = px.bar(summary_df, x="Value", y="Count", color="Value", title=f"Bar Chart: {trait}")
                    st.plotly_chart(fig_bar, use_container_width=True)
                with col2:
                    fig_pie = px.pie(summary_df, names="Value", values="Count", title=f"Pie Chart: {trait}", hole=0.3)
                    st.plotly_chart(fig_pie, use_container_width=True)
    with tab3:
        st.header("Correlation Heatmap")
        df_corr = df.drop(columns=['S.No', 'Name']).copy()
        for col in df_corr.columns:
            if df_corr[col].dtype == 'object':
                df_corr[col] = df_corr[col].astype('category').cat.codes
        corr = df_corr.corr()
        fig_heatmap = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r', title="Feature Correlation Heatmap")
        st.plotly_chart(fig_heatmap, use_container_width=True)

    st.markdown("<div style='text-align:center; color:grey; padding-top: 2rem;'>👨‍💻 Created by Shreyas Sahoo</div>", unsafe_allow_html=True)
