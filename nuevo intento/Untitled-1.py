a = 1
while a == 1:
    rut = int(input("ingrese su rut: "))
    n = len(str(rut))
    if n == 9:
       r = rut
    else:
        print("introduzca un rut válido: ")
        
