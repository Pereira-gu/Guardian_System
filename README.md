# 🛡️ Guardian System - Endpoint Monitoring & Analysis

O **Guardian System** é um sistema de monitorização de segurança modular desenvolvido para detetar e analisar processos em execução no Windows, atribuindo scores de risco e visualizando telemetria em tempo real.

## 🚀 Funcionalidades
- **Coleta Automatizada:** Monitorização de processos via `psutil`.
- **Análise de Risco:** Motor de regras que identifica processos suspeitos (ex: PowerShell com privilégios).
- **Pipeline de Dados:** Ingestão de dados em SQLite com tratamento de duplicados.
- **Visualização BI:** Dashboard interativo em Power BI conectado via ODBC/Python.

## 📊 Dashboard (v1.0)
*(Aqui você deve tirar um print do seu dashboard no Power BI, guardar na pasta do projeto e linkar assim:)*
![Dashboard Screenshot](img/Screenshot%202026-02-27%20191414.png)

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Base de Dados:** SQLite
- **Business Intelligence:** Power BI (ODBC Driver)
- **Bibliotecas:** `psutil`, `pandas`, `sqlite3`

## ⚙️ Como Executar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt