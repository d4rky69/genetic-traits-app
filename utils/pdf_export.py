import streamlit as st

def load_css():
    """Loads the app's custom CSS for the futuristic glassmorphism theme."""
    st.markdown("""
    <style>
        /* Aurora animation */
    @keyframes aurora { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    @keyframes fadeInUp { 0% { opacity: 0; transform: translateY(20px); } 100% { opacity: 1; transform: translateY(0); } }

    /* Main background */
    .stApp {
        background: linear-gradient(125deg, #0D0520, #241A4D, #0D0520);
        background-size: 400% 400%;
        animation: aurora 15s ease infinite;
    }

    /* Glassmorphism containers */
    [data-testid="stMetric"], [data-testid="stSidebar"], .profile-card, .stTabs, [data-testid="stExpander"] {
        background: rgba(44,44,77,0.5) !important;
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 0 8px 32px 0 rgba(0,0,0,0.37);
        animation: fadeInUp 0.5s ease-out forwards;
    }

    /* Metric Box Alignment */
    [data-testid="stMetric"] {
        min-height: 110px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start; /* top-align */
        align-items: flex-start;      /* left-align */
        padding: 18px 24px;
        gap: 0.5em;
        box-sizing: border-box;
    }
    [data-testid="stMetricLabel"] {
        font-size: 1.15rem;
        font-weight: 500;
        color: #B8C6E5 !important;
        margin-bottom: 0.4em;
        letter-spacing: 0.01em;
        text-align: left;
        width: 100%;
    }
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 700;
        color: #FFFFFF !important;
        line-height: 1.1;
        width: 100%;
        text-align: left;
    }

    /* Sidebar header and label alignment */
    .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5 {
        text-align: left;
        margin-bottom: 0.3em;
    }
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] .stRadio label, [data-testid="stSidebar"] .stSelectbox label {
        color: #E0E0E0 !important;
        text-align: left !important;
        font-weight: 500 !important;
    }
    [data-testid="stSidebar"] .stRadio, [data-testid="stSidebar"] .stSelectbox {
        margin-bottom: 0.7em;
    }

    /* General text fixes */
    .stApp, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label, .stMarkdown, [data-testid="stExpander"] p {
        color: #E0E0E0;
    }
    h1, h2, h3, h4, h5, h6 { color: #FFFFFF; }
    [data-testid="stSelectbox"] label { color: white !important; }

    /* Tab Styling */
    .stTabs [data-baseweb="tab"] { background-color: transparent; color: #AAAAAA; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #FFFFFF; border-bottom: 2px solid #2575FC; }

    /* Hover Animations */
    [data-testid="stMetric"]:hover, .profile-card:hover {
        transform: scale(1.03);
        box-shadow: 0 12px 40px 0 rgba(37,117,252,0.5);
        border: 1px solid rgba(37,117,252,0.8);
    }
    [data-testid="stMetric"]:nth-of-type(1) { animation-delay: 0.1s; }
    [data-testid="stMetric"]:nth-of-type(2) { animation-delay: 0.2s; }
    [data-testid="stMetric"]:nth-of-type(3) { animation-delay: 0.3s; }

    /* Profile Card Section */
    .profile-card { animation-delay: 0.4s; padding: 1.2em 2em; }
    .profile-name { font-size: 2rem; font-weight: 600; color: #FFFFFF; margin-bottom: 1rem; }

    /* Trait grid and chips (profile card) */
    .trait-grid { 
        display: flex; 
        flex-wrap: wrap; 
        gap: 1em; 
        color: #D1D1E0; 
        margin-top: 0.3em;
    }
    .trait-item {
        background-color: rgba(0, 0, 0, 0.2); 
        padding: 0.75em 1.3em; 
        border-radius: 10px;
        display: flex; 
        justify-content: flex-start; /* left-align */
        align-items: center; 
        text-align: left;
        font-size: 1.08rem;
        font-family: inherit;
        min-width: 120px;
        margin-bottom: 0.1em;
        box-sizing: border-box;
    }
    .trait-label { font-weight: 700; color: #69b3f2; padding-right: 0.5rem; }
    .trait-value { color: #FFFFFF; }

    /* Personal Trait Profile section header */
    .stMarkdown h3 {
        display: flex;
        align-items: center;
        gap: 0.6em;
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        color: #FFFFFF !important;
        margin-bottom: 0.4em;
    }
    </style>
    """, unsafe_allow_html=True)

def add_pdf_export():
    pdf_generation_script = """
        <script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/jspdf@2.5.1/dist/jspdf.umd.min.js"></script>
        <script>
            function exportPageToPDF() {
                const element = document.querySelector('[data-testid="stAppViewContainer"]');
                html2canvas(element, { onclone: function (document) { document.body.style.background = '#0E1117'; }, useCORS: true })
                .then(canvas => {
                    const { jsPDF } = window.jspdf;
                    const pdf = new jsPDF({ orientation: 'portrait', unit: 'px', format: [canvas.width, canvas.height] });
                    pdf.addImage(canvas.toDataURL('image/png'), 'PNG', 0, 0, canvas.width, canvas.height);
                    pdf.save("genetic-traits-dashboard.pdf");
                });
            }
            setTimeout(() => {
                const pdfButton = document.getElementById('export-pdf-button');
                if (pdfButton) { pdfButton.addEventListener('click', exportPageToPDF); }
            }, 1500);
        </script>
    """
    download_button_html = f"""
        <div style="text-align: center; padding-top: 1rem;">
            <button id="export-pdf-button" style="
                background: linear-gradient(90deg, #6A11CB 0%, #2575FC 100%); color: white;
                border: none; padding: 12px 24px; text-align: center; font-size: 16px;
                font-weight: bold; cursor: pointer; border-radius: 12px;
            ">
                Download Page as PDF
            </button>
        </div>
        {pdf_generation_script}
    """
    st.sidebar.markdown(download_button_html, unsafe_allow_html=True)
