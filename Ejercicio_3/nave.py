class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __repr__(self):
        return (f"Nombre: {self.nombre}, Longitud: {self.longitud}, "
                f"Tripulantes: {self.tripulantes}, Pasajeros: {self.pasajeros}")