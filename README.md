[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/0eApECPo)
# Tarea: Triángulo simétrico

## 🎯 Objetivo
Practicar:
- Validación básica de datos de entrada.
- Uso de ciclos anidados para generar patrones de texto.
- Separación de responsabilidades entre lectura/validación de entrada y lógica del algoritmo.

## 📝 Descripción del Problema
Crear un programa que lea un número entero positivo `m`, que representa la altura máxima de la figura, y un carácter `s`.

El programa deberá dibujar una figura de la siguiente manera:
- Primero, dibujará un triángulo rectángulo creciente que va desde $1$ carácter hasta `m` caracteres.
- Inmediatamente después, dibujará un triángulo rectángulo decreciente que va desde $m-1$ caracteres hasta $1$ carácter.

Cada fila de la figura estará formada únicamente por el carácter `s`, repetido tantas veces como corresponda.

Si la entrada no cumple con las condiciones el programa deberá mostrar el mensaje de error correspondiente y no dibujar la figura.

### 📥 Entrada
El programa recibirá dos líneas de entrada desde la entrada estándar:

1. Altura máxima (`m`):
   
   Una cadena que se espera que represente un número entero. Tras validarse, será la altura del triángulo creciente y el ancho máximo de la figura.

2. Carácter (`s`):
   
   Una cadena de texto cuyo primer carácter se utilizará para rellenar la figura.
   Esta línea no puede estar vacía.

### 📤 Salida
Si la entrada es válida, el programa imprimirá por pantalla la figura simétrica:
- Primero, `m` líneas crecientes: de $1$ a `m` caracteres.
- Después, $m - 1$ líneas decrecientes: de $m - 1$ a $1$ carácter.

Si la entrada es inválida, el programa imprimirá únicamente uno de los siguientes mensajes (según el caso):

- Si no se reciben al menos 2 líneas:
   ```
   Error: Se esperan 2 lineas de entrada (altura, caracter)
   ```

- Si la primera línea no es un entero:
   ```
   Error: La altura debe ser un numero entero
   ```

- Si la altura es menor o igual a 0:
   ```
   Error: La altura debe ser un entero positivo
   ```

### ⛔️ Restricciones
- El programa debe trabajar únicamente con la entrada estándar (no debe pedir datos con input() dentro de la versión que se evalúa).
- No cambies los nombres de los archivos ni de la función triangulo_simetrico.

> *Sugerencia*: Primero valida toda la entrada. Solo si todas las validaciones pasan, entra a la parte de dibujo de la figura. Esto te ayudará a mantener el código más claro y evitar errores.

### 🧾 Muestras
A continuación se muestran algunos ejemplos de entradas y salidas esperadas.

| Entrada | Salida |
|---------|--------|
| 3<br>*  | * <br> ** <br> *** <br> ** <br> * |
| 0<br>#  | Error: La altura debe ser un entero positivo |
| dos<br>@ | Error: La altura debe ser un numero entero |
| 4<br> | Error: El caracter no puede ser vacío |

El formato es estricto: respeta mayúsculas, minúsculas, espacios y saltos de línea.

### 🛠️ Resumen

- En **main.py**, valida primero todo lo relacionado con la entrada (cantidad de líneas, tipo de dato, vacío o no).
- En **solucion.py**, asume que s ya es válido y concéntrate en validar m y construir la figura.

---

## 📂 Estructura del Repositorio

```
.
├── README                        # Instrucciones de la tarea [No modificar]
├── main.py                       # Archivo para ejecutar el programa [Modificar]
├── solucion.py                   # Archivo donde debes implementar tu solución [Modificar]
├── .gitignore                    # Archivo para ignorar archivos en Git [No modificar]
├── requirements.txt              # Archivo para dependencias [No modificar]
└── disparador_autoevaluacion.py  # Archivo de respaldo para disparar la autoevaluación [No modificar]
```