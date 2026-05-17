import csv
import json
import os

# ==========================================
# 0. SETUP: Criando dados fictícios (CSV)
# ==========================================
def criar_dados_ficticios():
    dados = [
        ["ID", "Nome", "Conta", "Limite_Atual", "Score_Credito"],
        ["1001", "Guilherme Santos", "99123-4", "5000.00", "850"],
        ["1002", "Ana Silva", "99567-8", "1200.00", "420"],
        ["1003", "Carlos Souza", "99345-2", "8000.00", "950"]
    ]
    with open('clientes_banco.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(dados)

if not os.path.exists('clientes_banco.csv'):
    criar_dados_ficticios()


# ==========================================
# 1. EXTRACT (Extração)
# ==========================================
def extrair_dados(caminho_arquivo):
    print("🔋 [EXTRACT] Iniciando extração de dados do CSV...")
    clientes = []
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            clientes.append(linha)
    print(f"✔️ [EXTRACT] {len(clientes)} registros extraídos com sucesso.")
    return clientes


# ==========================================
# 2. TRANSFORM (Transformação)
# ==========================================
def transformar_dados(clientes):
    print("⚙️ [TRANSFORM] Aplicando regras de negócio e gerando insights...")
    notificacoes = []
    
    for c in clientes:
        score = int(c["Score_Credito"])
        nome = c["Nome"]
        limite = float(c["Limite_Atual"])
        
        # Simulação de uma decisão automatizada de IA/Modelo
        if score > 800:
            mensagem = f"Olá, {nome}! Seu excelente comportamento financeiro liberou um upgrade de limite. Confira no app!"
            acao = "OFERTAR_UPGRADE"
        elif score < 500:
            mensagem = f"Olá, {nome}. Identificamos oportunidades de otimização de gastos para melhorar sua saúde financeira."
            acao = "ALERTA_RISCO"
        else:
            mensagem = f"Olá, {nome}! Mantenha suas contas em dia e acompanhe suas metas no nosso painel."
            acao = "MANUTENCAO"
            
        notificacoes.append({
            "id_cliente": c["ID"],
            "conta": c["Conta"],
            "mensagem_customizada": mensagem,
            "acao_crm": acao
        })
        
    print("✔️ [TRANSFORM] Transformação concluída.")
    return notificacoes


# ==========================================
# 3. LOAD (Carregamento)
# ==========================================
def carregar_dados(dados_transformados, caminho_saida):
    print(f"💾 [LOAD] Salvando dados transformados em {caminho_saida}...")
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        json.dump(dados_transformados, f, indent=4, ensure_ascii=False)
    print("✔️ [LOAD] Pipeline executado com 100% de sucesso!")


# ==========================================
# EXECUÇÃO DO PIPELINE
# ==========================================
if __name__ == "__main__":
    # Executa o fluxo ponta a ponta
    dados_brutos = extrair_dados('clientes_banco.csv')
    dados_processados = transformar_dados(dados_brutos)
    carregar_dados(dados_processados, 'alertas_clientes.json')
