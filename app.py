import streamlit as st

pages = {
    "Tutorials": [
        st.Page("pages/tutorial_1.py", title="Create your account"),
        st.Page("pages/tutorial_2.py", title="Manage your account"),
    ],
    "Documentation": [
        st.Page("pages/document_wizard.py", title="Document Wizard"),
    ],
}

pg = st.navigation(pages)
pg.run()
