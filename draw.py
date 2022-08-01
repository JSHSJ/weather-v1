from curses import COLOR_WHITE
from PIL import Image,ImageDraw,ImageFont

width = 400
height = 300

Font_REGULAR = "./WorkSans-Regular.otf"
Font_BOLD = "./WorkSans-SemiBold.otf"
Font_MONO = "./MDIO0.4-Regular.otf"

COLOR_WHITE = (255,255,255)

temp = "25.5"
rainHour = "0.5"
rainTotal = "400.2"
windSpeed = "1.2"
windDirection = "205"

def drawArrow(dir: int):
    arrowLength = 8
    al = arrowLength / 2
    aw = arrowLength / 10
    off = arrowLength / 5
    image = Image.new('1', (arrowLength + 8, arrowLength + 8), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)
    x = 8
    y = al

    p1 = (x - aw, y - al)
    p2 = (x + aw, y - al)

    p3 = (x + aw, y + arrowLength - al)

    p4 = (x + aw + off, y + arrowLength - al - off)
    p5 = (x + aw + off + aw, y + arrowLength - al - off)

    p6 = (x + aw, y + arrowLength + off)
    p7 = (x - aw, y + arrowLength + off)

    p8 = (x - aw - off - aw, y + arrowLength - al - off)
    p9 = (x - aw - off, y + arrowLength - al - off)

    p10 = (x - aw, y + arrowLength - al)

    draw.polygon([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10], fill=0)

    if (dir >= 0 and dir < 45):
        return image
    elif (dir >= 45 and dir < 90):
        return image.rotate(-45, fillcolor=255, expand=True)
    elif (dir >= 90 and dir < 135):
        return image.rotate(-90, fillcolor=255, expand=True)
    elif (dir >= 135 and dir < 180):
        return image.rotate(-135, fillcolor=255, expand=True)
    elif (dir >= 180 and dir < 225):
        return image.rotate(-180, fillcolor=255, expand=True)
    elif (dir >= 225 and dir < 270):
        return image.rotate(-225, fillcolor=255, expand=True)
    elif (dir >= 270 and dir < 315):
        return image.rotate(-270, fillcolor=255, expand=True)
    elif (dir >= 315 and dir < 360):
        return image.rotate(-315, fillcolor=255, expand=True)

     
   




if __name__=='__main__':
  image = Image.new('1', (width, height), 255)  # 255: clear the frame
  draw = ImageDraw.Draw(image)

  fontLabel = ImageFont.truetype(Font_MONO, 12)
  

  # Draw temperature rectangle
  draw.rectangle((40, 40, 360, 110), outline=0, width=2)
  tempTextSize = draw.textlength("Temperatur", font = fontLabel)
  draw.rectangle((50, 30, 50 + tempTextSize + 12, 50), fill = 255)
  draw.text((56, 32), "Temperatur", font = fontLabel, fill = 0)

  # Draw temperature value

  # Get length of temperature string
  font = ImageFont.truetype(Font_BOLD, 40)
  # Get width of temperature string
  tempTextSize = draw.textlength(temp, font = font)
  # Draw temperature value centered left of middle
  draw.text(((width / 2) - tempTextSize - 6, 48), temp, font = font, fill = 0)
  font = ImageFont.truetype(Font_REGULAR, 30)
  draw.text(((width / 2) + 6, 60), "°C", font = font, fill = 0)


  # Draw rain rectangle
  draw.rectangle((40, 130, 190, 270), outline=0, width=1)
  tempTextSize = draw.textlength("Regen", font = fontLabel)
  draw.rectangle((50, 120, 50 + tempTextSize + 12, 140), fill = 255)
  draw.text((56, 122), "Regen", font = fontLabel, fill = 0)

  fontValue = ImageFont.truetype(Font_BOLD, 14)
  fontValueUnit = ImageFont.truetype(Font_REGULAR, 12)

  # Draw rain value

  draw.text((56, 156), "Nächste Stunde", font = fontLabel, fill = 0)
  draw.text((56, 174), rainHour, font = fontValue, fill = 0)
  tempTextSize = draw.textlength(rainHour, font = fontValue)
  draw.text((56 + tempTextSize + 6, 175), "ml / m³", font = fontValueUnit, fill = 0)

  draw.text((56, 210), "16 Stunden", font = fontLabel, fill = 0)
  draw.text((56, 228), rainTotal, font = fontValue, fill = 0)
  tempTextSize = draw.textlength(rainTotal, font = fontValue)
  draw.text((56 + tempTextSize + 6, 229), "ml / m³", font = fontValueUnit, fill = 0)

   # Draw wind rectangle
  draw.rectangle((210, 130, 360, 270), outline=0, width=1)
  tempTextSize = draw.textlength("Wind", font = fontLabel)
  draw.rectangle((220, 120, 220 + tempTextSize + 12, 140), fill = 255)
  draw.text((226, 122), "Wind", font = fontLabel, fill = 0)

  # Draw wind value

  draw.text((226, 156), "Geschwindigkeit", font = fontLabel, fill = 0)
  draw.text((226, 174), windSpeed, font = fontValue, fill = 0)
  tempTextSize = draw.textlength(windSpeed, font = fontValue)
  draw.text((226 + tempTextSize + 6, 175), "km/h", font = fontValueUnit, fill = 0)

  draw.text((226, 210), "Richtung", font = fontLabel, fill = 0)
  i = drawArrow(int(windDirection))
  image.paste(i, (230, 232))

  image.show()


    
    


