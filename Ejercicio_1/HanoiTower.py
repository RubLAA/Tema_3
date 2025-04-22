class HanoiTower:
    def __init__(self, x, y, base_width, height):
        self.x = x
        self.y = y
        self.base_width = base_width
        self.height = height
        self.blocks = []  # Lista de mayor (abajo) a menor (arriba)
    
    def add_block(self, width):
        self.blocks.append(width)  # Ahora añade al final (arriba)
    
    def remove_block(self):
        return self.blocks.pop()  # Quita el bloque superior
    
    def top_block(self):
        return self.blocks[-1] if self.blocks else 0