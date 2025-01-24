import pgzrun,random
WIDTH=500
HEIGHT=500

def draw():
    h=470
    w=90
    r=255
    g=200
    b=225
    screen.fill((20,5,5))
    for i in range(20):
     thing=Rect(0,0,h,w)
     thing.center=(250,250)
     screen.draw.rect(thing,(r,g,b))
     h-=15
     w+=15
     r-=10
     g-=10
     b-=10



def update():
    pass
pgzrun.go()