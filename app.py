import streamlit as st

pages = {
    "Tutorials": [
        st.Page("pages/tutorial_2.py", title="Uploading an extended invoice"),
        st.Page("pages/tutorial_4.py", title="Uploading and editing an invoice"),
    ],
    "Documentation": [
        st.Page("pages/document_wizard.py", title="Document Wizard"),
    ],
}

pg = st.navigation(pages)
pg.run()
