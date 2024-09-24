# Bibliotecas
import streamlit as st
import pandas as pd
import datetime
import os

### Define o datetime
today = datetime.date.today()
first = today.replace(day=1)
last_month = first - datetime.timedelta(days=1)
month = last_month.strftime('%m')

st.title('🎲 Dados CNES')

# Lê o arquivo json
json_data = pd.read_json(r'documentos\documentacao_cnes\json\relacao_tabelas.json')
json_data = json_data[json_data['nome_tabela_banco_prod_fed'].notna()]
list_of_tables = sorted(set([row['nome_tabela_banco_prod_fed'] for index, row in json_data.iterrows() if row['nome_tabela_banco_prod_fed'] != "-"]))
selected_file = st.selectbox("Selecione a tabela que deseja visualizar", options=list_of_tables)

desc_tabela = json_data[json_data['nome_tabela_banco_prod_fed'] == selected_file]["desc_tabela"].iloc[0]
tipo_tabelas = json_data[json_data['nome_tabela_banco_prod_fed'] == selected_file]["tipo_tabelas"].iloc[0]
nome_tabela_banco_local = json_data[json_data['nome_tabela_banco_prod_fed'] == selected_file]["nome_tabela_banco_local"].iloc[0]

st.subheader("Metadados:")
st.info(f"""
    Os dados abaixos são extraídos do arquivo disponibilizado pelo DataSUS no endereço **https://cnes.datasus.gov.br/pages/downloads/documentacao.jsp**, como nome do arquivo **Dicionário de Dados do SCNES**, com data de última atualização de **18/06/2024**.
""", icon="💡")

with st.container(border=True):
    st.markdown(f"**Descrição da Tabela:** {desc_tabela}")
    st.markdown(f"**Tipo da Tabela:** {tipo_tabelas}")
    st.markdown(f"**Nome da Tabela no Banco Local:** {nome_tabela_banco_local}")
try:
    df = pd.read_csv(fr"documentos/documentacao_cnes/{nome_tabela_banco_local}.csv", sep=';')
    st.dataframe(df, hide_index=True, use_container_width=True)
except FileNotFoundError:
    st.error(f"Erro: Arquivo '{selected_file}' não encontrado no caminho.", icon="🚨")
except PermissionError:
    st.error(f"Permissão negada: Não foi possível abrir o arquivo '{selected_file}'.", icon="🚨")
except Exception as e:
    st.error(f"Erro encontrado ao selecionar o arquivo '{selected_file}': {str(e)}", icon="🚨")

st.subheader("Tabela de Dados:")
st.info(f"""
    Os dados abaixo trazem informações da tabela **{selected_file}** do mês **{month}/{last_month.year}**.
""", icon="💡")

def normaliza_nome_tbl(nome_tbl: str):

    # Mapping para replacements de caracteres especiais
    replacements = {
        'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c'
    }
    
    translation_table = str.maketrans(replacements)
    str_nome_normalizado = f"{nome_tbl.lower().translate(translation_table).replace("_", "")}{last_month.year}{month}"
    
    return str_nome_normalizado

try:
    str_selected_file_corrected = normaliza_nome_tbl(selected_file)

    # Lista todos os arquivos no diretório
    direct_path_ftp_csv_tbls = fr'documentos\FTP-CNES-Files\Arquivos extraídos\BASE_DE_DADOS_CNES_{last_month.year}{month}'

    files = os.listdir(direct_path_ftp_csv_tbls)

    # Encontra o arquivo que há match e construí o nome (case-insensitive)
    matching_file = None
    for file in files:
        
        if file.lower() == f"{str_selected_file_corrected}.csv":
            matching_file = file
            break
    
    if matching_file == None:
        raise FileNotFoundError("Tabela não existe no diretório.")
    
    with st.spinner("Carregando arquivo..."):
        df = pd.read_csv(os.path.join(direct_path_ftp_csv_tbls, matching_file), encoding="latin1", sep=';', dtype=str, engine="pyarrow")
        
    col1, col2 = st.columns(2)
    
    with col1:
        options_column_filtro = ["-"] + list(df.columns)
        select_column_filter = st.selectbox("Filtrar tabela pela coluna:", options=options_column_filtro)
    with col2:
        if select_column_filter != "-":
            options_dado_filtro = ["-"] + list(set(df[select_column_filter]))
        else:
            options_dado_filtro = None
        select_value_filter = st.selectbox("Filtrar tabela pelo dado:", options=options_dado_filtro)

    if select_value_filter != "-" and select_value_filter != None:
        df = df[df[select_column_filter] == select_value_filter]
        
    st.dataframe(df, hide_index=True, use_container_width=True)


except FileNotFoundError:
    st.error(f"Erro: Arquivo '{str_selected_file_corrected}' não encontrado no caminho.", icon="🚨")
except PermissionError:
    st.error(f"Permissão negada: Não foi possível abrir o arquivo '{str_selected_file_corrected}'.", icon="🚨")
except Exception as e:
    st.error(f"Erro encontrado ao selecionar o arquivo '{str_selected_file_corrected}': {str(e)}", icon="🚨")