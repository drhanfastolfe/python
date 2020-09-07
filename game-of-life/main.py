import sys, pygame
pygame.init()

size = width, height = 600, 600

nX_cells = 60
nY_cells = 60

dimCW = (width - 1) / nX_cells
dimCH = (height - 1) / nY_cells

bg = 25, 25, 25

screen = pygame.display.set_mode(size)

screen.fill(bg)

while 1:
    
    for i in range(1, nY_cells + 1):
        for j in range(1, nX_cells + 1):
            poly = [((j - 1) * dimCW, (i -1) * dimCH),
                    ((j) * dimCW, (i - 1) * dimCH),
                    ((j) * dimCW, (i) * dimCH),
                    ((j - 1) * dimCW, (i) * dimCH)]
            
            pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            
    pygame.display.flip()