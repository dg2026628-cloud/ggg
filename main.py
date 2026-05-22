Web VPython 3.2
ball = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.gray)
ball = sphere(pos=vector(0.5, 0.3, 0), radius=0.3, color=color.gray)
ball = sphere(pos=vector(-0.5, 0.3, 0), radius=0.3, color=color.gray)
ball = sphere(pos=vector(0.2, 0.1, 0.4), radius=0.05, color=color.black)
ball = sphere(pos=vector(-0.2, 0.1, 0.4), radius=0.05, color=color.black)
ball = sphere(pos=vector(0.0, 0.1, 0.5), radius=0.03, color=color.black)

box(pos=vec(0, 3, 0), size=vec(10, 0.1, -1))
box(pos=vec(0, -3, 0), size=vec(10, 0.1, -1))
box(pos=vec(-5, -0.5, 0), size=vec(0.1, 5, -1))
box(pos=vec(5, 0.5, 0), size=vec(0.1, 5, -1))
box(pos=vec(2.5, 0.7, 0), size=vec(0.1, 4.5, -1))
box(pos=vec(0, -0.7, 0), size=vec(0.1, 4.5, -1))
box(pos=vec(-2.5, 0.7, 0), size=vec(0.1, 4.5, -1))


mouse = compound([a,b,c,d,e,f])
mouse.pos.x = -3
while True :
    rate(100)
    k = keysdown()
    if 'a' in k  and -5 < mouse.pos.x < -2:
        mouse.pos.x = mouse.pos.x - 0.1
    if 'd' in k and -5 < mouse.pos.x < -2:
        mouse.pos.x = mouse.pos.x + 0.1
    if 'w' in k and -5 < mouse.pos.x < -2:
        mouse.pos.y = mouse.pos.y + 0.1
    if 's' in k  and -5 < mouse.pos.x < -2:
        mouse.pos.y = mouse.pos.y - 0.1
