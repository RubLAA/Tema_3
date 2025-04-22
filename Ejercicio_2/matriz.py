class Matriz:
    """Clase para calcular el determinante de una matriz cuadrada usando métodos iterativo y recursivo.
    
    Atributos:
        matriz (list): Lista de listas representando la matriz cuadrada.
        n (int): Tamaño de la matriz (n x n).
    """
    
    def __init__(self, matriz):
        """Inicializa la matriz con validación de matriz cuadrada.
        
        Args:
            matriz (list): Lista de listas representando una matriz.
            
        Raises:
            ValueError: Si la matriz no es cuadrada.
        """
        if not all(len(fila) == len(matriz) for fila in matriz):
            raise ValueError("La matriz debe ser cuadrada.")
        self.matriz = matriz
        self.n = len(matriz)
    
    def determinante_iterativo(self):
        """Calcula el determinante para matrices 3x3 usando el método iterativo (fórmula directa).
        
        Returns:
            int/float: Valor del determinante.
            
        Raises:
            ValueError: Si la matriz no es 3x3.
        """
        if self.n != 3:
            raise ValueError("El método iterativo requiere una matriz 3x3.")
        
        a, b, c = self.matriz[0]
        d, e, f = self.matriz[1]
        g, h, i = self.matriz[2]
        
        return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    
    def determinante_recursivo(self):
        """Calcula el determinante usando recursión (expansión por cofactores).
        
        Returns:
            int/float: Valor del determinante.
        """
        return self._calculo_recursivo(self.matriz)
    
    def _calculo_recursivo(self, m):
        """Método auxiliar recursivo para calcular el determinante.
        
        Args:
            m (list): Submatriz en cada paso recursivo.
            
        Returns:
            int/float: Determinante calculado.
        """
        tam = len(m)
        if tam == 1:
            return m[0][0]
        if tam == 2:
            return m[0][0]*m[1][1] - m[0][1]*m[1][0]
        
        det = 0
        for j in range(tam):
            menor = [fila[:j] + fila[j+1:] for fila in m[1:]]  # Excluye fila 0 y columna j
            signo = (-1) ** j
            det += signo * m[0][j] * self._calculo_recursivo(menor)
        return det