# desafio-etl-python

# Pipeline ETL: Engenharia de Dados para Alertas de Risco de Crédito

Este repositório contém a implementação de um pipeline de **ETL (Extract, Transform, Load)** simplificado e resiliente utilizando **Python** puro. O objetivo do projeto é simular o fluxo industrial de processamento de dados financeiros, onde dados brutos de clientes são extraídos, passam por um motor de regras de negócio (Validação/Transformação) e são carregados em uma estrutura de dados de alta disponibilidade para consumo de sistemas de CRM ou auditoria.

---

## 🛠️ Arquitetura do Pipeline (Topologia do Fluxo)

O projeto foi desenhado seguindo a filosofia de **Data Plumbing** (Encanamento de Dados), focando na redução da entropia da informação e garantindo a integridade referencial dos dados ponta a ponta.

| Etapa | Operação | Descrição |
| :--- | :--- | :--- |
| **Extract** | Leitura de Arquivo Bruto | Extração de registros a partir de um arquivo `clientes_banco.csv` usando dicionários nativos do Python. |
| **Transform** | Motor de Regras | Processamento do *Score de Crédito* de cada cliente, tomada de decisão algorítmica e geração de mensagens customizadas de CRM. |
| **Load** | Persistência Hierárquica | Carregamento e salvamento dos dados refinados em formato estruturado `alertas_clientes.json`, pronto para consumo via API. |

---

## 🚀 Tecnologias Utilizadas

*   **Python 3.x** (Ambiente de execução e manipulação de tipos)
*   **Biblioteca `csv`** (Manipulação de arquivos de dados tabulares estruturados)
*   **Biblioteca `json`** (Serialização de objetos para formato semiestruturado)
*   **Biblioteca `os`** (Interação com o sistema de arquivos para automação de setup)

---

## 🖥️ Como Executar o Projeto

Como o pipeline foi desenvolvido utilizando exclusivamente a biblioteca padrão do Python, **não é necessária a instalação de dependências externas**.

1. Clone o repositório ou execute diretamente via GitHub Codespaces.
2. Execute o script principal:
   ```bash
   python pipeline_etl.py
   
```
3. O script criará automaticamente o arquivo `clientes_banco.csv` simulado na primeira execução, rodará o pipeline e gerará o arquivo final de saída `alertas_clientes.json`.

---

## 📊 Estrutura dos Dados de Saída (JSON)

O resultado final é um arquivo JSON plano e hierárquico que preserva a invariância de identidade dos registros e serve como o produto final do pipeline:

```json
[
    {
        "id_cliente": "1001",
        "conta": "99123-4",
        "mensagem_customizada": "Olá, Guilherme Santos! Seu excelente comportamento financeiro liberou um upgrade de limite. Confira no app!",
        "acao_crm": "OFERTAR_UPGRADE"
    }
]
```

---

> *"Talk is cheap. Show me the code."* — Linus Torvalds
