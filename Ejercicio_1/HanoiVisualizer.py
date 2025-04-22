import pygame
import sys
from pygame.locals import *
from HanoiTower import HanoiTower

class HanoiVisualizer:
    def __init__(self, num_blocks, screen_width=800, screen_height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Pirámide de Piedras Preciosas')
        self.clock = pygame.time.Clock()
        self.num_blocks = num_blocks
        self.speed = 1
        self.running = True
        
        # Configuración de colores
        self.colors = {
            'background': (40, 40, 60),
            'tower': (120, 80, 60),
            'block': (255, 215, 0),
            'text': (255, 255, 255)
        }
        
        # Configurar torres
        tower_spacing = screen_width // 4
        self.towers = [
            HanoiTower(tower_spacing, screen_height - 50, 20, 400),
            HanoiTower(2 * tower_spacing, screen_height - 50, 20, 400),
            HanoiTower(3 * tower_spacing, screen_height - 50, 20, 400)
        ]
        
        # Inicializar con bloques de MAYOR (abajo) a MENOR (arriba)
        for i in range(num_blocks, 0, -1):
            self.towers[0].add_block(i * 25 + 15)  # Bloques más grandes primero
        
        self.moves = []
        self.current_move = 0
        self.animating = False
        self.generate_moves(num_blocks, 0, 2, 1)

    def show_initial_screen(self):
        font_large = pygame.font.Font(None, 74)
        font_small = pygame.font.Font(None, 36)
        
        total_steps = len(self.moves)
        text1 = font_large.render(f"Pasos Totales: {total_steps}", True, (255, 255, 255))
        text2 = font_small.render("Presiona ESPACIO para comenzar", True, (200, 200, 200))
        
        text1_rect = text1.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2 - 50))
        text2_rect = text2.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2 + 50))

        waiting = True
        while waiting:
            self.screen.fill(self.colors['background'])
            self.screen.blit(text1, text1_rect)
            self.screen.blit(text2, text2_rect)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        waiting = False
    
    def generate_moves(self, n, source, target, auxiliary):
        if n > 0:
            self.generate_moves(n-1, source, auxiliary, target)
            self.moves.append((source, target))
            self.generate_moves(n-1, auxiliary, target, source)
    
    def draw_block(self, x, y, width, height):
        # Dibuja bloque con sombra
        pygame.draw.rect(self.screen, self.colors['block'],
                         (x - width//2, y, width, height), 0, 5)
        pygame.draw.line(self.screen, (255, 223, 0),
                         (x - width//2 + 2, y), (x + width//2 - 2, y), 3)
    
    def draw_towers(self):
        for tower in self.towers:
            # Base de la torre
            pygame.draw.rect(self.screen, self.colors['tower'],
                             (tower.x - 60, tower.y - 20, 120, 40))
            # Poste
            pygame.draw.rect(self.screen, self.colors['tower'],
                             (tower.x - 10, tower.y - tower.height, 20, tower.height))
            
            # Dibuja bloques desde el MÁS GRANDE (abajo)
            y_pos = tower.y - 30
            for block in tower.blocks:  # Eliminar reversed() aquí
                self.draw_block(tower.x, y_pos, block, 25)
                y_pos -= 30
    
    def animate_move(self, source_idx, target_idx):
        source = self.towers[source_idx]
        target = self.towers[target_idx]
        block_width = source.top_block()
        
        # Animación de elevación
        start_y = source.y - 30 - 30 * (len(source.blocks) - 1)
        for y in range(start_y, 150, -5):
            self.update_display(source, target, source_idx, target_idx, block_width, y)
        
        # Movimiento horizontal
        start_x = source.x
        end_x = target.x
        step = 5 if end_x > start_x else -5
        for x in range(start_x, end_x, step):
            self.update_display(source, target, source_idx, target_idx, block_width, 150, x)
        
        # Descenso
        final_y = target.y - 30 - 30 * len(target.blocks)
        for y in range(150, final_y, 5):
            self.update_display(source, target, source_idx, target_idx, block_width, y, end_x)
        
        # Actualizar estado
        target.add_block(source.remove_block())
    
    def update_display(self, source, target, s_idx, t_idx, width, y, x=None):
        self.screen.fill(self.colors['background'])
        self.draw_towers()
        
        current_x = x if x is not None else source.x
        self.draw_block(current_x, y, width, 25)
        
        # Resaltado de torres
        for idx in [s_idx, t_idx]:
            pygame.draw.rect(self.screen, (255, 255, 0),
                            (self.towers[idx].x - 70, 50, 140, 40), 3)
        
        pygame.display.update()
        self.clock.tick(60)
    
    def draw_controls(self):
        font = pygame.font.Font(None, 28)
        text = font.render(f"Bloques: {self.num_blocks} | Velocidad: {self.speed}x | Movimientos: {self.current_move}/{2**self.num_blocks -1}", 
                          True, self.colors['text'])
        self.screen.blit(text, (10, 10))
    
    def run(self):
        self.show_initial_screen()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.speed = min(5, self.speed + 1)
                    elif event.key == K_LEFT:
                        self.speed = max(1, self.speed - 1)
                    elif event.key == K_r:
                        self.__init__(self.num_blocks)
                    elif event.key == K_ESCAPE:
                        self.running = False
            
            self.screen.fill(self.colors['background'])
            self.draw_towers()
            self.draw_controls()
            
            if self.current_move < len(self.moves) and not self.animating:
                self.animating = True
                source, target = self.moves[self.current_move]
                self.animate_move(source, target)
                self.current_move += 1
                self.animating = False
            
            pygame.display.update()
            self.clock.tick(60 * self.speed)
        
        pygame.quit()
        sys.exit()