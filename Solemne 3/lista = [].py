import pandas as pd
import numpy as np
import random as rd

lista = []
estudiante = "maicon"
lista.append(estudiante)

print(lista)

listam = []
def agrega_lista():
    for i in range(len(df)):
        n = rd.randint(1,2) 
        if n == 1:
            value = "estudiante"
            listam.append(value)
        else:
            value = "docente"
            listam.append(value)