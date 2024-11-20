# Programa optimizado para calcular el promedio y listar aprobados
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

def listar_aprobados(estudiantes, calificaciones):
    # Usando una lista por comprensión y zip para iterar eficientemente
    return [estudiante for estudiante, calificacion in zip(estudiantes, calificaciones) if calificacion >= 6]

# Datos de entrada
estudiantes = ["Ana", "Luis", "María", "Carlos", "Sofía"]
calificaciones = [8, 5, 9, 6, 4]

# Calcular promedio
promedio = calcular_promedio(calificaciones)
print(f"Promedio general: {promedio:.2f}")

# Obtener lista de aprobados
aprobados = listar_aprobados(estudiantes, calificaciones)
print("Estudiantes aprobados:", ", ".join(aprobados))
