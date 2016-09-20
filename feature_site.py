import csv
import numpy as np

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
variancia_amostra = np.var(y)
desvio_padrao_amostra = np.sqrt(variancia_amostra)
print("\nMédia da amostra:", media_amostra)
print("Variância da amostra:", variancia_amostra)
print("Desvio padrão da amostra", desvio_padrao_amostra)
print("Tamanho da amostra:", tamanho_amostra)

#hipotese 0: media populacional é igual 1.9983
#hipotese 1: media populacional é diferente de 1.9983


def calcula_z(media_populacao, desvio_padrao_populacao, media_amostra, tamanho_amostra):
    numerador = (media_amostra - media_populacao)
    denominador = (desvio_padrao_populacao/tamanho_amostra)
    return numerador/denominador

z = calcula_z(media_populacao, desvio_padrao_populacao, media_amostra, tamanho_amostra)
alfa = 0.05

