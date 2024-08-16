import streamlit as st

# Define page structure
pg = st.navigation(
    [
        st.Page("widgets/recommendations.py", title="Rekomendacje")
    ],
    position="hidden"
)

st.set_page_config(
    page_title='Jaki Laptop',
    layout='wide'
)
pg.run()
