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

#####################################################################################################################

#Zona de métodos

#Aquí vamos a saludar mediante un método, dar la bienvenida al Software

def saludoInicial():
    print("Bienvenido al Software de Administración de Productores de la Cooperativa La Vaca Lechera")

#Aquí vamos a indicar el monto a pagar por cada botella entregada y el precio de cada botella, mediante un método

def mostrarPagoEntregaPrecioBotella():
    global pagoBotellaEntregada
    pagoBotellaEntregada = 200
    print("El pago por botella entregada es de: ",pagoBotellaEntregada)
    global precioUnitarioBotella
    precioUnitarioBotella = 1200
    print("El precio unitario por botella es de: ",precioUnitarioBotella)

#Aquí vamos a preguntar mediante un método, por el registro de cada productor

def consultaRegistroProductores():
    global listaRegistroProductores
    listaRegistroProductores = []
    global nombreProductor
    nombreProductor = str(input("Por favor ingrese el nombre del productor a registrar: "))
    listaRegistroProductores.append(nombreProductor)

#Aquí vamos a preguntar mediante un método, el ID del productor

def consultaIDProductores():
    global listaProductores
    listaProductores = []
    global productorID
    productorID = int(input("Por favor ingrese el ID del productor a registrar: "))
    listaProductores.append(productorID)

#Aquí vamos a preguntar mediante un método, la cantidad de entregas por productor

def consultaCantidadEntregas():
    global listaEntregas
    listaEntregas = []
    global cantidadEntregas
    cantidadEntregas = int(input("Por favor ingrese la cantidad de entregas a registrar: "))
    listaEntregas.append(cantidadEntregas)

#Aquí vamos a preguntar mediante un método, la cantidad de botellas enviadas por productor

def consultaCantidadBotellas():
    global listaBotellasPorEntrega
    listaBotellasPorEntrega = []
    global cantidadBotellas
    cantidadBotellas = int(input("Por favor ingrese la cantidad de botellas a registrar: "))
    listaBotellasPorEntrega.append(cantidadBotellas)

#Aquí vamos a preguntar mediante un método, el año en el cuál la información se va a registrar

def consultaAño():
    global año
    año = int(input("Por favor ingrese el año en el cuál desea guardar sus datos: "))

#Aquí vamos a preguntar mediante un método, si desea continuar agregando información al programa

def consultaDeseaContinuar():
    global deseaContinuar
    deseaContinuar = str(input("Desea continuar agregando datos? ")).upper()

#Aquí vamos a guardar toda la información de cada productor y crear un índice

def consultaListaIndices():
    global listaIndices
    listaIndices = []
    listaIndices.append(listaRegistroProductores,listaProductores,listaEntregas,listaBotellasPorEntrega)

#Aquí vamos a calcular el promedio de entrega mediante un método

def calculoPromedio():
    global calcPromedio
    calcPromedio = cantidadBotellas / cantidadEntregas
    return calcPromedio

#Aquí vamos a calcular el pago que va a recibir el productor, mediante un método

def calculoPagoProductor():
    global pagoProductor
    pagoProductor = pagoBotellaEntregada * cantidadBotellas
    return pagoProductor

#Aquí vamos a calcular la ganancia de la Cooperativa por ventas, mediante un método

def calculoGananciaCooperativa():
    global gananciaCooperativa
    gananciaCooperativa = (precioUnitarioBotella - pagoBotellaEntregada) * cantidadBotellas
    return gananciaCooperativa

#####################################################################################################################

#Zona de pruebas

menu = True

while menu:

    saludoInicial()
    mostrarPagoEntregaPrecioBotella()
    consultaRegistroProductores()
    consultaIDProductores()
    consultaCantidadEntregas()
    consultaCantidadBotellas()
    consultaAño()
    consultaDeseaContinuar()

    if deseaContinuar == "SI":
        menu = True
    else:
        menu = False

print("El productor:",nombreProductor,", con ID número:",productorID,", con una cantidad total de entregas de:",cantidadEntregas,", con una cantidad total de botellas de:",cantidadBotellas,", en el año:",año)
print("Teniendo un promedio de:",calcPromedio,"botellas por entrega. Recibiendo un pago de:",pagoProductor,"y dejando una ganancia a la Cooperativa de:",gananciaCooperativa)