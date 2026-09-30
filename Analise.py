# Exemplo simples de script em Python para o Projeto 1 da EBAC
# Este script simula a leitura e o tratamento de dados de vendas

print("Iniciando a leitura dos dados...")

# Lista de dados fictícios simulando uma base de dados
vendas = [
    {"produto": "Notebook", "categoria": "Eletrônicos", "preco": 3500, "quantidade": 2},
    {"produto": "Mouse", "categoria": "Eletrônicos", "preco": 150, "quantidade": 5},
    {"produto": "Cadeira", "categoria": "Móveis", "preco": 800, "quantidade": 1}
]

# Calculando o faturamento total por item
print("\nProcessando faturamento dos produtos:")
faturamento_total = 0

for item in vendas:
    total_item = item["preco"] * item["quantidade"]
    faturamento_total += total_item
    print(f"- {item['produto']}: R$ {total_item}")

print(f"\nFaturamento Geral da Loja: R$ {faturamento_total}")
print("Processamento concluído com sucesso!")