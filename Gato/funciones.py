# Archivo con todas las funciones necesarias para la aplicacion linea

def calcular_y(x: float, m: float, b: float) -> float:
    return m * x + b

def test_lineas():
    # Verificamos que calcular_y funcione correctamente
    assert calcular_y(0, 2, 3) == 3
    assert calcular_y(1, 2, 3) == 5
    assert calcular_y(-1, 2, 3) == 1
    print("Pruebas exitosas")

if __name__ == '__main__':
    test_lineas()
