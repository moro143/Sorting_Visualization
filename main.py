import pygame
import math
import numpy as np
import random

class SortingVisualization:
    def __init__(self):
        self.listToSort = [1]
    
    def randomize(self, length = 100, maximal=10000):
        self.listToSort = []
        for _ in range(length):
            self.listToSort.append(random.randint(0, maximal))

    def visualize(self, size=(500, 500), color=np.array([0, 200, 0]), bgcolor=(0,0,0)):
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
                        self.randomize()
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
                if idx == len(self.listToSort)-1:
                    idx = 0
                if self.listToSort[idx+1]<self.listToSort[idx]:
                    self.listToSort[idx+1], self.listToSort[idx] = self.listToSort[idx], self.listToSort[idx+1]
                idx += 1

            elif method == "selection":
                if idxDone == len(self.listToSort)-1:
                    method = None
                minIdx = idxDone
                for i in range(len(self.listToSort)-idxDone):
                    if self.listToSort[i+idxDone]<self.listToSort[minIdx]:
                        minIdx=i+idxDone
                self.listToSort[idxDone], self.listToSort[minIdx] = self.listToSort[minIdx], self.listToSort[idxDone]
                idxDone += 1
                clock.tick(30)

            elif method == "insertion":
                tmp = self.listToSort[idx]
                for i in range(len(self.listToSort[:idx])):
                    if self.listToSort[idx-i-1]>self.listToSort[idx-i]:
                        self.listToSort[idx-i-1], self.listToSort[idx-i] = self.listToSort[idx-i], self.listToSort[idx-i-1]
                idx+=1
                if idx==len(self.listToSort):
                    method = None
                clock.tick(30)

            l = size[0]/len(self.listToSort)
            d = size[1]/max(self.listToSort)
            h = 0
            for i in self.listToSort:
                pygame.draw.rect(screen, color*i/max(self.listToSort), (int(h*l), size[1]-d*i, math.ceil(l), d*i))
                h+=1
            
            pygame.display.update()

test = SortingVisualization()
test.randomize(500, 500)
test.visualize((1000,500))