import pygame

# pygame.init()
# screen = pygame.display.set_mode([500, 500])
# pygame.display.set_caption("Hola Mundo")
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.MOUSEBUTTONDOWN:
#                 print(event.pos)
#     screen.fill((255,255,255))
#     pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
#     # pygame.draw.rect(screen, (255, 255, 0), (30, 30, 100, 100))
#     pygame.display.flip()
# pygame.quit()
for x in range(0, 4 * 200, 200):
    for y in range(0, 4 * 200, 200):
        print(x, y)         