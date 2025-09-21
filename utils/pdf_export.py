import streamlit as st

def add_pdf_export():
    # This version loads the scripts from jsdelivr.net, which is less commonly blocked.
    pdf_generation_script = """
        <script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/jspdf@2.5.1/dist/jspdf.umd.min.js"></script>
        <script>
            function exportPageToPDF() {
                const element = document.querySelector('[data-testid="stAppViewContainer"]');
                if (!element) {
                    alert("Error: Could not find the main app container to export.");
                    return;
                }
                
                window.html2canvas(element, {
                    onclone: function (document) {
                        document.body.style.background = '#0E1117';
                    },
                    useCORS: true
                }).then(canvas => {
                    const { jsPDF } = window.jspdf;
                    const pdf = new jsPDF({
                        orientation: 'portrait',
                        unit: 'px',
                        format: [canvas.width, canvas.height]
                    });
                    pdf.addImage(canvas.toDataURL('image/png'), 'PNG', 0, 0, canvas.width, canvas.height);
                    pdf.save("genetic-traits-dashboard.pdf");
                }).catch(err => {
                    alert("An error occurred while generating the PDF. See the browser console for details.");
                    console.error("Error during PDF generation:", err);
                });
            }

            // Use a timeout to ensure Streamlit has rendered the button before attaching the listener
            setTimeout(() => {
                const pdfButton = document.getElementById('export-pdf-button');
                if (pdfButton) {
                    pdfButton.addEventListener('click', exportPageToPDF);
                }
            }, 1500); // 1.5 second delay
        </script>
    """

    download_button_html = f"""
        <div style="text-align: center; padding-top: 1rem;">
            <button id="export-pdf-button" style="
                background: linear-gradient(90deg, #6A11CB 0%, #2575FC 100%);
                color: white; border: none; padding: 12px 24px; text-align: center;
                text-decoration: none; display: inline-block; font-size: 16px;
                font-weight: bold; margin: 4px 2px; cursor: pointer; border-radius: 12px;
                transition: all 0.3s ease-in-out;
            ">
                Download Page as PDF
            </button>
        </div>
        {pdf_generation_script}
    """
    
    st.sidebar.markdown(download_button_html, unsafe_allow_html=True)
