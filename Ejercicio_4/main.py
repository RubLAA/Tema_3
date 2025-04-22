from polinomio import Polinomio

def imprimir_prueba(titulo, funcion_prueba):
    print(f"\n{'='*50}\n{titulo}\n{'='*50}")
    funcion_prueba()
    print("✓ Prueba completada\n")

def main():
    # Creación de polinomios de prueba
    p1 = Polinomio([(3, 2), (2, 1), (5, 0)])   # 3x² + 2x + 5
    p2 = Polinomio([(1, 2), (-4, 1), (1, 0)])  # x² - 4x + 1
    p3 = Polinomio([(2, 3), (3, 2), (-1, 1), (4, 0)])  # 2x³ + 3x² - x + 4
    divisor = Polinomio([(1, 2), (1, 0)])      # x² + 1
    p4 = Polinomio([(4, 3), (-2, 1), (7, 0)])  # 4x³ - 2x + 7

    def prueba_resta():
        print("Polinomio 1:", p1)
        print("Polinomio 2:", p2)
        resultado = p1.restar(p2)
        print("\nResultado resta:", resultado)

    # En la prueba de división del main.py
    def prueba_division():
        dividendo = Polinomio([(2.0, 3), (3.0, 2), (-1.0, 1), (4.0, 0)])  # 2x³ + 3x² - x + 4
        divisor = Polinomio([(1.0, 2), (1.0, 0)])  # x² + 1
        print("Dividendo:", dividendo)
        print("Divisor:", divisor)
        cociente, resto = dividendo.dividir(divisor)
        print("\nCociente:", cociente)
        print("Resto:", resto)

    def prueba_eliminar_termino():
        print("Polinomio original:", p4)
        modificado = p4.eliminar_termino(-2, 1)
        print("\nDespués de eliminar -2x:", modificado)

    def prueba_contiene_termino():
        print("Polinomio:", p4)
        print("\n¿Contiene 4x³?", p4.contiene_termino(4, 3))
        print("¿Contiene 5x²?", p4.contiene_termino(5, 2))

    def prueba_division_por_cero():
        print("Intentando dividir por cero...")
        try:
            cero = Polinomio([])
            p1.dividir(cero)
        except ZeroDivisionError as e:
            print(f"Error capturado: {e}")

    # Ejecutar todas las pruebas
    imprimir_prueba("PRUEBA DE RESTA DE POLINOMIOS", prueba_resta)
    imprimir_prueba("PRUEBA DE DIVISIÓN DE POLINOMIOS", prueba_division)
    imprimir_prueba("PRUEBA DE ELIMINACIÓN DE TÉRMINO", prueba_eliminar_termino)
    imprimir_prueba("PRUEBA DE EXISTENCIA DE TÉRMINO", prueba_contiene_termino)
    imprimir_prueba("PRUEBA DE DIVISIÓN POR CERO", prueba_division_por_cero)

if __name__ == "__main__":
    main()