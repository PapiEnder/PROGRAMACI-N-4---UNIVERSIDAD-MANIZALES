#ESTUDIANTE: JOSE FERNANDO RAVE HENAO
#A partir de la verisión 3 del programa (v3_decisiones), resolver los siguientes requerimientos:
#    1. Algunos productos pueden tener un porcentaje de descuento. Por cada producto se debe preguntar si 
# tiene porcentaje de descuento, en caso que el producto tenga descuento este debe ser aplicado y debe 
# reflejarse en el total de la compra. Debe aplicarse a los dos productos de la compra

producto1 = str(input("Ingrese el nombre del primer producto:  "))
precio1 = float(input("Ingrese el precio del primer producto:  $"))
if precio1 > 0:
    tf_descuento = str(input("¿El primer producto tiene descuento? (si/no):  ")).lower()
    if tf_descuento == "si":
        porcen_descuento = float(input("Ingrese el porcentaje de descuento del primero producto: %"))
        print(f"El precio del producto {producto1} es de ${precio1} y con descuento es de ${precio1-(precio1*porcen_descuento/100)}")
    else:
        print(f"El precio del producto {producto1} es de ${precio1} y no tiene descuento.")
else:
    print("El precio del producto debe ser mayor a 0")

#    2. Algunos clientes son clientes VIP, cuando un cliente es VIP, puede escoger si paga a cuotas o de contado. 
# Si el cliente decide pagar a cuotas, entonces el sistema debe mostrarle cuanto debe pagar por cada cuota

nombre_cliente = str(input("Ingrese el nombre del cliente:  "))
valor_pagar = float(input("Ingrese el valor que va a pagar:  $"))
if valor_pagar > 0:
    cliente_vip = str(input(f"¿{nombre_cliente} es cliente VIP?(si/no):  ")).lower()
    if cliente_vip == "si":
        metodo = str(input("¿Cómo desea pagar? (cuotas/contado):  ")).lower()
        if metodo == "cuotas":
            cuotas = int(input("¿En cuántas cuotas desea pagar?:  "))
            if cuotas > 0:
                valor_cuota = valor_pagar / cuotas
                print(f"El cliente {nombre_cliente}, debera pagar ${valor_cuota} por cada cuota")
            else:
                print("El numero de cuotas debe ser mayor a 0")
        else:
            print(f"El cliente {nombre_cliente} deberá pagar de contado ${valor_pagar}")
    else:
        print(f"El cliente {nombre_cliente} deberá pagar de contado ${valor_pagar}")
else:
    print("El valor a pagar debe ser mayor a 0")



#    3. El supermercado a veces hace rifas, se le pregunta al cliente un número entre un valor X y un valor Y. 
# Si el cliente adivina el número la compra tendrá un descuento del 90%, 
# se le debe informar al cliente cuánto dinero se ahorró y cuánto debe pagar en el total de la cuenta.

descuento = 0.9
numero_correcto = int(input("Ingrese el numero correcto de la rifa:  "))
numero_X = int(input("Ingrese el limite inferior:  "))
numero_Y = int(input("Ingrese el limite superior:  "))
if numero_X <= numero_correcto <= numero_Y:
    print("-----------------------------------------------------")
    cliente = str(input("Ingrese el nombre del cliente:  "))
    pagar = float(input("Ingrese el valor a pagar:  $"))
    if pagar > 0: 
        numero_adivinado = int(input(f"{cliente}, adivina un número entre {numero_X} y {numero_Y}:  "))
        print("-----------------------------------------------------")
        if numero_adivinado == numero_correcto:
            total = pagar - (pagar * descuento)
            print(f"¡Felicidades {cliente}, adivinaste el numero correcto, el pago total de tu compra es de ${total}, y ahorraste ${pagar-total}!")
        else:
            print(f"Lo siento {cliente}, no adivinaste el número correcto, tu valor a pagar es de ${pagar}")
    else:
        print("El valor a pagar debe ser mayor a 0")
else:
    print(f"El número {numero_correcto} no se encuentra dentro de {numero_X} y {numero_Y}, por lo tanto no se puede realizar la rifa")

#    Parámetros de entrega:
#    1. Debe ser resuelto en Python
#    2. Debe ser individual
#    3. Fecha de entrega: Debe entregarse máximo el día 25 de agosto a las 12 am
#    4. Deben subir este taller a GitHub antes de la fecha de entrega, es decir: 25 de agosto a las 12 am
#    5. Por cada día de retraso en la entrega se disminuye la calificación del taller una (1) unidad
#    6. Deben adjuntar pantallazos del programa funcionando. Estos pantallazos deben ir dentro del mismo código fuente del proyecto.
