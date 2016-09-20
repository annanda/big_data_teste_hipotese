import csv
import numpy as np

with open('data/populacao_tempo.csv', 'r') as arquivo:
    data = csv.reader(arquivo, delimiter=";")

    dados = []

    for i, line in enumerate(data):
        if i is not 0:
            dados.append(line[1])

    x = np.array(dados, dtype='f')

    media_populacao = np.mean(x)
    variancia_populacao = np.var(x)
    desvio_padrao_populacao = np.sqrt(variancia_populacao)
    print("Média:", media_populacao)
    print("Variância:", variancia_populacao)
    print("Desvio padrão", desvio_padrao_populacao)

    
