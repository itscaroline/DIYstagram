#100 pixel boarder
from PIL import Image
import math
img = Image.open("london.jpg")

height = img.size[1]
width = img.size[0]

print img.size
print (height)
print (width)

for y in range(height):
    for x in range(width):
        distance = math.sqrt((height - y)**2 + (width - x)**2)
        rgb_value = img.getpixel((x, y))
        ratio = distance / max(height, width)
        change_factor = (250-distance) / 500

        if (x > 100 and x < (width) - 100) and (y > 100 and y < (height)-100 ):
            red = int(rgb_value[0] + 0)
            green = int(rgb_value[1] + 25)
            blue = int(rgb_value[2] + 0)

        else:
            red = int(rgb_value[0] * ratio)
            green = int(rgb_value[1] * ratio)
            blue = int(rgb_value[2] * ratio)

        img.putpixel ((x,y), (red, green, blue))

img.save ('output.jpg')
print "Done making new image!"




# cute little black boarder
from PIL import Image
import math
img = Image.open("london.jpg")

height = img.size[1]
width = img.size[0]

print img.size
print (height)
print (width)

for y in range(height):
    for x in range(width):
        distance = math.sqrt((height - y)**2 + (width - x)**2)
        rgb_value = img.getpixel((x, y))
        #ratio = distance / max(height, width)
        change_factor = (250-distance) / 500

       if (x > 30 and x < (width) - 30) and (y > 30 and y < (height)- 30 ):
            red = int(rgb_value[0] + 20)
            green = int(rgb_value[1] + 10)
            blue = int(rgb_value[2] + 0)

        else:
            red = int(rgb_value[0] * 0)
            green = int(rgb_value[1] * 0)
            blue = int(rgb_value[2] * 0)

        img.putpixel ((x,y), (red, green, blue))

img.save ('output.jpg')
print "Done making new image!"


     
   

#Watermelon Party
from PIL import Image
import math
img = Image.open("london.jpg")

height = img.size[1]
width = img.size[0]

print img.size
print (height)
print (width)

for y in range(height):
    for x in range(width):
        distance = math.sqrt((height - y)**2 + (width - x)**2)
        rgb_value = img.getpixel((x, y))
        #ratio = distance / max(height, width)
        change_factor = (250-distance) / 500

        if (x > 150 and x < (width) -150) and (y > 150  and y < (height)- 150 ):
            red = int(rgb_value[0] +100)
            green = int(rgb_value[1] )
            blue = int(rgb_value[2] +100)

        else:
            red = int(rgb_value[0] -100 )
            green = int(rgb_value[1] )
            blue = int(rgb_value[2]-100 )

        img.putpixel ((x,y), (red, green, blue))

img.save ('output.jpg')
print "Done making new image!"




#Focused Filter
from PIL import Image
import math
img = Image.open("path.jpg")

height = img.size[1]
width = img.size[0]

print img.size
print (height)
print (width)

for y in range(height):
    for x in range(width):
        distance = math.sqrt((height - y)**2 + (width - x)**2)
        rgb_value = img.getpixel((x, y))
        #ratio = distance / max(height, width)
        change_factor = (250-distance) / 500

        if (x > 150 and x < (width) -150) and (y > 150  and y < (height)- 150 ):
            red = int(rgb_value[0] + 15)
            green = int(rgb_value[1] +10 )
            blue = int(rgb_value[2] +25)

        else:
            red = int(rgb_value[0] +60 )
            green = int(rgb_value[1] +40 )
            blue = int(rgb_value[2]+ 60 )

        img.putpixel ((x,y), (red, green, blue))

img.save ('output.jpg')
print "Done making new image!"


#little black boarder
from PIL import Image
import math
img = Image.open("path.jpg")

height = img.size[1]
width = img.size[0]

print img.size
print (height)
print (width)

for y in range(height):
    for x in range(width):
        distance = math.sqrt((height - y)**2 + (width - x)**2)
        rgb_value = img.getpixel((x, y))

        if (x > 30 and x < (width) - 30) and (y > 30 and y < (height)- 30 ):
            red = int(rgb_value[0] + 20)
            green = int(rgb_value[1] + 10)
            blue = int(rgb_value[2] + 0)

        else:
            red = int(rgb_value[0] * 0)
            green = int(rgb_value[1] * 0)
            blue = int(rgb_value[2] * 0)

        img.putpixel ((x,y), (red, green, blue))

img.save ('output.jpg')
print "Done making new image!"


#Watermelon Party
from PIL import Image
import math
img = Image.open("path.jpg")

height = img.size[1]
width = img.size[0]

print img.size
print (height)
print (width)

for y in range(height):
    for x in range(width):
        distance = math.sqrt((height - y)**2 + (width - x)**2)
        rgb_value = img.getpixel((x, y))

        if (x > (width/10) and x < (width - width/10))and (y > (height/10) and y < (height - height/10)):
            red = int(rgb_value[0] +100)
            green = int(rgb_value[1] )
            blue = int(rgb_value[2] +100)

        else:
            red = int(rgb_value[0] -100 )
            green = int(rgb_value[1] )
            blue = int(rgb_value[2]-100 )

        img.putpixel ((x,y), (red, green, blue))

img.save ('output.jpg')
print "Done making new image!"



#Outside my window
from PIL import Image
import math
img = Image.open("path.jpg")

height = img.size[1]
width = img.size[0]
#middle = (width/2, height/2)

print img.size
print (height)
print (width)


for y in range(height):
    for x in range(width):
        distance = math.sqrt((height - y)**2 + (width - x)**2)
        rgb_value = img.getpixel((x, y))

        if (x > width/2 - width/150 and x <width/2 + width/150) or (y > height/2 - height/200 and y <height/2 + height/200):
            red = int(rgb_value[0] * 0)
            green = int(rgb_value[1] * 0 )
            blue = int(rgb_value[2] * 0)

        else:
            red = int(rgb_value[0] + 15)
            green = int(rgb_value[1] +10 )
            blue = int(rgb_value[2] +25)

        img.putpixel ((x,y), (red, green, blue))

img.save ('my_window.jpg')
print "Done making new image!"
