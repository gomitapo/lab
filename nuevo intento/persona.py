class Persona():
    def __init__(self, nombre="", rut=""):
        self.__nombre = nombre
        self.__rut = rut
    
    def getnombre(self):
        return self.__nombre
    def getrut(self):
        return self.__rut
    
    def setnombre(self, nombre):
        self.__nombre = nombre
    def setrut(self, rut):
        self.__rut = rut
    
    def __str__(self):
         return "-Nombre: {0} -Rut: {1}".format(self.__nombre, self.__rut)