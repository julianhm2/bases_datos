# Programa para calcular el área y el perímetro de un rectángulo
def calcular_area(base, altura):
    # Error: 'resultado' no se inicializa correctamente
    resultado = base * altura
    return area  # Error: la variable 'area' no está definida, debería ser 'resultado'

def calcular_perimetro(base, altura):
    # Error: Suma incorrecta, debería ser 2 * (base + altura)
    perimetro = base + altura * 2
    return perimetro

# Datos de entrada
base = 10
altura = "5"  # Error: 'altura' es un string, no un número

# Cálculo del área
area = calcular_area(base, altura)  # Error: mezcla de tipos incompatibles
print(f"El área del rectángulo es: {area}")

# Cálculo del perímetro
perimetro = calcular_perimetro(base, altura)
print(f"El perímetro del rectángulo es: {perimetro}")
