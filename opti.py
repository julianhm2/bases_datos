# Programa para calcular el promedio de calificaciones y determinar los aprobados
def calcular_promedio(calificaciones):
    suma = 0
    contador = 0
    for calificacion in calificaciones:
        suma = suma + calificacion
        contador = contador + 1
    promedio = suma / contador
    return promedio

def listar_aprobados(estudiantes, calificaciones):
    aprobados = []
    for i in range(len(estudiantes)):
        if calificaciones[i] >= 6:
            aprobados.append(estudiantes[i])
    return aprobados

# Datos de entrada
estudiantes = ["Ana", "Luis", "María", "Carlos", "Sofía"]
calificaciones = [8, 5, 9, 6, 4]

# Calcular promedio
promedio = calcular_promedio(calificaciones)
print(f"Promedio general: {promedio}")

# Obtener lista de aprobados
aprobados = listar_aprobados(estudiantes, calificaciones)
print("Estudiantes aprobados:")
for aprobado in aprobados:
    print(aprobado)
