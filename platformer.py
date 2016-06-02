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

class Player(Sprite):
    TT = ImageAsset("PlayerTemplate1.png",
    Frame(0,0,17,33))

    def __init__(self, position):
        super().__init__(Player.TT, position)
        Platformer.listenKeyEvent("keypress", "D", self.moveRight)
        Platformer.listenKeyEvent("keypress", "A", self.moveLeft)
        self.fxcenter = self.fycenter = 0.5
        
    def step(self):
        pass
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
        self.p = Player((40,40))
        
    def step(self):
        self.p.step()
    
    
myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()