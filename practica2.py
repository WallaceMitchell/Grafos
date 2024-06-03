def cuenta_grado(grafo_lista):
    '''
    Muestra por pantalla los grados de los vertices de un grafo. 
    El argumento esta en formato de lista.
    
    Ejemplo Entrada: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    Ejemplo retorno: 
        {'A': 1, 'B': 3, 'C': 2}
    '''
    vert = grafo_lista [0]
    aristas = grafo_lista [1]
    lista = {v: 0 for v in vert}

    for a in aristas:
        lista[a[0]] += 1
        lista[a[1]] += 1

    return lista


def vertice_aislado(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene una lista de los vértices aislado.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B')])
    Ejemplo formato salida: 
        ['D','E']
    '''

    aislado = []
    vert = grafo_lista [0]
    aristas = grafo_lista [1]
    lista = cuenta_grado(grafo_lista)

    for x, y in lista.items():
            if y == 0:
                aislado.append (x)

    return aislado

def componentes_conexas(grafo_lista):      #REVISAR MAÑANAAAAAAAAAAAAAAAAAAAAAA -----------------------------------------
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
    Ejemplo formato salida: 
        [['A, 'B','C'], ['D','E']]
    '''
    vertices = grafo_lista[0]
    aristas = grafo_lista[1]

    visitados = set()
    componentes = []

    def dfs(nodo, actual):
        visitados.add(nodo)
        actual.append(nodo)
        for vecino in [v for u, v in aristas if u == nodo]:
            if vecino not in visitados:
                dfs(vecino, actual)

    for nodo in vertices:
        if nodo not in visitados:
            nueva = []
            dfs(nodo, nueva)
            componentes.append(nueva)

    return componentes

def es_conexo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, y utilizando la función "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''

    trueOrFalse = False
    conexas = (componentes_conexas(grafo_lista))

    if len(conexas) == 1:
        trueOrFalse = True
    else:
        trueOrFalse = False


    return trueOrFalse


    