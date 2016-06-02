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
    Sprite(TT, (0, 200))
    TT = ImageAsset("PlayerTemplate1.png",
    Frame(19,0,17,33))
    Sprite(TT, (0, 300))


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()