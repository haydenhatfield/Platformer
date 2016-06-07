"""
platformer.py
Author: Hayden
Credit: Avery, Mr Denison
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

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
            
            
class FloorVertical(Floor):
    def __init__(self, position):
        super().__init__(position, "Floor.png")

class Floor2(Floor):
    def __init__(self, position):
        super().__init__(position, "TestPlatform.png")
        Platformer.listenKeyEvent("keydown", "d", self.moveRight)
        Platformer.listenKeyEvent("keydown", "a", self.moveLeft)
        
    def moveRight(self, event):
        self.x -= 1

    def moveLeft(self, event):
        self.x += 1
        

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
        self.scale  = 1
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
                
            """
        self.x += self.vx
        self.y += self.vy
        if self.movement == 1:
            self.setImage(self.moveframe)
            self.thrustframe += 1
            if self.movementframe == 4:
                self.movementframe = 1
        else:
            self.setImage(0)
        """

    def moveRight(self, event):
        self.x += 1

    def moveLeft(self, event):
        self.x -= 1



class Platformer(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        self.p = Player((200,200))
        self.fl = FloorVertical((100,300))
        self.f2 = FloorVertical((200,300))
        self.f3 = Floor2((100, 100))
        
    def step(self):
        self.p.step()
        self.fl.step()
        self.f2.step()
        self.f3.step()
    
    
myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()