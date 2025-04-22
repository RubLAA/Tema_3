import pygame
import sys
from pygame.locals import *

class HanoiCalculator:
    def __init__(self, num_blocks):
        self.num_blocks = num_blocks
        self.total_moves = 2 ** num_blocks - 1  # Fórmula directa para Torre de Hanói
    
    def show_result(self):
        pygame.init()
        screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Resultado Final")
        
        font_title = pygame.font.Font(None, 48)
        font_result = pygame.font.Font(None, 72)
        font_instruction = pygame.font.Font(None, 32)
        
        # Configurar textos
        title_text = font_title.render("Puzzle de la Pirámide Egipcia", True, (255, 215, 0))
        result_text = font_result.render(f"{self.total_moves:,} movimientos", True, (255, 255, 255))
        instruction_text = font_instruction.render("Presiona cualquier tecla para salir", True, (200, 200, 200))
        
        # Posicionar textos
        title_rect = title_text.get_rect(center=(300, 100))
        result_rect = result_text.get_rect(center=(300, 200))
        instruction_rect = instruction_text.get_rect(center=(300, 320))
        
        running = True
        while running:
            screen.fill((40, 40, 60))  # Fondo oscuro
            
            # Dibujar textos
            screen.blit(title_text, title_rect)
            screen.blit(result_text, result_rect)
            screen.blit(instruction_text, instruction_rect)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    running = False
        
        pygame.quit()
        sys.exit()