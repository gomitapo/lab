class Persona():
    def __init__(self,Nombres, Edad):
        self.__Nombres = Nombres
        self.__Edad = Edad
        

    def __str__(self):
        return "-Nombre: {0} - Edad: {1} ".format(self.__Nombres, self.__Edad)

    def GetNombre(self):
        return self.__Nombres

    def SetNombre(self,Nombres):
        self.__Nombres = Nombres
    

    def GetEdad(self):
        return self.__Nombres

    def SetEdad(self,Edad):
        self.__Edad = Edad
    
    
    