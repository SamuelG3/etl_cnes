import streamlit as st


st.title("🏥 Sobre o Projeto:")
st.markdown("""
        O Cadastro Nacional de Estabelecimentos de Saúde (CNES) é uma base de dados que identifica e registra todos os estabelecimentos de saúde do Brasil, públicos e privados, e os profissionais que neles atuam.

        Os dados são disponibilizados mensalmente por FTP (File Transfer Protocol), e são de fácil acesso através do endereço https://cnes.datasus.gov.br/ .
        
        No entanto, devido à quantidade de dados e à complexidade relacional, os dados não são facilmente compreensíveis para indivíduos menos técnicos. Este projeto visa facilitar a visão macro do banco de dados, em vez da busca por CNPJ único, como disponível no site do Datasus, além de facilitar o entendimento dos metadados de todas as tabelas.        
""")