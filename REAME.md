# 📊 DataOps Mini Lab

## 🧩 Sobre o projeto

Este projeto implementa um pipeline de dados simples com o objetivo de simular um cenário real de ingestão e análise inicial de dados.

O contexto é de uma empresa que recebe diariamente arquivos CSV contendo pedidos. Esses dados são carregados em uma base analítica local para possibilitar consultas e agregações.

Este laboratório serve como base para evolução incremental com práticas de DataOps, como rastreabilidade, versionamento, governança e qualidade de dados.

---

## ⚙️ O que o pipeline faz

O pipeline realiza as seguintes etapas:

- Leitura de um arquivo CSV contendo pedidos  
- Validação da existência do arquivo de entrada  
- Carregamento dos dados em memória com pandas  
- Criação de uma tabela no DuckDB  
- Tipagem explícita das colunas  
- Persistência dos dados no banco local  
- Execução de uma agregação por status dos pedidos  

---

## 📁 Estrutura do projeto

dataops-mini-lab/
├── data/
│ ├── raw/ # Dados brutos (entrada)
│ └── curated/ # Dados tratados (futuro)
├── ingestion/ # Scripts de ingestão
├── docs/ # Documentação
├── warehouse/ # Banco DuckDB
├── .gitignore


---

## 🛠️ Tecnologias utilizadas

- Python  
- pandas  
- DuckDB  
- Git  

---

## 📊 Saída esperada

O pipeline gera uma tabela analítica (`raw_orders`) no DuckDB e retorna uma agregação com:

- quantidade de pedidos por status  
- valor total por status  

---

## 🔮 Evolução do projeto

Este projeto foi estruturado para evoluir com práticas de engenharia de dados modernas, incluindo:

- Data lineage  
- Testes de qualidade  
- Camadas de dados (raw → curated)  
- Versionamento de dados  
- Contratos de dados  
- Orquestração de pipelines  