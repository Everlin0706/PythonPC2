#Estructuras Iterativas:
#Problema 1:
#Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
#en el rango de 1500 y 2700 (ambos incluidos).

# Definir el rango de búsqueda
inicio = 1500
fin = 2700

# Crear una lista para almacenar los números que cumplen la condición
numeros_encontrados = []

# Iterar sobre el rango de números
for num in range(inicio, fin + 1):
    if num % 7 == 0 and num % 5 == 0:
        numeros_encontrados.append(num)

# Mostrar los números encontrados
print("Números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700:")
print(numeros_encontrados)


#Problema 2:
#Escriba un programa en Python para construir el siguiente patrón.
# Parte superior del patrón
for i in range(1, 6):  # Desde 1 hasta 5
    print('* ' * i)

# Parte inferior del patrón
for i in range(4, 0, -1):  # Desde 4 hasta 1
    print('* ' * i)




#Problema 3:
# Inicializar listas y contadores
numeros = []
pares = 0
impares = 0

# Bucle para solicitar números al usuario
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").strip().upper()
    
    if respuesta == 'NO':
        break
    
    if respuesta == 'SI':
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
        
        # Evaluar si el número es par o impar
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

# Mostrar los resultados
print("\nNúmeros ingresados:", numeros)
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")


#Problema 4:

# Initialize an empty list to store students
students = []

# Get the number of students
n = int(input("Enter the number of students: "))

# Loop to get student details
for i in range(n):
    # Get student name
    name = input(f"Enter the name of student {i+1}: ")
    
    # Get the student's three grades
    grades = []
    for j in range(3):
        grade = int(input(f"Enter grade {j+1} for {name}: "))
        grades.append(grade)
    
    # Create a dictionary for the student and their grades
    student = {
        "Alumno": name,
        "Notas": grades
    }
    
    # Add the student dictionary to the list
    students.append(student)

# Display the complete list of students with their grades
print("\nList of students and their grades:")
for student in students:
    print(f"Alumno: {student['Alumno']}, Notas: {student['Notas']}")


#Problema 5

# Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función para encontrar la suma de los números primos menores que 100
def suma_primos_menores_100():
    suma = 0
    for num in range(2, 100):
        if es_primo(num):
            suma += num
    return suma

# Llamar a la función y mostrar el resultado
resultado = suma_primos_menores_100()
print(f"La suma de todos los números primos menores que 100 es: {resultado}")



#Problema 6
# Función para generar la serie de Fibonacci hasta un límite
def fibonacci_hasta_50():
    serie = []
    a, b = 0, 1
    while a <= 50:
        serie.append(a)
        a, b = b, a + b
    return serie

# Llamar a la función y mostrar el resultado
resultado = fibonacci_hasta_50()
print("La serie de Fibonacci entre 0 y 50 es:")
print(resultado)


#Problema 7:
# Función para verificar si un número es perfecto
def es_numero_perfecto(n):
    suma_divisores = 0
    # Encontrar los divisores propios de n
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    # Verificar si la suma de los divisores es igual al número
    return suma_divisores == n

# Función para encontrar todos los números perfectos menores que 1000
def numeros_perfectos_menores_1000():
    perfectos = []
    for num in range(1, 1000):
        if es_numero_perfecto(num):
            perfectos.append(num)
    return perfectos

# Llamar a la función y mostrar los números perfectos
resultado = numeros_perfectos_menores_1000()
print("Los números perfectos menores que 1000 son:")
print(resultado)


#Problema 8:
# Función para calcular el factorial de un número
def factorial(n):
    # Asegurarse de que el número es no negativo
    if n < 0:
        return "El factorial no está definido para números negativos."
    
    # El factorial de 0 es 1
    if n == 0 or n == 1:
        return 1
    
    # Calcular el factorial
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    
    return resultado

# Ejemplo de uso
numero = int(input("Introduce un número entero no negativo: "))
print(f"El factorial de {numero} es: {factorial(numero)}")



#Problema 9:
# Función para omitir las vocales de una cadena
def omitir_vocales(texto):
    vocales = "aeiouAEIOU"
    resultado = ""
    for char in texto:
        if char not in vocales:
            resultado += char
    return resultado

# Ejemplo de uso
entrada = input("Introduce una cadena de texto: ")
salida = omitir_vocales(entrada)
print(f"Texto sin vocales: {salida}")


#Problema 10:
# Diccionario para convertir los meses en palabras a su correspondiente número
meses = {
    "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04", "Mayo": "05", "Junio": "06",
    "Julio": "07", "Agosto": "08", "Septiembre": "09", "Octubre": "10", "Noviembre": "11", "Diciembre": "12"
}

# Función para convertir fecha en formato MM/DD/AAAA o Mes Día, Año a AAAA-MM-DD
def convertir_fecha(fecha):
    # Verificamos si la fecha tiene formato numérico (ejemplo: 8/9/1636)
    if '/' in fecha:
        mes, dia, anio = fecha.split('/')
        return f"{int(anio):04d}-{int(mes):02d}-{int(dia):02d}"
    
    # Si la fecha está en formato "Mes Día, Año" (ejemplo: Septiembre 8, 1636)
    else:
        partes = fecha.replace(',', '').split()  # Eliminamos la coma y separamos
        mes = partes[0]
        dia = partes[1]
        anio = partes[2]
        mes_numerico = meses[mes]
        return f"{int(anio):04d}-{mes_numerico}-{int(dia):02d}"

# Ejemplo de uso
fecha_1 = "8/9/1636"
fecha_2 = "Septiembre 8, 1636"

print(f"Input: {fecha_1} | Output: {convertir_fecha(fecha_1)}")
print(f"Input: {fecha_2} | Output: {convertir_fecha(fecha_2)}")
