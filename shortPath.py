import pandas as pd

def getInicioFinal(x):
    tam = len(x)
    for j in range(tam):
        for i in range(tam):
            if(x[j][i] == 1):
                inicio = (i,j)
            elif(x[j][i] == 2):
                final = (i,j)
    return inicio,final       
            
def criarGrafo(x, grafo):
    tam = len(x)
    for i in range(tam):
        for j in range(tam):
            if(j == 0):
                if(i == 0):
                    grafo[(i,j)]= [(i,j+1),(i+1,j)]
                
                elif(i == tam-1):
                    grafo[(i,j)] = [(i-1,j),(i,j+1)]
                else:
                    grafo[(i,j)] = [(i-1,j),(i,j+1),(i+1,j)]
                
                
            elif(j==tam-1):
                if(i == 0):
                    grafo[(i,j)] = [(i,j-1),(i+1,j)]            
                elif(i == tam-1):
                    grafo[(i,j)] = [(i-1,j),(i,j-1)]
                else:
                    grafo[(i,j)] = [(i-1,j),(i,j-1),(i+1,j)]
            else:
                if(i==0):
                    grafo[(i,j)] = [(i,j+1),(i,j-1),(i+1,j)]
                elif(i == tam-1):
                    grafo[(i,j)] = [(i-1,j),(i,j+1),(i,j-1)]
                else:
                    grafo[(i,j)] = [(i-1,j),(i,j+1),(i,j-1),(i+1,j)]

                
def caminhoMinimo(x, grafo, inicio, final):
    caminho = []
    fila = []
    visitado = {}
    cont = 1
    pai = {}
    fila.append(inicio)
    pai[inicio] = None
    visitado[inicio] = cont    
    vertice = inicio
    keys = []
    while(fila):
        vertice = fila.pop(0)
        ans = grafo.get(vertice)
        if ans == None:
            ans = []
        for vizinho in ans:
            if(not visitado.get(vizinho) and (x[vizinho[1]][vizinho[0]] == 2)):
                pai[vizinho] = vertice
                fila = []
                break
            elif(not visitado.get(vizinho) and (x[vizinho[1]][vizinho[0]] == 0)):
                fila.append(vizinho)
                visitado[vizinho] = cont
                pai[vizinho] = vertice
        cont += 1
    
    for i in pai.keys():
        if(i not in keys):
            keys.append(i)
      
    k = final
    
    while (k != None):
        if k in keys:
            caminho.append(k)
            k = pai[k]
    return caminho      
            
            
            

            
x = pd.read_csv("entrada.txt", sep=',', header=None)

inicio, final = getInicioFinal(x)
grafo = {}
criarGrafo(x, grafo)
caminho = caminhoMinimo(x, grafo, inicio, final)
tam = len(caminho)

print(x)
print("\nO menor caminho encontrado possui a distância de: %d casas" %(tam-2)) 
for i in reversed(caminho):
    if(i == caminho[0]):
        print(i)
    else:
        print(i, end  = ">>")
    