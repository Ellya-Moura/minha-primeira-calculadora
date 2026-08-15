# --- Nosso Primeiro Algoritmo em Python ---

def calcular_resumo_empresa():
    print("--- SISTEMA CONTÁBIL EXPRESS ---")
    
    # O programa pede os dados para o usuário
    faturamento = float(input("Digite o faturamento bruto da empresa (R$): "))
    custos = float(input("Digite os custos operacionais (R$): "))
    
    # A IA/Algoritmo faz as contas automaticamente
    imposto = faturamento * 0.06  # Simulando um imposto de 6% (Simples Nacional)
    lucro_liquido = faturamento - custos - imposto
    
    # O programa mostra o resultado na tela
    print("\n=== RESUMO FINANCEIRO ===")
    print(f"Faturamento: R$ {faturamento:,.2f}")
    print(f"Impostos (6%): R$ {imposto:,.2f}")
    print(f"Custos: R$ {custos:,.2f}")
    print(f"------------------------")
    print(f"Lucro Líquido: R$ {lucro_liquido:,.2f}")

# Executa o programa
calcular_resumo_empresa()
