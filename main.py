from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(0, 0, XRES-1, YRES-1, screen, color) #oct 1 and 5
color = [ 255, 0, 0]
draw_line(0, YRES-1, XRES-1, 0, screen, color) #oct 3 and 7
color = [ 0, 0, 255]
draw_line(XRES/2, 0, XRES/2, YRES-1, screen, color) #oct 2 and 6
color = [ 255, 255, 0]
draw_line(0, YRES/2, XRES-1, YRES/2, screen, color) #oct 4 and 8


save_ppm(screen, "pic.ppm")
#save_extension(screen, 'img.png')
