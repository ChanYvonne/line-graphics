from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

display(screen)
draw_line(0, 0, 4, 6, screen, color)
#save_extension(screen, 'img.png')
