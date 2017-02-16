from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if (y1 == y0):
        xaxis(x0, y0, x1, y1, screen, color)
    if (x1 == x0):
        yaxis(x0, y0, x1, y1, screen, color)
    else:
        m = slope(x0, y0, x1, y1)
        if (m > 0 and m <= 1):
            quad1(x0, y0, x1, y1, screen, color)
            quad1(x0, y0, -x1, -y1, screen, color)
        if (m > 0 and m >= 1):
            quad2(x0, y0, x1, y1, screen, color)
            quad2(x0, y0, -x1, -y1, screen, color)
        if (m < 0 and m <= 1):
            quad8(x0, y0, -x1, -y1, screen, color)
            quad8(x0, y0, x1, y1, screen, color)
        if (m < 0 and m >= 1):
            quad7(x0, y0, -x1, -y1, screen, color)
            quad7(x0, y0, x1, y1, screen, color)
        
def slope(x0, y0, x1, y1):
    A = (y1-y0)* 1.0
    B = (x1-x0)* 1.0
    return A/B

def xaxis(x0, y0, x1, y1, screen, color):
    x = x0
    while (x < x1):
        plot(screen, color, x, y0)
        x+=1
        

def yaxis(x0, y0, x1, y1, screen, color):
    y = y0
    while (y < y1):
        plot(screen, color, x0, y)
        y+=1
    

def quad1(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = y1-y0
    B = (x1-x0) * (-1)
    mid = 2 * A + B
    while (x < x1):
        plot(screen, color, x, y)
        if (mid > 0):
            y+=1
            mid+=2*B
        x+=1
        mid+=2*A

def quad2(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = y1-y0
    B = (x1-x0) * (-1)
    mid = A + 2*B
    while (y < y1):
        plot(screen, color, x, y)
        if (mid < 0):
            x+=1
            mid+=A
        y+=1
        mid+=2*B

def quad7(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = y1-y0
    B = (x1-x0) * (-1)
    mid = A - 2*B
    while (y > y1):
        plot(screen, color, x, y)
        if (mid > 0):
            x+=1
            mid+=2*A
        y-=1
        mid-=2*B

def quad8(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = y1-y0
    B = (x1-x0) * (-1)
    mid = 2 * A - B
    while (x < x1):
        plot(screen, color, x, y)
        if (mid < 0):
            y-=1
            mid-=2*B
        x+=1
        mid+=2*A
        
