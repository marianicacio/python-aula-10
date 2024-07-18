#criar uma tabela em python e mandar para excel
import pandas as pd
import numpy as np

col = "Prova01 Prova02 Prova03 Prova04".split()
lin = "Beatriz Bianca Bianca Caio Claudemir Daniel Deivid Douglas Emerson Erika Euclides Fabio Fabricio Fernando Floriano Gary Guilherme Gustavo Henrique Jessica Juan Kauê Lucas Luciano Duda Matheus Miriam Sabrina".split()
notas = np.random.randint(1,11,112).reshape(28,4)
print(notas)

dados = pd.DataFrame(data =notas,index=lin,columns=col)
print(dados)

dados.to_excel("Notas_TurmaPython.xlsx")