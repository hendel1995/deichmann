import streamlit as st

import streamlit as st

st.set_page_config(page_title="Document Wizard", page_icon="📄")

st.title("📄 Document Wizard")

st.write("The 'Document Wizard' window contains:")

st.markdown(
    """
    - 📘 **An icon** for manually opening the **'User Manual', 'eDocs Portal'**, or **'Invoice Portal'** (blue frame)
    - 🔵 **Information** about the files that can be uploaded (marked in blue)
    - 🟢 **An area** for uploading files (marked in green)
    - 🟠 **Links** for exporting CSV/Excel files, with and without sample data (marked in orange)
    """
)

st.header("📂 Uploadable Files in 'Document Wizard'")

st.subheader("1. Invoice-CSV")
st.write("Contains invoice data without documents. See 'Creating an Invoice-CSV' for details.")

st.subheader("2. Extended Invoice-CSV")
st.write("Contains invoice data with associated documents. See 'Creating an Extended Invoice-CSV'.")

st.subheader("3. Document-CSV")
st.write("Contains documents with necessary additional information. See 'Creating a Document-CSV'.")

st.subheader("4. Individual or Multiple Document PDFs")
st.write("Documents can be uploaded without a 'Document-CSV'. See 'Uploading Documents (PDF files)'.")

st.header("📦 Uploading ZIP Files")
st.write(
    "If you want to send documents with an 'Extended Invoice-CSV' or a 'Document-CSV', "
    "you must compress the CSV files along with the related PDFs into a ZIP file before uploading. "
    "See 'Creating a ZIP file' for more details."
)

st.header("📌 Additional Notes")
st.write(
    "- Ensure that file names comply with the conventions described in 'File names of CSV files'.\n"
    "- After uploading a file, you will be redirected to either the 'eDocs Portal' or the 'Invoice Portal'.\n"
    "- All functionalities are detailed in the 'User Manual'."
)


