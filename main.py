


import pygame
from pygame.locals import *
import random

SCREEN_WIDTH = 1560
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))

pygame.init()


FPS = 60
clock = pygame.time.Clock()


class player:
    def __init__(self,pos,size):
        self.alive = True
        self.pos = pos
        self.size = size
        self.color = "blue"
        self.rect = pygame.draw.rect(screen,"blue",(pos,size))
    
    def change_color(self):
        return random.choice(["blue","red","green"])
    
        
    def update(self):
        if self.alive:
            self.rect = pygame.draw.rect(screen,self.color,(self.pos,self.size))
        else:
            self.rect = pygame.draw.rect(screen,self.color,(-1000,-1000,self.size))
        



class Enemy:
    def __init__(self,pos):
        self.alive = True
        self.pos = pos
        self.size = [100,100]
        self.list = ["red","green","blue"]
        self.color = "blue"
        self.speed = 4
        
    def choice_color(self):
        num = random.randint(0,2)
        return self.list[num]
        
    def pos_x(self):
        return random.choice([70,320,570])
        
    def pos_y(self):
        return random.choice([150,-150,200,-200,320,-320])
         
        
    def show(self):
        if self.alive:
            self.rect = pygame.draw.rect(screen,self.color,(self.pos,self.size))
        self.pos[1] += self.speed
        

        

def event():
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            return 1
        if event.type == MOUSEBUTTONUP:
            return 2
        else:
            0
def reset_bot():
    for enemy in enemies:
        enemy.pos[1] = -100
        enemy.color = enemy.choice_color()
        enemy.pos[0] = enemy.pos_x()
        enemy.pos[1] = -100 + enemy.pos_y()

player = player([300,900],(100,100))

block_1 = Enemy([100,-100])
block_2 = Enemy([100,-100])
block_3 = Enemy([100,-100])
block_4 = Enemy([100,-100])
block_5 = Enemy([100,-100])
block_6 = Enemy([100,-100])
block_7 = Enemy([100,-100])
block_8 = Enemy([100,-100])
block_9 = Enemy([100,-100])
block_10 = Enemy([100,-100])

enemies = [block_1,block_2,block_3,block_4,block_5,block_6,block_7,block_8,block_9,block_10]

def main():
    
    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.play(-1)
    
    life = 1
    level = 1
    
    reset_bot()
        
    move = False
    
    player.color = player.change_color()
    
    font = pygame.font.Font('freesansbold.ttf',100)
    
    run = True 
    while run:
        
        Level = font.render(str(level),True,[0,0,0])
        
        if life >= 6:
            level += 1
            life = 1
            player.color = player.change_color()
        if life < 1:
            if level > 1:
                level -= 1
                life = 5
                player.color = player.change_color()
            else:
                player.alive = False
            
        if level > 22:
            level = 22
            life = 5
        if level == 22:
            for enemy in enemies:
                enemy.speed = 8
        else:
            for enemy in enemies:
                enemy.speed = 4
        
        pos = pygame.mouse.get_pos()
        
        bg = pygame.draw.rect(screen,[220 - (level * 10),220 - (level * 10),220 - (level * 10)],(0,0,720,1560))
        
        
        if player.alive:   
            for enemy in enemies:
                enemy.show()
                
                if enemy.pos[1] > 1600:
                    enemy.pos[1] = -100
                    enemy.color = enemy.choice_color()
                    enemy.pos[0] = enemy.pos_x()
                    enemy.pos[1] = -100 + enemy.pos_y()
                    for i in enemies:
                        i.alive = True
                        reset_bot
        
        
        nav = pygame.draw.rect(screen,[150,150,150],(0,1100,720,660))
        left = pygame.draw.rect(screen,[0,0,0],(100,1200,150,200))
        right = pygame.draw.rect(screen,[0,0,0],(470,1200,150,200))
        
        
        
        ev = event()
        
        if player.pos[0] < 0:
            player.pos[0] = 0
        if player.pos[0] > 620:
            player.pos[0] = 620
            
        if ev == 1:
            move = True
        if ev == 2:
            move = False
        
        if move:
            if left.collidepoint(pos):
                player.pos[0] -= 5
            if right.collidepoint(pos):
                player.pos[0] += 5
        
        for enemy in enemies:
            if enemy.rect.colliderect(player.rect) and enemy.alive:
                if enemy.color == player.color:
                    life += 1
                if enemy.color != player.color:
                    life -= 1
                enemy.alive = False
                enemy.pos[0] = -100
                enemy.pos[1] = -500
        
        
        
        player.update()
        
        life_dist = 0
        for i in range(life):
            pygame.draw.rect(screen,[0,255,255],(250 + life_dist,1150,20,30))
            life_dist += 40
            
        screen.blit(Level,(player.pos[0],player.pos[1]))
        
        pygame.display.update()
    
    
if __name__ == "__main__":
    main()

