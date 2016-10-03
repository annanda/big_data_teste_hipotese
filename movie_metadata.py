import csv
import math
import numpy as np
from scipy import stats
import pylab as pl

with open('data/movie_metadata.csv', 'r') as arquivo:
    data = csv.reader(arquivo, delimiter=",")

    var_1 = []
    var_2 = []

    for i, line in enumerate(data):
        if i != 0:
            if line[15] != '':
                var_1.append(line[15])
            else:
                var_1.append('0')

            var_2.append(line[25])


var_1 = np.array(var_1, dtype='f')
var_2 = np.array(var_2, dtype='f')
tamanho_amostra = len(var_1)

coeficiente, p_valor = stats.spearmanr(var_1, var_2)


def significancia_spearman(coeficiente, tamanho_amostra):
    denominador = math.sqrt((1 - coeficiente ** 2) / (tamanho_amostra - 2))
    significancia = coeficiente / denominador
    return significancia

print(coeficiente)
print(p_valor)
print(tamanho_amostra)
print(significancia_spearman(coeficiente, tamanho_amostra))



h = sorted([186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
     187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
     161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180])  #sorted

fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed

pl.plot(var_1,'o', color="red")
pl.plot(var_2, 'o', color="blue")

# pl.hist(h,normed=True)      #use this to draw histogram of your data

pl.show()