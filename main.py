import pygame
import math
import random

lista = [1]
for i in range(100):
    lista.append(random.randint(0, 10000))

size = (500, 500)
bgcolor=(0,0,0)
color = (0, 200, 0)

pygame.init()
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
running = True
method = None

while running:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                method = None
            elif event.key == pygame.K_r:
                method = None
                lista = []
                for i in range(100):
                    lista.append(random.randint(0, 10000))
            elif event.key == pygame.K_b:
                method = "bubble"
                idx = 0
            elif event.key == pygame.K_s:
                method = "selection"
                idx = 0
                idxDone = 0
            elif event.key == pygame.K_i:
                method = "insertion"
                idx = 1

    if method == "bubble":
        if idx == len(lista)-1:
            idx = 0
        if lista[idx+1]<lista[idx]:
            lista[idx+1], lista[idx] = lista[idx], lista[idx+1]
        idx += 1

    elif method == "selection":
        if idxDone == len(lista)-1:
            method = None
        minIdx = idxDone
        for i in range(len(lista)-idxDone):
            if lista[i+idxDone]<lista[minIdx]:
                minIdx=i+idxDone
        lista[idxDone], lista[minIdx] = lista[minIdx], lista[idxDone]
        idxDone += 1
        clock.tick(30)

    elif method == "insertion":
        tmp = lista[idx]
        for i in range(len(lista[:idx])):
            if lista[idx-i-1]>lista[idx-i]:
                lista[idx-i-1], lista[idx-i] = lista[idx-i], lista[idx-i-1]
        idx+=1
        if idx==len(lista):
            method = None

    l = size[0]/len(lista)
    d = size[1]/max(lista)
    h = 0

    for i in lista:
        pygame.draw.rect(screen, color, (int(h*l), size[1]-d*i, math.ceil(l), d*i))
        h+=1
    
    pygame.display.update()
