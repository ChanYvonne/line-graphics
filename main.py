from display import *
from draw import *
import random

screen = new_screen()

#testing
'''
color = [ 0, 255, 0 ]
draw_line(0, 0, XRES-1, YRES-1, screen, color) #slope of 1
color = [ 255, 0, 0]
draw_line(0, YRES-1, XRES-1, 0, screen, color) #slope of -1
color = [ 0, 0, 255]
draw_line(XRES/2, 0, XRES/2, YRES-1, screen, color) #0 slope
color = [ 255, 255, 0]
draw_line(0, YRES/2, XRES-1, YRES/2, screen, color) #no slope
color = [ 0, 255, 0]
draw_line(0, 50, XRES-1, 300, screen, color) #oct 1 and 5
color = [ 255, 0, 0]
draw_line(150, YRES-1, 350, 0, screen, color) #oct 3 and 7
color = [ 0, 0, 255]
draw_line(150, 0, 350, YRES-1, screen, color) #oct 2 and 6
color = [ 255, 255, 0]
draw_line(0, 400, XRES-1, 100, screen, color) #oct 4 and 8
draw_line(250,250, XRES-1,YRES-1, screen, color)
'''

#axis
color = [ 0, 0, 255]
draw_line(XRES/2, 0, XRES/2, YRES-1, screen, color)
draw_line(0, YRES/2, XRES-1, YRES/2, screen, color)

'''
color = [ 0, 255, 255]
draw_line(200, YRES/2, XRES/2, 200, screen, color)
draw_line(200, YRES/2, XRES/2, 300, screen, color)
draw_line(XRES/2, 300, 300, YRES/2, screen, color)
draw_line(XRES/2, 200, 300, YRES/2, screen, color)
'''

color = [random.randint(0,255), random.randint(0,255), random.randint(0, 255)]
x = XRES/2-50
y = YRES/2
x1 = XRES/2
y1 = YRES/2-50
while (x > 0 and y1 < YRES):
    draw_line(x, y, x1, y1, screen, color)
    x-=10
    y1-=10
    
color = [random.randint(0,255), random.randint(0,255), random.randint(0, 255)]
x = XRES/2
y = YRES/2-50
x1 = XRES/2+50
y1 = YRES/2
while (x1 < XRES and y < YRES):
    draw_line(x, y, x1, y1, screen, color)
    x1+=10
    y-=10

color = [random.randint(0,255), random.randint(0,255), random.randint(0, 255)]
x = XRES/2
y = YRES/2+50
x1 = XRES/2+50
y1 = YRES/2
while (x1 < XRES and y < YRES):
    draw_line(x, y, x1, y1, screen, color)
    x1+=10
    y+=10

color = [random.randint(0,255), random.randint(0,255), random.randint(0, 255)]
x = XRES/2-50
y = YRES/2
x1 = XRES/2
y1 = YRES/2+50
while (x > 0 and y1 < YRES):
    draw_line(x,y,x1, y1, screen, color)
    x-=10
    y1+=10


save_ppm(screen, "pic.ppm")
#save_extension(screen, 'img.png')
