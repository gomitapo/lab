from Persona import Persona

class Docente(Persona):
    def __init__(self,Nombres="", Edad="", Sueldo="", Clase="", profesion=""):
        super().__init__(Nombres, Edad)
        self.__Sueldo = Sueldo
        self.__Clase = Clase
        self.__profesion = profesion
        self.__Nombres = Nombres
        self.__Edad = Edad

    def __str__(self):
        return "-Nombre: {} - Edad: {} - Sueldo: {} -Profesión {}".format(self.__Nombres, self.__Edad, self.__Sueldo, self.__Clase, self.__profesion )

    def GetNombre(self):
        return self.__Nombres

    def SetNombre(self,Nombres):
        self.__Nombres = Nombres
    
    def GetEdad(self):
        return self.__Nombres

    def SetEdad(self,Edad):
        self.__Edad = Edad
    
    def GetSueldo(self):
        return self.__Sueldo
    
    def SetSueldo(self,Sueldo):
        self.__Sueldo = Sueldo

    def GetClase(self):
        return self.__Clase

    def SetClase(self,Clase):
        self.__Clase = Clase
    
    def GetNet_Worth(self):
        return self.__profesion

    def SetNet_Worth(self,profesion):
        self.__profesion = profesion

    def Net_Worth_Calculator(self):
        networth = ((self.__Sueldo * 12) * (self.__Edad - 25))
        return networth
   