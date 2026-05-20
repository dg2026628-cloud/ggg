Web VPython 3.2
import random
b = box(make_trail = True)

while True : 
    rate(100)
    k = keysdown()
    if ' ' in k :
        b.pos.x = random.uniform(-5, 5)
        b.pos.y = random.uniform(-5, 5)
        b.color = vec(random.uniform(0.9,1),random.random(),random.random())
        b.trail_color = b.
