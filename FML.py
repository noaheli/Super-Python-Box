import random
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=1366,height=768, background='white')
enemiescoords = ['poop',]
weaponcoords = ['0',]
player = drawpad.create_oval(663, 364, 703, 404, fill = "red")
bullets = 0
gun = False
missiles = 2
sword = False
mines =  False
class SuperPythonBox(object):
    def __init__(self, parent):
        global drawpad
        global enemiescoords
        global x1, x2, y1, y2
        self.randomcoordsr1()
        enemy1 = drawpad.create_rectangle(enemiescoords[1],enemiescoords[2],enemiescoords[3],enemiescoords[4], fill = "purple")
        enemy2 = drawpad.create_rectangle(enemiescoords[5],enemiescoords[6],enemiescoords[7],enemiescoords[8], fill = "purple")
        enemy3 = drawpad.create_rectangle(enemiescoords[9],enemiescoords[10],enemiescoords[11],enemiescoords[12], fill = "purple")
        enemy4 = drawpad.create_rectangle(enemiescoords[13],enemiescoords[14],enemiescoords[15],enemiescoords[16], fill = "purple")
        enemy5 = drawpad.create_rectangle(enemiescoords[17],enemiescoords[18],enemiescoords[19],enemiescoords[20], fill = "purple")
        root.bind_all('<Key>', self.key)
        drawpad.pack()
    def randomcoordsr1(self):
        global x1, x2, y1, y2
        global roundstart
        global rounds
        global enemies
        global enemiescoords
        rounds = 5
        enemies = 5
        while enemies != 0:
            x1 = random.randint(0,768)
            enemiescoords.append(x1)
            weaponcoords.append(x1)
            y1 = random.randint(0,768)
            enemiescoords.append(y1)
            weaponcoords.append(y1)
            x2 = x1 + (random.randint(0,150))
            enemiescoords.append(x2)
            weaponcoords.append(x2)
            y2 = y1 + (random.randint(0, 150))
            enemiescoords.append(y2)
            enemies = enemies - 1
            if enemies == 0:
                roundstart = True
    def animate(self, event):
        global player
        global drawpad
        global enemy1
        global enemy2
        global enemy3
        global enemy4
        global enemy5
        x1,y1,x2,y2 = drawpad.coords(player)
        e1x1,e1y1,e1x2,e1y2 = drawpad.coords(enemy1)
        e2x1,e2y1,e2x2,e2y2 = drawpad.coords(enemy2)
        e3x1,e3y1,e3x2,e3y2 = drawpad.coords(enemy3)
        e4x1,e4y1,e4x2,e4y2 = drawpad.coords(enemy4)
        e5x1,e5y1,e5x2,e5y2 = drawpad.coords(enemy5)
        if event.char == "w":
            drawpad.move(player, 0,-10)
            
        if event.char == "a":
            drawpad.move
app = SuperPythonBox(root)
root.mainloop()