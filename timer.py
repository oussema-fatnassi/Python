import pygame
import time

WIDTH, HEIGHT = 800, 200

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timer")
clock = pygame.time.Clock()
FPS = 60

RED = (255, 0, 0)
BLACK = (0, 0, 0)

def timer(time):
    time_str = "{:03d}".format(time)
    font = pygame.font.Font("DS-DIGIT.TTF", 100)
    text = font.render(time_str, True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.fill(BLACK)
    screen.blit(text, text_rect)
    pygame.display.update(text_rect)

def main():
    start = time.time()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        passed_time = int(time.time() - start)

        screen.fill(BLACK)
        timer(passed_time)
        pygame.display.update()
        clock.tick(FPS)

main()