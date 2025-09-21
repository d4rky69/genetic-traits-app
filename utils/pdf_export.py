import streamlit as st

def add_pdf_export():
    pdf_generation_script = """
        <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
        <script>
            function exportPageToPDF() {
                const element = document.querySelector('[data-testid="stAppViewContainer"]');
                html2canvas(element, {
                    onclone: function (document) {
                        document.body.style.background = '#0E1117';
                    }
                }).then(canvas => {
                    const imgData = canvas.toDataURL('image/png');
                    const pdf = new jspdf.jsPDF({
                        orientation: 'portrait',
                        unit: 'px',
                        format: [canvas.width, canvas.height]
                    });
                    pdf.addImage(imgData, 'PNG', 0, 0, canvas.width, canvas.height);
                    pdf.save("genetic-traits-dashboard.pdf");
                });
            }
        </script>
    """

    download_button_html = f"""
        <div style="text-align: center; padding-top: 1rem;">
            <button onclick="exportPageToPDF()" style="
                background: linear-gradient(90deg, #6A11CB 0%, #2575FC 100%);
                color: white;
                border: none;
                padding: 12px 24px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                font-weight: bold;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 12px;
                transition: all 0.3s ease-in-out;
            ">
                Download Page as PDF
            </button>
        </div>
        {pdf_generation_script}
    """
    
    st.sidebar.markdown(download_button_html, unsafe_allow_html=True)
