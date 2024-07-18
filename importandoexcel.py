import pandas as pd
excel = pd.read_excel("vendedor.xlsx")

# Variável 'mês' para controlar o fluxo de venda dos meses
mes = input("Qual mês você quer analisar? ")

# Retornar análise do vendedor do mês
# Ordena o mês
analise = excel.sort_values(by=f'{mes}',ascending=False)
# Melhorando...
print(f"O melhor vendedor do mês {mes}, foi a {analise.iloc[0][0]}")

# Quem menos vendeu
analise = excel.sort_values(by=f'{mes}',ascending=True)
# ...
print(f"O pior vendedor do mês {mes}, foi a {analise.iloc[0][0]}")

# Só quero o vendedor, como ele está na primeira coluna: [0][0]
print(analise.iloc[0][0])