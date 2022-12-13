from Persona import Persona
class Estudiante(Persona):
    def __init__(self,Nombres="", Edad="", Sueldo=0, Clase="", h_trabajadas= 0):
        super().__init__(Nombres, Edad)
        self.__Sueldo = Sueldo
        self.__Clase = Clase
        self.__Nombres = Nombres
        self.__Edad = Edad
        
        self.__h_trabajadas= h_trabajadas

    def __str__(self):
        return "-Nombre: {0} - Edad: {1} - Sueldo: {2} -Clase: {3}".format(self.__Nombres, self.__Edad, self.__Sueldo, self.__Clase )

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
    
    def GetH_Trabajadas(self):
        return self.__h_trabajadas

    def SetClase(self,h_trabajadas):
        self.__h_trabajadas = h_trabajadas
    
    
    def Ganancia_Hora(self):
        g_hora = (self.__Sueldo/self.__h_trabajadas)
        return g_hora
