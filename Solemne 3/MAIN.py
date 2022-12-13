import pandas as pd
import numpy as np
import random as rd
from Persona import Persona
from Estudiante import Estudiante
from Docente import Docente


#SOLEMNE 3 CARLOS CERDA MANUEL CAYUMAN

def lectura():
    global df
    global carga
    df = pd.read_csv("Solemne03.csv")
    carga = True
    return df


def limpieza_1():
    global df
    global listam
    global limpio
    df = df.drop(df.index[df.Edad == 0], axis = 0)

    df = df.drop(df.index[df.Edad > 120], axis = 0)

    df = df.drop(df.index[df.Nombres == "nan"], axis= 0 )

    df = df.drop(df.index[df.Nombres == "NaN"], axis = 0)

    df = df.drop(df.index[df.Nombres == "TRUE"], axis = 0)

    df = df.drop(df.index[df.Nombres == "FALSE" ], axis = 0)
    
    df = df.drop(df.index[df.Nombres == "NaN" ], axis = 0)
    
    df = df.sort_values(by= "Sueldo")

    df = df.drop(columns = ["Unnamed: 0"])

    df = df.drop_duplicates(subset="Nombres", keep="last")
    
    listam = []
    
    for i in range(len(df)):
        n = rd.randint(1,2) 
        if n == 1:
            value = "Estudiante"
            listam.append(value)
        else:
            value = "Docente"
            listam.append(value)
    df["Clase"]=listam
    limpio = True
    print(df)
    return df





def csx():
    global dfdocente
    global d
    for i in df:
        try:
            dfdocente = df.drop(df.index[df.Clase == "Estudiante"])
            d = dfdocente.values.tolist()
            

        except:NameError

        finally:
            return "ha ocurrido un error de nombre"

def csx2():
    global dfestudiante
    global e
    for i in df:
        try:
            dfestudiante = df.drop(df.index[df.Clase == "Docente"])
            e = dfestudiante.values.tolist()
            
            

        except:NameError

        finally:
            return "ha ocurrido un error de nombre"

def Lista_Docentes():
    global listaDocentes
    global d
    listaDocentes = []
    n = 0
    for i in d:
    
        atributo1 = d[n][0]
        atributo2 = d[n][1]
        atributo3 = d[n][2]
        atributo4 = d[n][3]
        obj = Docente(atributo1, atributo2, atributo3, atributo4)
        listaDocentes.append(obj)
        n = n+1
        

def Lista_Estudiantes():
    global listaEstudiantes
    global e
    listaEstudiantes = []
    n = 0
    for i in e:
    
        atributo1 = e[n][0]
        atributo2 = e[n][1]
        atributo3 = e[n][2]
        atributo4 = e[n][3]
        obj = Estudiante(atributo1, atributo2, atributo3, atributo4)
        listaEstudiantes.append(obj)
        n = n+1
        




def MuestraDatos1(lista):
    print("\nLista De: \n")
    for i in lista:
        print(i)


val = 1

while val == 1:
    print("menú de seleción")
    cuek = int(input("1. Realizar carga 2. Realizar Limpieza 3.Crear lista de docentes 4. Crear lista de estudiantes 5. crear archivos excell 6. salir: "))
    if cuek == 1:
        lectura()
    elif cuek == 2 and carga == True:
        try:
            limpieza_1()
        except NameError:
            print("Complete el paso 1")

    elif cuek == 3 and carga == True and limpio == True:
        global todo
        csx()
        csx2()
        Lista_Docentes()
        Lista_Estudiantes()
        todo = True
    
    elif cuek == 5 and todo == True:
        dfestudiante.to_excel("ListaEstudiantes.xlsx")
        dfdocente.to_excel("ListaDocentes.xlsx")
    
    elif cuek == 6:
        val = 2
#para ver si estan las listas hechas nomas
MuestraDatos1(listaEstudiantes)
MuestraDatos1(listaDocentes)




            

           
    

    
        

            
        

    
    

    













