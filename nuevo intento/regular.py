from docente import Docente


class Regular(Docente):
    def __init__(self, nombre="", rut="", grado="", tipo="", fecha="", jornada="",sueldob=0, nacionalidad=""):
        super().__init__(nombre, rut, grado, tipo, fecha)
        self.__jornada = jornada
        self.__nombre = nombre
        self.__rut = rut
        self.__grado = grado
        self.__tipo = tipo
        self.__fecha = fecha
        self.__nacionalidad = nacionalidad
        self.__sueldob = sueldob
    
    def getjornada(self):
        return self.__jornada
    def setjornada(self,jornada):
        self.__jornada = jornada
    
    # 2 metodos extra
    def getnacionalidad(self):
        return self.__nacionalidad
    def setnacionalidad(self,nacionalidad):
        self.__nacionalidad = nacionalidad
    # 2 metodos extra
    def getsueldob(self):
        return self.__sueldob
    def setsueldob(self, sueldob):
        self.__sueldob = sueldob
    
    def calcularsueldo(self):
        if self.__jornada == "completa":
            if self.__grado == "licenciado":
                sueldo = self.__sueldob + 200000
                return sueldo
            if self.__grado == "magister":
                sueldo = self.__sueldob + 500000
                return sueldo
            if self.__grado == "doctorado":
                sueldo = self.__sueldob + 800000
                return sueldo
        else:
            if self.__grado == "licenciado":
                sueldo = self.__sueldob + 100000
                return sueldo
            if self.__grado == "magister":
                sueldo = self.__sueldob + 300000
                return sueldo
            if self.__grado == "doctorado":
                sueldo = self.__sueldob + 700000
                return sueldo

    
    def __str__(self):
         return "-Nombre: {0} -Rut: {1} -Grado: {2} -Tipo: {3} -Fecha: {4} -Jornada: {5} -Sueldo Base: {6} -Nacionalidad {7} ".format(self.__nombre, self.__rut, self.__grado, self.__tipo, self.__fecha, self.__jornada, self.__sueldob, self.__nacionalidad)