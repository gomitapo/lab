from persona import Persona

class Docente(Persona):
    def __init__(self, nombre="", rut="", grado="", tipo="", fecha="" ):
        super().__init__(nombre, rut)
        self.__grado = grado
        self.__tipo = tipo
        self.__fecha = fecha
    


    def getgrado(self):
        return self.__grado
    
    def gettipo(self):
        return self.__tipo
    
    def getfecha(self):
        return self.__tipo
    
   
    def setgrado(self, grado):
        self.__grado = grado
    
    def settipo(self,tipo):
        self.__tipo = tipo
    
    def setfecha(self, fecha):
        self.__fecha = fecha

    def __str__(self):
         return "-Nombre: {0} -Rut: {1} -Grado: {2} -Tipo: {3} -Fecha: {4}".format(self.__nombre, self.__rut, self.__grado, self.__tipo, self.__fecha)