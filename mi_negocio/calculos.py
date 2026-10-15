def buscar_posicion(lista,nombre):
    for i in range((len(lista))):
        if lista[i]==nombre:
            return i
    return -1

def calcular_subtotal(precio,cantidad):
    return precio*cantidad

def aplicar_descuento(subtotal,porcentaje=0.1):
    descuento= round(sum(subtotal)*porcentaje,2)
    descontado= round(sum(subtotal)-descuento,2)
    return descuento, descontado

def aplicar_iva(descontado, tasa_iva=0.21):
    iva= round(descontado*tasa_iva,2)
    aplicado=round(descontado+iva,2)
    return iva, aplicado
