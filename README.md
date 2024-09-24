# Projeto ETL CNES - Dados Abertos do DATASUS

## Descrição
Este projeto realiza a extração, transformação e carga (ETL) dos dados do Cadastro Nacional de Estabelecimentos de Saúde (CNES) disponíveis na plataforma de dados abertos do DATASUS. O objetivo é coletar e processar esses dados mensalmente, proporcionando uma visão clara e acessível das informações sobre estabelecimentos de saúde no Brasil.

## Funcionalidades
- Extração: Coleta automatizada dos dados do CNES diretamente da fonte do DATASUS.
Transformação: Processamento dos dados para garantir a integridade e a qualidade das informações. Inclui limpeza, normalização e enriquecimento dos dados.
- Carga: Armazenamento dos dados transformados em um banco de dados para consulta e análise.
- Visualização: Aplicação interativa desenvolvida com Streamlit, permitindo a exploração dos dados em tempo real. Os usuários podem visualizar estatísticas, gráficos e realizar filtragens com facilidade.

## Tecnologias Utilizadas
- Python (Pandas, NumPy)
- Streamlit

## Como Usar
1. Clone este repositório.
2. Instale as dependências com pip install -r requirements.txt.
3. Configure as credenciais e as configurações do banco de dados.
4. Execute o script ETL para importar os dados.
5; Inicie a aplicação Streamlit com streamlit run main.py.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

### Licença
Este projeto está licenciado sob a MIT License.

Explore os dados do CNES e ajude a promover a transparência e o acesso à informação na área da saúde!
