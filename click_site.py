import csv

with open('data/amostra_A_click.csv', 'r') as arquivo:
    data = csv.reader(arquivo, delimiter=";")

    amostra_a_observada = [0, 0, 0]

    for line in data:
        if line[1] == 'yes':
            amostra_a_observada[0] += 1
        elif line[1] == 'no':
            amostra_a_observada[1] += 1

    amostra_a_observada[2] = amostra_a_observada[0] + amostra_a_observada[1]
    print(amostra_a_observada)

with open('data/amostra_B_click.csv', 'r') as arquivo:
    data = csv.reader(arquivo, delimiter=";")

    amostra_b_observada = [0, 0, 0]

    for line in data:
        if line[1] == 'yes':
            amostra_b_observada[0] += 1
        elif line[1] == 'no':
            amostra_b_observada[1] += 1

    amostra_b_observada[2] = amostra_b_observada[0] + amostra_b_observada[1]
    print(amostra_b_observada)

tabela_observada = []
tabela_observada.append(amostra_a_observada)
tabela_observada.append(amostra_b_observada)
terceira_linha = [amostra_a_observada[0]+ amostra_b_observada[0], amostra_a_observada[1] + amostra_b_observada[1], amostra_a_observada[2] + amostra_b_observada[2]]
tabela_observada.append(terceira_linha)

print(tabela_observada)

tabela_esperada = []
tabela_esperada_0_0 = (tabela_observada[0][2] * tabela_observada[2][0]) / tabela_observada[2][2]
tabela_esperada_0_1 = (tabela_observada[0][2] * tabela_observada[2][1]) / tabela_observada[2][2]
tabela_observada_1_0 = (tabela_observada[1][2] * tabela_observada[2][0]) / tabela_observada[2][2]
tabela_observada_1_1 = (tabela_observada[1][2] * tabela_observada[2][1]) / tabela_observada[2][2]

tabela_esperada = [[tabela_esperada_0_0, tabela_esperada_0_1], [tabela_observada_1_0, tabela_observada_1_1]]
print(tabela_esperada)

# graus de liberdade: (c-1)(r-1) => (2-1)(2-1) => 1
# alfa = 0.05

def calcula_qui_quadrado(tabela_observada, tabela_esperada):
    qui_quadrado = 0
    for i in range(2):
        for j in range(2):
            qui_quadrado += ((tabela_observada[i][j] - tabela_esperada[i][j]) ** 2) / tabela_esperada[i][j]
    return qui_quadrado

qui_quadrado = calcula_qui_quadrado(tabela_observada,tabela_esperada)
print(qui_quadrado)

# 13.293900961620135