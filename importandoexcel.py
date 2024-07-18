import pandas as pd
excel = pd.read_excel("aula.xlsx")

#variável mê para controlar o fluxo de venda dos meses
mes = input("Qual mês vc quer analisar?: ")

#retornar a analisa do que mais vendou no mês 
#ordena o mês
analise = excel.sort_values(by=f'{mes}',ascending=False)
print(analise)