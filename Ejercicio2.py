lista=[]
for i in range(2):
    nombre = input( "Ingrese nombre: ")
    sexo = input("Ingrese sexo: ")
    edad = int(input("Ingrese edad: "))
    if edad >= 5 and edad <= 17:
        item = [nombre, sexo, edad]
        lista.append(item)
    else:
        print("No se aceptan personas mayores a 17 o menores a 5. Reinicie la aplicación")
        break
for item in lista:
    print("Nombre:", item[0],"Sexo:", item[1],"Edad:", item[2])
 

    




