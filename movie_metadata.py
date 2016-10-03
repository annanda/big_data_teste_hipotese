import csv

with open('data/movie_metadata.csv', 'r') as arquivo:
    data = csv.reader(arquivo, delimiter=",")

    dados = []

    for i, line in enumerate(data):
        if i != 0:
            dados.append([line[15], line[25]])

