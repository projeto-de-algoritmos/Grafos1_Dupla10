import networkx as nx
import matplotlib.pyplot as plt


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

G=nx.Graph()
grafo = {}
numVertices = 0


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
        print('[{}] {}:'.format(node, nomes[node]), end=' ')
        for vizinho in grafo[node]:
            if vizinho != grafo[node][-1]:
                print('[{}] {}'.format(vizinho, nomes[vizinho]), end=' - ')
            else:
                print('[{}] {}'.format(vizinho, nomes[vizinho]))


for v in range(1, 50):
    G.add_node(v)
    adcVertice(v)

for azul in range(1, 18):
    G.add_edge(azul, azul+1)
    adcAresta(azul, azul+1)

for amarelo in range(19, 29):
    G.add_edge(amarelo, amarelo + 1)
    adcAresta(amarelo, amarelo+1)


adcAresta(29, 13)
G.add_edge(29,13)
adcAresta(13, 30)
G.add_edge(13,30)
adcAresta(31, 24)
G.add_edge(31,24)
adcAresta(24, 32)
G.add_edge(24,32)

for verde in range(32, 39):
    G.add_edge(verde, verde+1)
    adcAresta(verde, verde+1)

G.add_edge(39,16)
adcAresta(39, 16)
G.add_edge(16,40)
adcAresta(16, 40)

for vermelho in range(41, 49):
    G.add_edge(vermelho, vermelho+1)
    adcAresta(vermelho, vermelho+1)

adcAresta(49, 35)
G.add_edge(49,35)
adcAresta(35, 28)
G.add_edge(35,28)
adcAresta(28, 11)
G.add_edge(28,11)


def distBFS(inicio, destino):
    global grafo
    fila = []
    visitados = {}
    for node in grafo:
        visitados[node] = False
    visitados[inicio] = True
    dist = {inicio: 0}
    fila.append(inicio)
    while fila:
        atual = fila.pop(0)
        for i in grafo[atual]:
            if not visitados[i]:
                visitados[i] = True
                dist[i] = dist[atual]+1
                fila.append(i)
    try:
        return dist[destino]
    except:
        return None


def printCaminho(inicio, destino):
    global grafo
    fila = []
    visitados = {}
    for node in grafo:
        visitados[node] = False
    visitados[inicio] = True
    antecessor = {inicio: None}
    fila.append(inicio)
    while fila:
        atual = fila.pop(0)
        for i in grafo[atual]:
            if not visitados[i]:
                visitados[i] = True
                antecessor[i] = atual
                fila.append(i)
    caminho = []
    atual = destino
    while atual:
        caminho.append(atual)
        atual = antecessor[atual]
    caminho = caminho[::-1]
    for estacao in caminho:
        if estacao == caminho[-1]:
            print('[{}] {}'.format(estacao, nomes[estacao]))
        else:
            print('[{}] {}'.format(estacao, nomes[estacao]), end=' -> ')


def printDistancia(inicio, destino):
    print('[{}] {} -> [{}] {}: {} estações\n'.format(inicio, nomes[inicio],
                                                     destino, nomes[destino], distBFS(inicio, destino)))

color_map = []
for node in G:
    if node <= 18:
        color_map.append('dodgerblue')
    elif 18 < node <= 30:
        color_map.append('yellow')
    elif 30 < node <= 40:
        color_map.append('green')
    else:
        color_map.append('red')

plt.savefig("grafo.png")# save as png



def menu():
    while True:
        print('='*len('02. Distância entre duas estações'))
        print('01. Listar estações')
        print('02. Distância entre duas estações')
        print('03. Caminho entre duas estações')
        print('04. Mostrar lista de adjacência')
        print('05. Mostrar Grafo')
        print('06. Encerrar')
        print('='*len('02. Distância entre duas estações'))

        func = int(input('Selecione uma função(1~6): '))
        if func == 1:
            print(' ')
            for estacao in nomes:
                print('[{}]: {}'.format(estacao, nomes[estacao]))
            print(' ')
            nx.draw_circular(G, node_color=color_map, with_labels=True)
            plt.show() # display
        elif func == 2:
            inicio = int(input('Selecione a estação de início(nº): '))
            destino = int(input('Selecione a estação de destino(nº): '))
            print(' ')
            printDistancia(inicio, destino)
            nx.draw_circular(G, node_color=color_map, with_labels=True)
            plt.show() # display
        elif func == 3:
            inicio = int(input('Selecione a estação de início(nº): '))
            destino = int(input('Selecione a estação de destino(nº): '))
            print(' ')
            printCaminho(inicio, destino)
            print(' ')
            nx.draw_circular(G, node_color=color_map, with_labels=True)
            plt.show() # display
        elif func == 4:
            print(" ")
            printGrafo(grafo)
            print(" ")
        elif func == 5:
            nx.draw_circular(G, node_color=color_map, with_labels=True)
            plt.show() # display
        elif func ==6:
            return
        else:
            print('Função não definida!\n')


menu()
