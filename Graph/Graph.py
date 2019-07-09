'''
Grupo:
- Emanuel Umbelino
- Yuri Strack
'''

def permutacao(str):
    if len(str) <=1:
        return [str]
    perms = []
    for perm in permutacao(str[1:]):
        for i in range(len(perm)+1):
            perms += [perm[:i] + str[0:1] + perm[i:]]
    return perms

def movimentos(str):
	possibilidades = []
	vazio = str.index('0')
	if(vazio == 0 or vazio == 1):
		possibilidades += [str[1] + str[0] + str[2:]]
	if(vazio == 0 or vazio == 3):
		possibilidades += [str[3] + str[1:3] + str[0] + str[4:]]
	if(vazio == 1 or vazio == 2):
		possibilidades += [str[0] + str[2] + str[1] + str[3:]]
	if(vazio == 1 or vazio == 4):
		possibilidades += [str[0] + str[4] + str[2:4] + str[1] + str[5:]]
	if(vazio == 2 or vazio == 5):
		possibilidades += [str[:2] + str[5] + str[3:5] + str[2] + str[6:]]
	if(vazio == 3 or vazio == 4):
		possibilidades += [str[:3] + str[4] + str[3] + str[5:]]
	if(vazio == 3 or vazio == 6):
		possibilidades += [str[:3] + str[6] + str[4:6] + str[3] + str[7:]]
	if(vazio == 4 or vazio == 5):
		possibilidades += [str[:4] + str[5] + str[4] + str[6:]]
	if(vazio == 4 or vazio == 7):
		possibilidades += [str[:4] + str[7] + str[5:7] + str[4] + str[8]]
	if(vazio == 5 or vazio == 8):
		possibilidades += [str[:5] + str[8] + str[6:8] + str[5]]
	if(vazio == 6 or vazio == 7):
		possibilidades += [str[:6] + str[7] + str[6] + str[8]]
	if(vazio == 7 or vazio == 8):
		possibilidades += [str[:7] + str[8] + str[7]]

	return possibilidades


def gerarGrafo():
	perm = permutacao('012345678')
	dic = {}
	for p in perm:
		dic[p] = movimentos(p)
	return dic

G = gerarGrafo()
def nArestas(G):
    cont = 0
    for keys in G:
        cont += len(G[keys])
    return cont


print('\n--------------TAREFA 1--------------\n')

print('Numero de nós:',len(list(G.keys())))
print('Numero de arestas:',nArestas(G))
print('Visinhos do 012345678:',G['012345678'])

#----------------------------------------------------------

def createVisited(g):
    v = {}
    for node in g:
        # marca todos vertices como nao visitado (flag 0)
        v[node] = 0
    return v

visited = createVisited(G)

levels = [] 

def BFS(g):
    components = 0
    for vertex in g: #vertice == chave do dict
        if visited[vertex] == 0:
            BFS2(g,vertex)
            '''
            print('Leveis da Componente conexa %d' % (components+1))
            for el in levels:
                if len(el) != 0:
                    print(el)
            '''
            del levels[:]
            components += 1
    print("Number of components:", components)
    return

def BFS2(g,s):
    levels.append([s])
    visited[s] = 1
    j = 1
    while True:
        levels.append([])
        for u in levels[j-1]:
            for v in g[u]:
                if visited[v] == 0:
                    levels[j].append(v)
                    visited[v] = 1
        if len(levels[j]) == 0:
            return
        j += 1

print('\n--------------TAREFA 2--------------\n')

BFS(G)
visited.clear()
visited = createVisited(G)
levels = []

#----------------------------------------------------------

def maxCaminhoCurto(G,vertice):
    BFS2(G,vertice)
    tamMaior = len(levels)-1 #tamanho do maior dos caminhos mais curtos
    cfg = levels[tamMaior-1] #possiveis configuracoes iniciais
    return (cfg,tamMaior)


def main():
    t = maxCaminhoCurto(G,'123456780')
    print('Possiveis configuracoes iniciais:',t[0])
    print('Numero de movimentos necessarios:',t[1])
    visited.clear()
    return

print('\n--------------TAREFA 3--------------\n')

main()

#----------------------------------------------------------