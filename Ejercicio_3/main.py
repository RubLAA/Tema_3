from nave import NaveEspacial

def crear_naves():
    """Retorna la lista predefinida de naves espaciales."""
    return [
        NaveEspacial("Cometa Veloz", 150, 5, 50),
        NaveEspacial("Titán del Cosmos", 300, 10, 100),
        NaveEspacial("GX-2000", 200, 8, 80),
        NaveEspacial("GX-100", 100, 4, 30),
        NaveEspacial("Estrella Fugaz", 120, 3, 20),
        NaveEspacial("Galactica", 250, 15, 150),
        NaveEspacial("Nebulosa", 180, 6, 60),
        NaveEspacial("Andromeda", 220, 12, 90)
    ]

def imprimir_titulo(texto):
    """Imprime un título formateado para las tareas."""
    print(f"\n{'=' * 50}\n{texto}\n{'=' * 50}")

def imprimir_naves(naves, mensaje=None):
    """Imprime una lista de naves con un mensaje opcional."""
    if mensaje:
        print(mensaje)
    for nave in naves:
        print(nave)

def tarea1_ordenar(naves):
    """Ordena naves por nombre (asc) y longitud (desc)."""
    return sorted(naves, key=lambda x: (x.nombre, -x.longitud))

def tarea2_filtrar_por_nombre(naves, nombres):
    """Filtra naves por una lista de nombres específicos."""
    return [nave for nave in naves if nave.nombre in nombres]

def tarea3_top_pasajeros(naves, top=5):
    """Retorna las top naves con más pasajeros."""
    return sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:top]

def tarea4_max_tripulacion(naves):
    """Encuentra la nave con mayor tripulación."""
    return max(naves, key=lambda x: x.tripulantes)

def tarea5_filtrar_prefijo(naves, prefijo):
    """Filtra naves cuyo nombre comienza con un prefijo."""
    return [nave for nave in naves if nave.nombre.startswith(prefijo)]

def tarea6_filtrar_pasajeros(naves, minimo=6):
    """Filtra naves con capacidad de pasajeros >= mínimo."""
    return [nave for nave in naves if nave.pasajeros >= minimo]

def tarea7_naves_extremas(naves):
    """Retorna la nave más pequeña y más grande."""
    return (min(naves, key=lambda x: x.longitud), 
            max(naves, key=lambda x: x.longitud))

def main():
    naves = crear_naves()

    # Tarea 1: Ordenar por nombre y longitud
    imprimir_titulo("TAREA 1: Naves ordenadas por nombre (A-Z) y longitud (↓)")
    imprimir_naves(tarea1_ordenar(naves))

    # Tarea 2: Mostrar naves específicas
    imprimir_titulo("TAREA 2: Naves 'Cometa Veloz' y 'Titán del Cosmos'")
    nombres_buscados = ["Cometa Veloz", "Titán del Cosmos"]
    imprimir_naves(tarea2_filtrar_por_nombre(naves, nombres_buscados))

    # Tarea 3: Top 5 naves con más pasajeros
    imprimir_titulo("TAREA 3: Top 5 naves con más pasajeros")
    imprimir_naves(tarea3_top_pasajeros(naves))

    # Tarea 4: Nave con mayor tripulación
    imprimir_titulo("TAREA 4: Nave con mayor tripulación")
    print(tarea4_max_tripulacion(naves))

    # Tarea 5: Naves que comienzan con 'GX'
    imprimir_titulo("TAREA 5: Naves que comienzan con 'GX'")
    imprimir_naves(tarea5_filtrar_prefijo(naves, "GX"))

    # Tarea 6: Naves con 6+ pasajeros
    imprimir_titulo("TAREA 6: Naves con 6 o más pasajeros")
    imprimir_naves(tarea6_filtrar_pasajeros(naves))

    # Tarea 7: Nave más pequeña y grande
    imprimir_titulo("TAREA 7: Nave más pequeña y más grande")
    nave_min, nave_max = tarea7_naves_extremas(naves)
    print(f"► Más pequeña: {nave_min}\n► Más grande: {nave_max}")

if __name__ == "__main__":
    main()