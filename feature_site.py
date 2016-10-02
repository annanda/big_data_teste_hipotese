import csv
import numpy as np
import math

with open('data/populacao_tempo.csv', 'r') as arquivo:
    data = csv.reader(arquivo, delimiter=";")

    dados_populacao = []

    for i, line in enumerate(data):
        if i is not 0:
            dados_populacao.append(line[1])

with open('data/amostra_tempo.csv', 'r') as arquivo_2:
    data = csv.reader(arquivo_2, delimiter=';')

    dados_amostra = []

    for i, line in enumerate(data):
        if i is not 0:
            dados_amostra.append(line[1])

x = np.array(dados_populacao, dtype='f')
y = np.array(dados_amostra, dtype='f')
tamanho_amostra = len(y)

media_populacao = np.mean(x)
variancia_populacao = np.var(x)
desvio_padrao_populacao = np.sqrt(variancia_populacao)
print("Média:", media_populacao)
print("Variância:", variancia_populacao)
print("Desvio padrão", desvio_padrao_populacao)

media_amostra = np.mean(y)
print("\nMédia da amostra:", media_amostra)


#hipotese 0: media populacional é igual 1.9983
#hipotese 1: media populacional é diferente de 1.9983
#alfa = 0.05
# isso faz z = 1.96
z = 1.96


def calcula_desvio_padrao_amostra(desvio_padrao_populacao, tamanho_amostra):
    return desvio_padrao_populacao/math.sqrt(tamanho_amostra)


def calcula_x_critico(z, desvio_padrao_amostral, mi):
    x_critico = z * desvio_padrao_amostral
    x_critico += mi
    return x_critico

desvio_padrao_amostral = calcula_desvio_padrao_amostra(desvio_padrao_populacao, tamanho_amostra)
x_critico = calcula_x_critico(z, desvio_padrao_amostral, media_populacao)

print("x crítico", x_critico)
