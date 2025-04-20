import pygame
pygame.init()
import random



RECTANGLE_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (255,255,255)


screen = pygame.display.set_mode((640,480))

top_left = (0, 0 )
size = (0,0)
dragging = False

rectangles = [ ]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            top_left = event.pos
            size = 0, 0
            dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            right_bottom = event.pos
            size = right_bottom[0] - top_left[0], right_bottom[1] - top_left[1]
            dragging = False
            rect = pygame.Rect(top_left, size)
            color = (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255) )
            rectangles.append((rect, color))

        elif event.type == pygame.MOUSEMOTION and dragging:
            right_bottom = event.pos
            size = right_bottom[0] - top_left[0], right_bottom[1] - top_left[1]


    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, RECTANGLE_COLOR, (top_left, size), 1)
    for rectangle, color in rectangles:
        pygame.draw.rect(screen, color, rectangle, 1)

    pygame.display.flip()
pygame.quit()

