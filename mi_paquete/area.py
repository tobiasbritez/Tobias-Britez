import math

def area_circulo(radio=3):
    """Calcula el área de un círculo dado su radio. 
    Si no se proporciona, el radio por defecto es 3."""
    return math.pi * (radio ** 2)

def area_cuadrado(lado):
    """Calcula el área de un cuadrado dado el lado."""
    return lado ** 2

def area_triangulo(base, altura):
    """Calcula el área de un triángulo dado su base y altura."""
    return (base * altura) / 2
