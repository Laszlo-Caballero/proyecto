from PIL import ImageFont
from tkinter import font

class Font:
    def __init__(self, parent, size , Font):
        self.LoadFont = ImageFont.truetype(f"./font/Flexo-{Font}-webfont.ttf", size= size)
        self.Font = font.Font(parent, family=self.LoadFont, size=size)