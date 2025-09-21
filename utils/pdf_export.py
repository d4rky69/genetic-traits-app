import streamlit as st

def load_css():
    """Loads the app's custom CSS for the futuristic glassmorphism theme."""
    st.markdown("""
    <style>
    /* Keyframes for Aurora Background & Animations */
    @keyframes aurora { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    @keyframes fadeInUp { 0% { opacity: 0; transform: translateY(20px); } 100% { opacity: 1; transform: translateY(0); } }

    /* Main App Styling */
    .stApp {
        background: linear-gradient(125deg, #0D0520, #241A4D, #0D0520);
        background-size: 400% 400%;
        animation: aurora 15s ease infinite;
    }

    /* Glassmorphism Effect for containers */
    [data-testid="stMetric"], [data-testid="stSidebar"], .profile-card, .stTabs, [data-testid="stExpander"] {
        background: rgba(44, 44, 77, 0.5) !important;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        animation: fadeInUp 0.5s ease-out forwards;
    }

    /* Text Color Fixes */
    .stApp, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label, .stMarkdown, [data-testid="stExpander"] p {
        color: #E0E0E0;
    }
    h1, h2, h3, h4, h5, h6 { color: #FFFFFF; }
    [data-testid="stSelectbox"] label { color: white !important; }

    /* Tab Styling Fixes */
    .stTabs [data-baseweb="tab"] { background-color: transparent; color: #AAAAAA; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #FFFFFF; border-bottom: 2px solid #2575FC; }

    /* Hover Animations */
    [data-testid="stMetric"]:hover, .profile-card:hover {
        transform: scale(1.03);
        box-shadow: 0 12px 40px 0 rgba(37, 117, 252, 0.5);
        border: 1px solid rgba(37, 117, 252, 0.8);
    }
    [data-testid="stMetric"]:nth-of-type(1) { animation-delay: 0.1s; }
    [data-testid="stMetric"]:nth-of-type(2) { animation-delay: 0.2s; }
    [data-testid="stMetric"]:nth-of-type(3) { animation-delay: 0.3s; }

    /* Profile Card Centering Fix */
    .profile-card { animation-delay: 0.4s; }
    .profile-name { font-size: 2rem; font-weight: 600; color: #FFFFFF; margin-bottom: 1rem; }
    .trait-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem; color: #D1D1E0; }
    .trait-item {
        background-color: rgba(0, 0, 0, 0.2); padding: 1rem; border-radius: 10px;
        display: flex; justify-content: center; align-items: center; text-align: center;
    }
    .trait-label { font-weight: 600; color: #69b3f2; padding-right: 0.5rem; }
    .trait-value { color: #FFFFFF; }
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
