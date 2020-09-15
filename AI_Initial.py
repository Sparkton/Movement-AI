import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import math, random

N = 25
M = 4

class sdost(object):
    def __init__(self):
        self.x = 10 * np.random.random_sample()
        self.y = 10 * np.random.random_sample()
        self.velx = self.generate_new_vel()
        self.vely = self.generate_new_vel()
        self.priority = 0
    
    

    


class dot(object):
    def __init__(self):
        self.x = 10 * np.random.random_sample()
        self.y = 10 * np.random.random_sample()
        self.velx = self.generate_new_vel()
        self.vely = self.generate_new_vel()
        self.priority = 1#int(input())#self.generate_priority_value()

    def generate_new_vel(self):
        return (np.random.random_sample() - 0.5) 

    def generate_priority_value(self):
        return random.randint(0, 1)
    
    def set_priority(self):
        self.priority = 1

    def move(self):
        def distance(x1, y1, x2, y2):
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        def inside(x1, y1):
            if distance(x1, y1, 5, 5) <= 1:
                return True
            else:
                return False

        def calc_dist(d):
            ret = 0
            for x in dots:
                if inside(x.x, x.y) and x != d:           
                    ret = ret + distance(x.x, x.y, d.x, d.y)
                if (distance(x.x,x.y,d.x,d.y) < 0.5):
                #if (abs(x.x - d.x) < 2 and abs(x.y-d.y) < 2): 
                    x.set_priority()
            return ret

        # if dot is inside the circle it tries to maximize the distances to
        # other dots inside circle
        if self.priority == 0:
            return
        dist = calc_dist(self)
        if inside(self.x, self.y):
            for i in range(1, 10):
                self.velx = self.generate_new_vel()
                self.vely = self.generate_new_vel()
                self.x = self.x + self.velx
                self.y = self.y + self.vely
                if calc_dist(self) <= dist or not inside(self.x, self.y):
                    self.x = self.x - self.velx
                    self.y = self.y - self.vely
        else:
            if np.random.random_sample() < 0.95:
                self.x = self.x + self.velx
                self.y = self.y + self.vely
            else:
                self.velx = self.generate_new_vel()
                self.vely = self.generate_new_vel()
                self.x = self.x + self.velx
                self.y = self.y + self.vely
            if self.x >= 10:
                self.x = 10
                self.velx = -1 * self.velx
            if self.x <= 0:
                self.x = 0
                self.velx = -1 * self.velx
            if self.y >= 10:
                self.y = 10
                self.vely = -1 * self.vely
            if self.y <= 0:
                self.y = 0
                self.vely = -1 * self.vely

dots = [dot() for i in range(N)]
fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
#for dot in dots:
d, = ax.plot([dot.x for dot in dots],[dot.y for dot in dots] , 'ro')
circle = plt.Circle((5, 5), 1, color='b', fill=False)
ax.add_artist(circle)


# animation function.  This is called sequentially
def animate(i):
    for dot in dots:
        dot.move()
    d.set_data([dot.x for dot in dots],
               [dot.y for dot in dots])
    return d,



anim = animation.FuncAnimation(fig, animate, frames=100, interval=100)
plt.show()
