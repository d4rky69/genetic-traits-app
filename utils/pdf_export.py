import streamlit as st
import base64

def add_pdf_export():
    """
    Adds a button to the sidebar to export the current page as a PDF.
    """
    # JavaScript to capture the page and generate PDF
    # We use html2canvas to render the page and jsPDF to create the PDF
    pdf_generation_script = """
        <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
        <script>
            function exportPageToPDF() {
                const element = document.querySelector('[data-testid="stAppViewContainer"]'); // Target the main Streamlit container
                
                // Use html2canvas to render the element
                html2canvas(element, {
                    onclone: function (document) {
                        // Make sure the background is not transparent
                        document.body.style.background = '#0E1117'; // Set to Streamlit dark theme background
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

    # Button to trigger the JavaScript function
    download_button_html = f"""
        <div style="text-align: center; padding-top: 1rem;">
            <button onclick="exportPageToPDF()" style="
                background-color: #FF4B4B;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 8px;
            ">
                Download Page as PDF
            </button>
        </div>
        {pdf_generation_script}
    """
    
    st.sidebar.markdown(download_button_html, unsafe_allow_html=True)
