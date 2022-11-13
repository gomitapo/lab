from docente import Docente

class Adjunto(Docente):
    def __init__(self, nombre="", rut="", grado="", tipo="", fecha="",horas=0, cumpleaños=""):
        super().__init__(nombre, rut, grado, tipo, fecha)
        self.__horas = horas
        self.__nombre = nombre
        self.__rut = rut
        self.__grado = grado
        self.__tipo = tipo
        self.__fecha = fecha
        self.__cumpleaños = cumpleaños
    def gethoras(self):
        return self.__horas
    
    #2 metodos extra
    def getcumpleaños(self):
        return self.__cumpleaños
    def setcumpleaños(self,cumpleaños):
        self.__cumpleaños = cumpleaños
    #2 metodos extra
   
    def sethoras(self, horas):
        self.__horas = horas
    def calcularsueldo(self):
        if self.__grado == "licenciado":
            sueldo = self.__horas * 16000
            return sueldo
        if self.__grado == "magister":
            sueldo = self.__horas *19000
            return sueldo
        if self.__grado == "doctorado":
            sueldo = self.__horas* 25000
            return sueldo
    def __str__(self):
         return "-Nombre: {0} -Rut: {1} -Grado: {2} -Tipo: {3} -Fecha: {4} -Horas: {5} -Cumpleaños: {6} ".format(self.__nombre, self.__rut, self.__grado, self.__tipo, self.__fecha, self.__horas, self.__cumpleaños)
