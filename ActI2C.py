#Actividad I2C

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time
i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp.fill(0)
disp.show()
width = disp.width
height = disp.height



def imprimeNombres():
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.rectangle((200,200,width,height), outline=300, fill=270)
    #draw.line((5,15, 100, 15), fill=270)
    #draw.line((5,50, 100, 50), fill=270)
    draw.text((15, 10), 'José Diego', font=font, fill=270)
    disp.image(image)
    disp.show()
    time.sleep(2)
    draw.text((15, 20), 'Pamela', font=font, fill=270)
    disp.image(image)
    disp.show()
    time.sleep(2)
    draw.text((15, 30), 'Victor Manuel', font=font, fill=270)
    disp.image(image)
    disp.show()
    time.sleep(2)
    draw.text((15, 40), 'Ángel', font=font, fill=270)
    disp.image(image)
    disp.show()


def terminal():
    image2 = Image.new('1', (width, height))
    draw2 = ImageDraw.Draw(image2)
    font = ImageFont.load_default()
    draw2.rectangle((200,200,width,height), outline=300, fill=270)
    mensaje = input("Escribe un mensaje : ")
    draw2.text((40, 20), mensaje, font=font, fill=270)
    disp.image(image2)
    disp.show()

imprimeNombres()
terminal()
