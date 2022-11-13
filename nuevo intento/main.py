from adjunto import Adjunto
from regular import Regular
import pickle
def MuestraDatos1(lista_regular):
    print("\nLista de docentes regulares\n")
    acc = 0
    for i in lista_regular:
        acc += 1
        print(i)
def MuestraDatos2(lista_adjunto):
    print("\nLista de docentes adjuntos\n")
    acc = 0
    for i in lista_adjunto:
        acc += 1
        print(i)


def guardardatos1():
    archivo = open("lista_docentes_r", "wb")
    pickle.dump(lista_regular, archivo)
    archivo.close


def guardardatos2():
    archivo = open("lista_docentes_a", "wb")
    pickle.dump(lista_adjunto, archivo)
    archivo.close

def cargar_datos1():
    archivo = open("lista_docentes_a", "ab+")
    archivo.seek(0)

    try:
        lista_regular = pickle.load(archivo)
        print(f"{len(lista_regular)} docentes cargados correctamente")
        MuestraDatos1(lista_regular)
    except EOFError:
        print("no se han cargado docentes")
    finally:
        archivo.close()

def cargar_datos2():
    archivo = open("lista_docentes_a", "ab+")
    archivo.seek(0)

    try:
        lista_adjunto = pickle.load(archivo)
        print(f"{len(lista_adjunto)} docentes cargados correctamente")
        MuestraDatos2(lista_adjunto)
    except EOFError:
        print("no se han cargado docentes")
    finally:
        archivo.close()
    
    

p = 1
while p == 1:
    print("sistema de ingreso de datos")
    tipo = input("ingrese el tipo de docente: ")
    if tipo == "regular":
        nom = input("ingrese el nombre del docente: ")
        a = 1
        while a == 1:
            rut = int(input("ingrese su rut: "))
            n = len(str(rut))
            if n == 9:
               r = rut
               a = 0
            else: ("introduzca un rut válido")
#validador de rut
            
                
        grade = input("ingrese el grado del docente: ")
        date = input("ingrese la fecha del contrato: ")
        jorn = input("ingrese el tipo de jornada: ")
        base = int(input("ingrese su sueldo base: "))
        k = int(input("si desea ingresar su nacionalidad marque 1: "))
        if k == 1:
            nacion = input("ingrese su nacionalidad: ")
            lista_regular = []
            docente1 = Regular(nom, r, grade, date, jorn, tipo, base, nacion)
            lista_regular.append(docente1)
            MuestraDatos1(lista_regular)
            guardardatos1()
            print("el sueldo del docente es:" + str(docente1.calcularsueldo()))
            q = int(input("¿Desea conocer la cantidad de docentes regulares?, presione 1: "))
            if q == 1:
                cargar_datos1()
                p = int(input("escriba 1 si desea seguir: "))
            else:
                 p = int(input("escriba 1 si desea seguir: "))
            
            
        else:
            lista_regular = []
            docente1 = Regular(nom, r, grade, date, jorn, tipo, base)
            lista_regular.append(docente1)
            MuestraDatos1(lista_regular)
            guardardatos1()
            print("el sueldo del docente es:" + str(docente1.calcularsueldo()))
            q = int(input("¿Desea conocer la cantidad de docentes regulares?, presione 1: "))
            if q == 1:
                cargar_datos1()
                p = int(input("escriba 1 si desea seguir: "))
            else:
                 p = int(input("escriba 1 si desea seguir: "))
            
       
        lista_regular = []
        docente1 = Regular(nom, r, grade, date, jorn, tipo)
        lista_regular.append(docente1)
        MuestraDatos1(lista_regular)
        guardardatos1()
        print("el sueldo del docente es:" + str(docente1.calcularsueldo()))
        q = int(input("¿Desea conocer la cantidad de docentes regulares?, presione 1: "))
        if q == 1:
            cargar_datos1()
            p = int(input("escriba 1 si desea seguir: "))
        else:
             p = int(input("escriba 1 si desea seguir: "))
        
       


    elif tipo == "adjunto":
        nom = input("ingrese el nombre del docente: ")
        a = 1
        while a == 1:
            rut = int(input("ingrese su rut: "))
            n = len(str(rut))
            if n == 9:
               r = rut
               a = 0
            else: ("introduzca un rut válido")
        grade = input("ingrese el grado del docente: ")
        date = input("ingrese la fecha del contrato: ")
        horas = int(input("ingrese las horas trabajadas: "))
        k = int(input("si desea ingresar el día de su cumpleaños marque 1: "))
        if k == 1:
            cumple = input("ingrese su cumpleaños en el formato que desee: ")
            lista_adjunto = []
            docente1 = Adjunto(nom, r, grade, tipo, date, horas, cumple)
            lista_adjunto.append(docente1)
            guardardatos2()
            MuestraDatos2(lista_adjunto)
            print("el sueldo del docente es:" + str(docente1.calcularsueldo()))
            q = int(input("¿Desea conocer la cantidad de docentes adjuntos?, presione 1: "))
            if q == 1:
                cargar_datos2()
                p = int(input("escriba 1 si desea seguir: "))
            else:
                 p = int(input("escriba 1 si desea seguir: "))
            
        else:
            lista_adjunto = []
            docente1 = Adjunto(nom, r, grade, tipo, date, horas)
            lista_adjunto.append(docente1)
            guardardatos2()
            MuestraDatos2(lista_adjunto)
            print("el sueldo del docente es:" + str(docente1.calcularsueldo()))
            q = int(input("¿Desea conocer la cantidad de docentes adjuntos?, presione 1: "))
            if q == 1:
                cargar_datos2()
            else:
                 p = int(input("escriba 1 si desea seguir: "))
            p = int(input("escriba 1 si desea seguir: "))

        lista_adjunto = []
        docente1 = Adjunto(nom, r, grade, tipo, date, horas)
        lista_adjunto.append(docente1)
        guardardatos2()
        MuestraDatos2(lista_adjunto)
        print("el sueldo del docente es:" + str(docente1.calcularsueldo()))
        q = int(input("¿Desea conocer la cantidad de docentes adjuntos?, presione 1: "))
        if q == 1:
            cargar_datos2()
            p = int(input("escriba 1 si desea seguir: "))
        else:
             p = int(input("escriba 1 si desea seguir: "))
        
            
       

