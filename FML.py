import random
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=1366,height=768, background='white')
enemiescoords = ['poop',]
weaponcoords = ['0',]
player = drawpad.create_oval(663, 364, 703, 404, fill = "red")
gunModel = drawpad.create_rectangle(644, 379, 663, 389, fill = "blue")
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
        self.enemy1 = drawpad.create_rectangle(enemiescoords[1],enemiescoords[2],enemiescoords[3],enemiescoords[4], fill = "purple")
        self.enemy2 = drawpad.create_rectangle(enemiescoords[5],enemiescoords[6],enemiescoords[7],enemiescoords[8], fill = "purple")
        self.enemy3 = drawpad.create_rectangle(enemiescoords[9],enemiescoords[10],enemiescoords[11],enemiescoords[12], fill = "purple")
        self.enemy4 = drawpad.create_rectangle(enemiescoords[13],enemiescoords[14],enemiescoords[15],enemiescoords[16], fill = "purple")
        self.enemy5 = drawpad.create_rectangle(enemiescoords[17],enemiescoords[18],enemiescoords[19],enemiescoords[20], fill = "purple")
        root.bind_all('<Key>', self.key)
        drawpad.pack()
        self.animate()
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
                
                x2 = x1 + (random.randint(75,150))
                enemiescoords.append(x2)
                
                y2 = y1 + (random.randint(75, 150))
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
            
                                   
    def animate(self):
        global enemiescoords
        global player
        e1x1, e1y1, e1x2, e1y2 = drawpad.coords(self.enemy1)
        e2x1, e2y1, e2x2, e2y2 = drawpad.coords(self.enemy2)
        e3x1, e3y1, e3x2, e3y2 = drawpad.coords(self.enemy3)
        e4x1, e4y1, e4x2, e4y2 = drawpad.coords(self.enemy4)
        e5x1, e5y1, e5x2, e5y2 = drawpad.coords(self.enemy5)
        direction = -10
        if e1y2 == 0:
            direction = 10
        if e1y1 == 767:
            direction = -10
        drawpad.move(self.enemy1, 0, -10)
        drawpad.after(10, self.animate)        
        #if event.char == "a":
        #        if gx1 < 1:
        #            return
        #        if gx1 > 1:
        #            drawpad.move(gunModel, -10, 0)
        #            
        #if event.char == "s":
        #        if gx2 > 1365:
        #            return
        #        if gx2 < 1365:
        #            drawpad.move(gunModel, 0, 10)
        #            
        #if event.char == "d":
        #        if gy2 > 767:
        #            return
        #        if gy2 < 767:
        #            drawpad.move(gunModel, 10, 0)
    def key(self, event):
        global player
        global drawpad
        global bullets
        global gun
        global sword
        global mines
        global missiles
        global weaponMove
        global gunModel
        x1,y1,x2,y2 = drawpad.coords(player)
        collide = self.collisionDetect()
        if event.char == "w":
            if gun == True:
                drawpad.move(gunModel, 0, -10)
            if y1 < 1:
                return
            if y1 > 1:
                drawpad.move(player, 0, -10)
                collide
        if event.char == "a":
            if gun == True:
                drawpad.move(gunModel, -10, 0)
            if x1 < 1:
                return
            if x1 > 1:
                drawpad.move(player, -10, 0)
                collide
        if event.char == "s":
            if gun == True:
                drawpad.move(gunModel, 0, 10)
            if x2 > 1365:
                return
            if x2 < 1365:
                drawpad.move(player, 0, 10)
                collide
        if event.char == "d":
            if gun == True:
                drawpad.move(gunModel, 10, 0)
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