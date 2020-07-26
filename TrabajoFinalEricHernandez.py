# 1.	Iniciar el programa: en la que el administrador ingresa la cantidad de productores del período y el sistema inicializa todas las listas,
# indica el monto que le va a pagar a cada productor por cada botella entregada, el precio al que vende cada botella y el premio en dinero que se le va a pagar al productor que realice 
# más entregas que el promedio de entregas general.
# 2.	Registrar productor (se debe registrar el productor de uno en uno), en la que se registra el id del productor, la cantidad de entregas y la cantidad de botellas de cada entrega.
# 3.	Imprimir la cantidad total de botellas que entregó un productor específico
# 4.	Imprimir el productor que más entregas realizó.
# 5.	Imprimir el promedio de entregas de todos los productores.
# 6.	Imprimir los productores que realizaron más entregas que el promedio de entregas.
# 7.	Realizar el pago a los productores, según el precio de cada botella y si aplica o no el premio por entregas.
# 8.	Imprimir el total de dinero que le debe pagar un productor específico.
# 9.	Imprimir el total que debe pagar a todos los productores.
# 10.	Imprimir la ganancia total de la cooperativa.

print("Bienvenido al Software de Administración de Productores de la Cooperativa La Vaca Lechera")

#Aquí vamos a preguntar el año en el cuál la información se va a registrar
año = int(input("Por favor ingrese el año en el cuál desea guardar sus datos: "))

#Aquí vamos a preguntar por la cantidad de productores y guardarlo en la variable.
cantidadProductores = int(input("Por favor ingresar la cantidad de productores a registrar: "))

#Aquí vamos a preguntar por el nombre del productor
nombreProductor = str(input("Por favor ingrese el nombre del productor a registrar: "))

#Aquí vamos a preguntar el ID del productor
productorID = int(input("Por favor ingrese el ID del productor a registrar: "))

#Aquí vamos a preguntar la cantidad de entregas por productor
cantidadEntregas = int(input("Por favor ingrese la cantidad de entregas a registrar: "))

#Aquí vamos a preguntar por la cantidad de botellas enviadas por productor
cantidadBotellas = int(input("Por favor ingrese la cantidad de botellas a registrar: "))




