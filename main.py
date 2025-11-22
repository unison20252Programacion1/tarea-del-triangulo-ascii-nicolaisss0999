# Completa las validaciones y llama a la funcion

import sys
from solucion import triangulo_simetrico

def main():
    """
    data: lista de lineas leidas desde la entrada estandar o ingresadas por el usario donde cada elemento de la lista es un string
    """
    # IF que permite leer desde la entrada estandar o pedir datos al usuario
    if sys.stdin.isatty():
        data = []
        data.append(input("Ingresa la altura: ").strip())
        data.append(input("Ingresa el caracter: "))
    else:
        data = sys.stdin.read().strip().splitlines()

        #Validar que se recibieron dos lineas
        if len(data) < 2:
            print("Error: Se esperan 2 lineas de entrada (altura, caracter)")
            return

        m_str = data[0].strip() # Primera linea: altura maxima (como texto)
        s = data[1]             # Segunda linea: caracter (o cadena) para la figura

        # Intentar convertir la altura a entero
        try:
            # TODO: Convertir m_str a entero y asignarlo a m
            m = int(m_str)
        except ValueError:
            #TODO: imprimir "Error: La altura debe ser un numero entero" y salir
            print("Error: La altura debe ser un numero entero")
            return

        # TODO: llamar a la funcion triangulo_simetrico con los parametros m y s 
        triangulo_simetrico(m,s)

    if _name_ == "_main_":
        main()
