import csv
import numpy as np
from scipy import stats

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

correferencia, p_valor = stats.spearmanr(var_1, var_2)

print(correferencia)
print(p_valor)