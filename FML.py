import random
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=500,height=500, background='white')
enemiescoords = ['poop',]
class SuperPythonBox(object):
    def __init__(self, parent):
        global drawpad
        global enemiescoords
        global x1, x2, y1, y2
        print "poop"
        self.randomcoordsr1()
        enemy1 = drawpad.create_rectangle(enemiescoords[1],enemiescoords[2],enemiescoords[3],enemiescoords[4], fill = "purple")
        enemy2 = drawpad.create_rectangle(enemiescoords[5],enemiescoords[6],enemiescoords[7],enemiescoords[8], fill = "purple")
        enemy3 = drawpad.create_rectangle(enemiescoords[9],enemiescoords[10],enemiescoords[11],enemiescoords[12], fill = "purple")
        enemy4 = drawpad.create_rectangle(enemiescoords[13],enemiescoords[14],enemiescoords[15],enemiescoords[16], fill = "purple")
        enemy5 = drawpad.create_rectangle(enemiescoords[17],enemiescoords[18],enemiescoords[19],enemiescoords[20], fill = "purple")
    def randomcoordsr1(self):
        global x1, x2, y1, y2
        global roundstart
        global rounds
        global enemies
        rounds = 5
        enemies = 5
        while enemies != 0:
            x1 = random.randint(0,500)
            enemiescoords.append(x1)
            y1 = random.randint(0,500)
            enemiescoords.append(y1)
            x2 = x1 + (random.randint(0,150))
            enemiescoords.append(x2)
            y2 = y1 + (random.randint(0, 150))
            enemiescoords.append(y2)
            enemies = enemies - 1
            if enemies == 0:
                roundstart = True
    def animate(self, event):
        print "poop"
app = SuperPythonBox(root)
root.mainloop()