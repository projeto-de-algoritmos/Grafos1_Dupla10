nomes = {  # Linha Azul
    1: 'Reboleira', 2: 'Amadora Este', 3: 'Alfornelos', 4: 'Pontinha', 5: 'Carnide',
    6: 'Colégio Militar/Luz', 7: 'Alto dos Moinhos', 8: 'Laranjeiras', 9: 'Jardim Zoológico',
    10: 'Praça de Espanha', 11: 'S. Sebastião', 12: 'Parque', 13: 'Marquês de Pombal', 14: 'Avenida',
    15: 'Rossio', 16: 'Baixa-Chiado', 17: 'Terreiro do Paço', 18: 'Santa Apolónia',
    # Linha Amarela
    19: 'Odivelas', 20: 'Senhor Roubado',
    21: 'Ameixoeira', 22: 'Lumiar', 23: 'Quinta das conchas',
    24: 'Campo Grande', 25: 'Cidade Universitária', 26: 'Entre campos',
    27: 'Campo pequeno', 28: 'Saldanha', 29: 'Picoas', 30: 'Rato',
    # Linha Verde
    31: 'Telheiras', 32: 'Alvalade', 33: 'Roma', 34: 'Areeiro',
    35: 'Alameda', 36: 'Anjos', 37: 'Intendente', 38: 'Martin Moniz',
    39: 'Rossio (Verde)', 40: 'Cais do Sodré',
    # Linha Vermelha
    41: 'Aeroporto', 42: 'Encarnação', 43: 'Moscavide', 44: 'Oriente',
    45: 'Cabo Ruivo', 46: 'Olivais', 47: 'Chelas', 48: 'Bela Vista', 49: 'Olaias'
}

grafo={}
numVertices=0

def adcVertice(vertice):
    global grafo
    global numVertices
    numVertices += 1
    grafo[vertice] = []


def adcAresta(vertice1, vertice2):
    global grafo
    grafo[vertice1].append(vertice2)
    grafo[vertice2].append(vertice1)

def printGrafo(grafo):
    for node in grafo:
        print("{}: {}".format(node, grafo[node]))
    print(' ')  

for v in range(1,50):
    adcVertice(v)

for azul in range(1,18):
    adcAresta(azul, azul+1)

for amarelo in range(19,29):
    adcAresta(amarelo, amarelo+1)


adcAresta(29, 13)
adcAresta(13, 30)
adcAresta(31, 24)
adcAresta(24, 32)

for verde in range(32,39):
    adcAresta(verde, verde+1)

adcAresta(39, 16)
adcAresta(16, 40)

for vermelho in range(41,49):
    adcAresta(vermelho, vermelho+1)

adcAresta(49, 35)
adcAresta(35, 28)
adcAresta(28, 11)

printGrafo(grafo)