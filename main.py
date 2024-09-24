import streamlit as st

## --- PAGE SETUP ---
sobre = st.Page(
    page="views/sobre.py",
    title="Sobre o Projeto",
    icon=":material/import_contacts:"
)

dados_cnes = st.Page(
    page="views/dados_cnes.py",
    title="Dados Cnes",
    icon=":material/bar_chart:"
)

dashboard = st.Page(
    page="views/dashboard.py",
    title="Dashboard",
    icon=":material/dashboard:"
)

### --- NAVIGATION ---
pg = st.navigation(pages={
    "Sobre": [sobre],
    "Projeto": [dados_cnes]
    })

### SHARED ON ALL PAGES ---
st.logo(r"assets\logo_cnes.png")
st.sidebar.text("Feito com Streamlit.")

### --- NAVIGATION ---
pg.run()