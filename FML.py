import random
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=1366,height=768, background='white')
enemiescoords = ['poop',]
weaponcoords = ['0',]
player = drawpad.create_oval(663, 364, 703, 404, fill = "red")

bullets = 0
gun = True
missiles = 0
sword = False
mines =  False
rounds = 5
class SuperPythonBox(object):
    def __init__(self, parent):
        global drawpad
        global enemiescoords
        global x1, x2, y1, y2
        self.randCoord()
        enemy1 = drawpad.create_rectangle(enemiescoords[1],enemiescoords[2],enemiescoords[3],enemiescoords[4], fill = "purple")
        enemy2 = drawpad.create_rectangle(enemiescoords[5],enemiescoords[6],enemiescoords[7],enemiescoords[8], fill = "purple")
        enemy3 = drawpad.create_rectangle(enemiescoords[9],enemiescoords[10],enemiescoords[11],enemiescoords[12], fill = "purple")
        enemy4 = drawpad.create_rectangle(enemiescoords[13],enemiescoords[14],enemiescoords[15],enemiescoords[16], fill = "purple")
        enemy5 = drawpad.create_rectangle(enemiescoords[17],enemiescoords[18],enemiescoords[19],enemiescoords[20], fill = "purple")
        root.bind_all('<Key>', self.key)
        root.bind_all('<Key>', self.weaponMove)
        drawpad.pack()
    def randCoord(self):
        global x1, x2, y1, y2
        global roundstart
        global rounds
        global enemies
        global enemiescoords
        global rounds
        rounds = 5
        enemies = 5
        if rounds == 5:
            while enemies != 0:
                x1 = random.randint(0,768)
                enemiescoords.append(x1)
                
                y1 = random.randint(0,768)
                enemiescoords.append(y1)
                
                x2 = x1 + (random.randint(0,150))
                enemiescoords.append(x2)
                
                y2 = y1 + (random.randint(0, 150))
                enemiescoords.append(y2)
                enemies = enemies - 1
                if enemies == 0:
                    roundstart = True
        if rounds == 4:
            while enemies != 0:
                x1 = random.randint(0,768)
                enemiescoords.append(x1)
                
                y1 = random.randint(0,768)
                enemiescoords.append(y1)
                
                x2 = x1 + (random.randint(0,150))
                enemiescoords.append(x2)
                
                y2 = y1 + (random.randint(0, 150))
                enemiescoords.append(y2)
                enemies = enemies - 1
                if enemies == 0:
                    roundstart = True
        if rounds == 3:
            while enemies != 0:
                x1 = random.randint(0,768)
                enemiescoords.append(x1)
                
                y1 = random.randint(0,768)
                enemiescoords.append(y1)
                
                x2 = x1 + (random.randint(0,150))
                enemiescoords.append(x2)
                
                y2 = y1 + (random.randint(0, 150))
                enemiescoords.append(y2)
                enemies = enemies - 1
                if enemies == 0:
                    roundstart = True
        if rounds == 2:
            while enemies != 0:
                x1 = random.randint(0,768)
                enemiescoords.append(x1)
                
                y1 = random.randint(0,768)
                enemiescoords.append(y1)
                
                x2 = x1 + (random.randint(0,150))
                enemiescoords.append(x2)
                
                y2 = y1 + (random.randint(0, 150))
                enemiescoords.append(y2)
                enemies = enemies - 1
                if enemies == 0:
                    roundstart = True
        if rounds == 1:
            while enemies != 0:
                x1 = random.randint(0,768)
                enemiescoords.append(x1)
                
                y1 = random.randint(0,768)
                enemiescoords.append(y1)
                
                x2 = x1 + (random.randint(0,150))
                enemiescoords.append(x2)
                
                y2 = y1 + (random.randint(0, 150))
                enemiescoords.append(y2)
                enemies = enemies - 1
                if enemies == 0:
                    roundstart = True
        else:
            return
    def weaponMove(self, event):
        if gun == True:
            gunModel = drawpad.create_rectangle(644, 379, 663, 389, fill = "blue")
            gx1,gy1,gx2,gy2 = drawpad.coords(gunModel)
            if gy1 < 1:
                return
            if gy1 > 1:
                drawpad.move(gunModel, 0, -10)
                
            if event.char == "a":
                if gx1 < 1:
                    return
                if gx1 > 1:
                    drawpad.move(gunModel, -10, 0)
                    
            if event.char == "s":
                if gx2 > 1365:
                    return
                if gx2 < 1365:
                    drawpad.move(gunModel, 0, 10)
                    
            if event.char == "d":
                if gy2 > 767:
                    return
                if gy2 < 767:
                    drawpad.move(gunModel, 10, 0)
                                   
    def key(self, event):
        global player
        global drawpad
        global bullets
        global gun
        global sword
        global mines
        global missiles
        x1,y1,x2,y2 = drawpad.coords(player)
        collide = self.collisionDetect()
        if event.char == "w":
            if y1 < 1:
                return
            if y1 > 1:
                drawpad.move(player, 0, -10)
                collide
        if event.char == "a":
            if x1 < 1:
                return
            if x1 > 1:
                drawpad.move(player, -10, 0)
                collide
        if event.char == "s":
            if x2 > 1365:
                return
            if x2 < 1365:
                drawpad.move(player, 0, 10)
                collide
        if event.char == "d":
            if y2 > 767:
                return
            if y2 < 767:
                drawpad.move(player, 10, 0)
                collide
    #def weaponCrap(self):
    #    global bullets
    #    global gun
    #    global sword
    #    global mines
    #    global missiles
    #    startWeapon = random.randint(0, 4)
    #    if startWeapon == 1:
    #      gun = true
             
    def collisionDetect(self):
        global player
        global enemiescoords
        x1,y1,x2,y2 = drawpad.coords(player)
        if x1 > enemiescoords[1] and x2 < enemiescoords[3]:
            if y1 > enemiescoords[2] and y2 < enemiescoords[4]:
                drawpad.delete(player)
        if x1 > enemiescoords[5] and x2 < enemiescoords[7]:
            if y1 > enemiescoords[6] and y2 < enemiescoords[8]:
                drawpad.delete(player)
        if x1 > enemiescoords[9] and x2 < enemiescoords[11]:
            if y1 > enemiescoords[10] and y2 < enemiescoords[12]:
                drawpad.delete(player)
        if x1 > enemiescoords[13] and x2 < enemiescoords[15]:
            if y1 > enemiescoords[14] and y2 < enemiescoords[16]:
                drawpad.delete(player)
        if x1 > enemiescoords[17]  and x2 < enemiescoords[19]:
             if y1 > enemiescoords[18] and y2 < enemiescoords[20]:
                drawpad.delete(player)
app = SuperPythonBox(root)
root.mainloop()