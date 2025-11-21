# Completa las validaciones y llama a la función

import sys
from solucion import triangulo_simetrico 

def main():

    if sys.stdin.isatty():
        data = []
        data.append(input("Ingresa la altura: ").strip())
        data.append(input("Ingresa el caracter: ").strip())
    else:
        data = sys.stdin.read().strip().splitlines()

    # Validar líneas
    if len(data) < 2:
        print("Error: Se esperan 2 lineas de entrada (altura, caracter)")
        return

    m_str = data[0].strip()
    s = data[1].strip()

    # Convertir altura
    try:
        m = int(m_str)
    except ValueError:
        print("Error: La altura debe ser un numero entero")
        return

    # Validar altura positiva
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return

    # Validar longitud del carácter
    if len(s) != 1:
        print("Error: El caracter debe ser un solo simbolo")
        return

    # Llamada a la función
    triangulo_simetrico(m, s)


if __name__ == "__main__":
    main()
