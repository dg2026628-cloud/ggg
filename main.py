Web VPython 3.2
a = sphere(pos=vector(0, 0, 0), radius=0.5, color = vec(0.9,0.9,0.9))
b = sphere(pos=vector(0.5, 0.3, 0), radius=0.3, color= vec(0.9,0.9,0.9))
c = sphere(pos=vector(-0.5, 0.3, 0), radius=0.3, color= vec(0.9,0.9,0.9))
d = sphere(pos=vector(0.2, 0.1, 0.4), radius=0.05, color=color.black)
e = sphere(pos=vector(-0.2, 0.1, 0.4), radius=0.05, color=color.black)
f = sphere(pos=vector(0.0, 0.1, 0.5), radius=0.03, color=color.black)

g = pyramid(axis=vec(-0.4, 0.4, 0),pos = vec(-0.2,0.4,0),color = vec(170/225, 150/225, 150/225), size = vec(0.6,0.6,0.6))
h = pyramid(axis=vec(-0.4, 0.4, 0),pos = vec(-0.1,0.3,0.1), size = vec(0.6,0.6,0.6))
i = pyramid(axis=vec(0.4, 0.4, 0),pos = vec(0.2,0.4,0),color = vec(170/225, 150/225, 150/225), size = vec(0.6,0.6,0.6))
j = pyramid(axis=vec(0.4, 0.4, 0),pos = vec(0.1,0.3,0.1), size = vec(0.6,0.6,0.6))
k = sphere(radius= 0.7, pos = vec(0,0,0),color = vec(170/225, 150/225, 150/225))
l = sphere(radius= 0.1 , pos = vec(0,-0.1,0.7),color=color. black)
m = sphere(radius= 0.2 , pos = vec(0,-0.1,0),color=color. black)
n = sphere(radius= 0.05 , pos = vec(0.2,0.2,0.7),color=color. black)
o = sphere(radius= 0.05 , pos = vec(-0.2,0.2,0.7),color=color. black)
cat = compound([g,h,i,j,k,l,m,n,o])
cat.pos.x = 3.5

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
    if 'a' in k  and -5 <= mouse.pos.x <= -2:
        mouse.pos.x = mouse.pos.x - 0.1
    if 'd' in k and -5 <= mouse.pos.x <= -2:
        mouse.pos.x = mouse.pos.x + 0.1
    if 'w' in k and -5 <= mouse.pos.x <= -2:
        mouse.pos.y = mouse.pos.y + 0.1
    if 's' in k  and -5 <= mouse.pos.x <= -2:
        mouse.pos.y = mouse.pos.y - 0.1
    print(mouse.pos)
    if mouse.pos.x < -4.2:
        mouse.pos.x = -4.2
    if mouse.pos.x > -3.5:
        mouse.pos.x = -3.5
    if mouse.pos.y < -3:
        mouse.pos.y = -3
    if mouse.pos.y < -2.5:
        mouse.pos.y = -2.5
    if mouse.pos.y > 2.3:
        mouse.pos.y = 2.3 
        










