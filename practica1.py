#! /usr/bin/python

# 1ra Practica Laboratorio 
# Teoria de Grafos
# Consigna: Implementar los siguientes metodos

import sys
from practica2 import *
from practica3 import *

def lee_grafo_stdin(grafo):

    tupla = ([],[])

    vert = int (grafo[0])

    for x in range (1, vert + 1):
        tupla[0].append(grafo[x])

    for y in range (vert + 1, len(grafo)):
        elem1 = grafo [y] [0]
        elem2 = grafo [y] [2]
        tupla[1].append((elem1, elem2))

    return tupla

def lee_grafo_archivo(file_path):
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    pass

def imprime_grafo_lista(grafo):
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
    pass

#################### FIN EJERCICIO PRACTICA ####################
def lee_entrada_1():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    '''
    data_input = []
    
    for line in sys.stdin:
        if line == '\n':
            break
        else:
            # Con strip() eliminamos los '\n' del final de c/line
            data_input.append(line.strip())
            
    return data_input

    
def lee_entrada_2():
    count = 0
    try:
        while True:
            line = input()
            count = count + 1
            print ('Linea: [{0}]').format(line)
    except EOFError:
        pass
    
    print ('leidas {0} lineas').format(count)


def main ():
    grafo = lee_entrada_1()
    print (grafo)
    print(lee_grafo_stdin(grafo))
    print(cuenta_grado(lee_grafo_stdin(grafo)))
    print(vertice_aislado(lee_grafo_stdin(grafo)))
    print(componentes_conexas(lee_grafo_stdin(grafo)))
    print(es_conexo(lee_grafo_stdin(grafo)))
    print(valida_nodo_en_grafo(lee_grafo_stdin(grafo), 'a'))

if __name__ == '__main__':
        main()
