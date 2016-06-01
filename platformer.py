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
    RedS = ImageAsset("RedScaffolding.png"
    Frame(2,0,3,6), 4)
    "sprtie position"
    Sprite(RedS, (0, 464))


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()