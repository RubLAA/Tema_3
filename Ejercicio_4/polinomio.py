class Polinomio:
    def __init__(self, terminos):
        self.terminos = {}
        for coeficiente, exponente in terminos:
            self.terminos[exponente] = self.terminos.get(exponente, 0) + coeficiente
        # Eliminar términos con coeficiente cero
        self.terminos = {exp: coeff for exp, coeff in self.terminos.items() if coeff != 0}
    
    @classmethod
    def desde_diccionario(cls, diccionario):
        polinomio = cls([])
        polinomio.terminos = diccionario.copy()
        return polinomio
    
    def copiar(self):
        return Polinomio.desde_diccionario(self.terminos)
    
    def restar(self, otro):
        resultado = self.terminos.copy()
        for exp, coeff in otro.terminos.items():
            resultado[exp] = resultado.get(exp, 0) - coeff
            if resultado[exp] == 0:
                del resultado[exp]
        return Polinomio.desde_diccionario(resultado)
    
    def multiplicar(self, otro):
        resultado = {}
        for exp1, coeff1 in self.terminos.items():
            for exp2, coeff2 in otro.terminos.items():
                exp = exp1 + exp2
                coeff = coeff1 * coeff2
                resultado[exp] = resultado.get(exp, 0) + coeff
        # Eliminar términos con coeficiente cero
        resultado = {exp: coeff for exp, coeff in resultado.items() if coeff != 0}
        return Polinomio.desde_diccionario(resultado)
    
    def dividir(self, divisor):
        if divisor.es_cero():
            raise ZeroDivisionError("No se puede dividir por un polinomio cero.")
        cociente = Polinomio([])
        resto = self.copiar()
        divisor_coeff_lider, divisor_exp_lider = divisor.termino_lider()
        while not resto.es_cero() and resto.grado() >= divisor_exp_lider:
            resto_coeff_lider, resto_exp_lider = resto.termino_lider()
            # Calcular término del cociente
            cociente_coeff = resto_coeff_lider / divisor_coeff_lider
            cociente_exp = resto_exp_lider - divisor_exp_lider
            # Crear polinomio con el término del cociente
            termino_cociente = Polinomio([(cociente_coeff, cociente_exp)])
            cociente = cociente.sumar(termino_cociente)
            # Restar (divisor * término del cociente) del resto
            divisor_por_termino = divisor.multiplicar(termino_cociente)
            resto = resto.restar(divisor_por_termino)
        return cociente, resto
    
    def sumar(self, otro):
        resultado = self.terminos.copy()
        for exp, coeff in otro.terminos.items():
            resultado[exp] = resultado.get(exp, 0) + coeff
            if resultado[exp] == 0:
                del resultado[exp]
        return Polinomio.desde_diccionario(resultado)
    
    def es_cero(self):
        return not self.terminos
    
    def grado(self):
        if self.es_cero():
            return float('-inf')
        return max(self.terminos.keys())
    
    def termino_lider(self):
        if self.es_cero():
            return (0, float('-inf'))
        max_exp = self.grado()
        return (self.terminos[max_exp], max_exp)
    
    def eliminar_termino(self, coeficiente, exponente):
        termino = Polinomio([(coeficiente, exponente)])
        return self.restar(termino)
    
    def contiene_termino(self, coeficiente, exponente):
        return self.terminos.get(exponente, 0) == coeficiente
    
    def __str__(self):
        if not self.terminos:
            return "0"
        terminos_ordenados = sorted(self.terminos.items(), key=lambda x: -x[0])
        partes = []
        for exp, coeff in terminos_ordenados:
            # Convertir coeficiente a float para verificar decimales
            coeff_float = float(coeff)
            if exp == 0:
                part = f"{int(coeff_float)}" if coeff_float.is_integer() else f"{coeff_float}"
            elif exp == 1:
                part = f"{int(coeff_float)}x" if coeff_float.is_integer() else f"{coeff_float}x"
            else:
                part = f"{int(coeff_float)}x^{exp}" if coeff_float.is_integer() else f"{coeff_float}x^{exp}"
            partes.append(part)
        # Manejar coeficientes negativos
        cadena = " + ".join(partes).replace("+ -", " - ")
        if cadena.startswith("- "):
            cadena = "-" + cadena[2:]
        return cadena