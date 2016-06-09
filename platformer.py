"""
platformer.py
Author: Hayden
Credit: Avery, Mr Denison
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 10000
SCREEN_HEIGHT = 800

# Background
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
bg = Sprite(bg_asset, (0,0))


class GravitySprite(Sprite):
    
    G = 50.0

    def __init__(self, asset, position, velocity):
        super().__init__(asset, position)
        self.vx = velocity[0]
        self.vy = velocity[1]
        self.mass = 1.0
        self.gravity = 1
        
    def step(self):
       self.x += self.vx
       self.vy += self.gravity
       self.y+= self.vy
       
       
class Floor(Sprite):

    
    def __init__(self, postion, BitMap):
        fl = ImageAsset(BitMap)
        super().__init__(fl, postion)
        
    def step(self):
        csprites = self.collidingWithSprites(Player)
        if len(csprites) > 0:
            csprites[0].vy = -1
            
            
class VerticalLinkPipe(Floor):
    def __init__(self, position):
        super().__init__(position, "VerticalLinkPipe.png")
        Platformer.listenKeyEvent("keydown", "d", self.moveRight)
        Platformer.listenKeyEvent("keydown", "a", self.moveLeft)
        
    def moveRight(self, event):
        self.x -= 2

    def moveLeft(self, event):
        self.x += 2

class MetalBlock20x20(Floor):
    def __init__(self, position):
        super().__init__(position, "MetalBlock20x20.png")
        Platformer.listenKeyEvent("keydown", "d", self.moveRight)
        Platformer.listenKeyEvent("keydown", "a", self.moveLeft)
        
    def moveRight(self, event):
        self.x -= 2

    def moveLeft(self, event):
        self.x += 2
        
class MetalPipeHorizantal103x20(Floor):
    def __init__(self, position):
        super().__init__(position, "MetalPipeHorizantal103x20.png")
        Platformer.listenKeyEvent("keydown", "d", self.moveRight)
        Platformer.listenKeyEvent("keydown", "a", self.moveLeft)
        
    def moveRight(self, event):
        self.x -= 2

    def moveLeft(self, event):
        self.x += 2

class MetalPipeVertical20x103(Floor):
    def __init__(self, position):
        super().__init__(position, "MetalPipeVertical20x103.png")
        Platformer.listenKeyEvent("keydown", "d", self.moveRight)
        Platformer.listenKeyEvent("keydown", "a", self.moveLeft)
        
    def moveRight(self, event):
        self.x -= 2

    def moveLeft(self, event):
        self.x += 2

class MetalPipeHorizantal296x20(Floor):
    def __init__(self, position):
        super().__init__(position, "MetalPipeHorizantal296x20.png")
        Platformer.listenKeyEvent("keydown", "d", self.moveRight)
        Platformer.listenKeyEvent("keydown", "a", self.moveLeft)
        
    def moveRight(self, event):
        self.x -= 2

    def moveLeft(self, event):
        self.x += 2

class MetalPipeVertical20x296(Floor):
    def __init__(self, position):
        super().__init__(position, "MetalPipeVertical20x296.png")
        Platformer.listenKeyEvent("keydown", "d", self.moveRight)
        Platformer.listenKeyEvent("keydown", "a", self.moveLeft)
        
    def moveRight(self, event):
        self.x -= 2

    def moveLeft(self, event):
        self.x += 2

class MetalPipeHorizantal72x20(Floor):
    def __init__(self, position):
        super().__init__(position, "MetalPipeHorizantal72x20.png")
        Platformer.listenKeyEvent("keydown", "d", self.moveRight)
        Platformer.listenKeyEvent("keydown", "a", self.moveLeft)
        
    def moveRight(self, event):
        self.x -= 2

    def moveLeft(self, event):
        self.x += 2

class MetalPipeVertical20x172(Floor):
    def __init__(self, position):
        super().__init__(position, "MetalPipeVertical20x172.png")
        Platformer.listenKeyEvent("keydown", "d", self.moveRight)
        Platformer.listenKeyEvent("keydown", "a", self.moveLeft)
        
    def moveRight(self, event):
        self.x -= 2

    def moveLeft(self, event):
        self.x += 2
        

class Player(GravitySprite):
    TT = ImageAsset("PlayerTemplateScaledFixed.png",
    Frame(0,0,66,128), 12, "horizontal")

    def __init__(self, position):
        super().__init__(Player.TT, position, (0, 0))
        

        
        self.mass = 30*1000
        self.fxcenter = 0.5
        self.fycenter = 0.5
        
        self.tickCount = 0
        Platformer.listenKeyEvent("keydown", "d", self.moveRight)
        Platformer.listenKeyEvent("keydown", "a", self.moveLeft)
        self.fxcenter = self.fycenter = 0.5
        self.scale  = .65
        self.imagecount = 0
        self.AD = 1
        
    def step(self):
        super().step()
        
        
        self.tickCount += 1
        if self.tickCount %5 == 0:
            self.imagecount += self.AD
            
            if self.imagecount >=11:
                self.AD *= -1
            self.setImage(self.imagecount)
            if self.imagecount == 0:
                self.AD += 1

    def moveRight(self, event):
        self.x += 2

    def moveLeft(self, event):
        self.x -= 2



class Platformer(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        self.p = Player((200,300))
        self.f1 = MetalPipeHorizantal296x20((34,199))
        self.f2 = MetalPipeHorizantal296x20((5,349))
        self.f3 = MetalPipeHorizantal296x20((589,349))
        self.f4 = MetalPipeHorizantal296x20((865,433))
        self.f5 = MetalPipeHorizantal296x20((1139,518))
        self.f6 = MetalPipeHorizantal296x20((1413,602))
        self.f7 = MetalPipeHorizantal296x20((1687,518))
        
    def step(self):
        self.p.step()
        self.f1.step()
        self.f2.step()
        self.f3.step()
        self.f4.step()
        self.f5.step()
        self.f6.step()
        self.f7.step()

    
    
myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()