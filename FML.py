import random
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=1366,height=768, background='white')
enemiescoords = ['poop',]
weaponcoords = ['0',]
bulletModel = drawpad.create_oval(1343, 376, 1323, 394, fill = "white")
player = drawpad.create_oval(1323, 364, 1363, 404, fill = "red")
gunModel = drawpad.create_rectangle(1325, 379, 1294, 389, fill = "white",  outline = "white")
bullets = 0
gun = True
shot = False
missiles = 0
rounds = 5
direction1 = -5
direction2 = -5
direction3 = -5
direction4 = -5
direction5 = -5
drawpad.config(bulletModel,fill = "blue")

class SuperPythonBox(object):
    def __init__(self, parent):
        global drawpad
        global enemiescoords
        global x1, x2, y1, y2
        global bullets
        global gun
        global gunModel
        self.randCoord()
        self.enemy1 = drawpad.create_rectangle(enemiescoords[1],enemiescoords[2],enemiescoords[3],enemiescoords[4], fill = "purple")
        self.enemy2 = drawpad.create_rectangle(enemiescoords[5],enemiescoords[6],enemiescoords[7],enemiescoords[8], fill = "purple")
        self.enemy3 = drawpad.create_rectangle(enemiescoords[9],enemiescoords[10],enemiescoords[11],enemiescoords[12], fill = "purple")
        self.enemy4 = drawpad.create_rectangle(enemiescoords[13],enemiescoords[14],enemiescoords[15],enemiescoords[16], fill = "purple")
        self.enemy5 = drawpad.create_rectangle(enemiescoords[17],enemiescoords[18],enemiescoords[19],enemiescoords[20], fill = "purple")
        root.bind_all('<Key>', self.key)
        drawpad.pack()

        self.animate()
        self.weaponCrap()
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
        global direction1
        global direction2
        global direction3
        global direction4
        global direction5
        global shot
        global bulletModel
        e1x1, e1y1, e1x2, e1y2 = drawpad.coords(self.enemy1)
        e2x1, e2y1, e2x2, e2y2 = drawpad.coords(self.enemy2)
        e3x1, e3y1, e3x2, e3y2 = drawpad.coords(self.enemy3)
        e4x1, e4y1, e4x2, e4y2 = drawpad.coords(self.enemy4)
        e5x1, e5y1, e5x2, e5y2 = drawpad.coords(self.enemy5)
        if e1y1 < 0:
            direction1 = 5
        if e1y2 > 767:
            direction1 = -5
        if e2y1 < 0:
            direction2 = 5
        if e2y2 > 767:
            direction2 = -5
        if e3y1 < 0:
            direction3 = 5
        if e3y2 > 767:
            direction3 = -5
        if e4y1 < 0:
            direction4 = 5
        if e4y2 > 767:
            direction4 = -5
        if e5y1 < 0:
            direction5 = 5
        if e5y2 > 767:
            direction5 = -5
        if shot == True:
            drawpad.move(bulletModel, -5, 0)
        drawpad.move(self.enemy1, 0, direction1)
        drawpad.move(self.enemy2, 0, direction2)
        drawpad.move(self.enemy3, 0, direction3)
        drawpad.move(self.enemy4, 0, direction4)
        drawpad.move(self.enemy5, 0, direction5)
        drawpad.after(10, self.animate)        

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
        global shot
        x1,y1,x2,y2 = drawpad.coords(player)
        collide = self.collisionDetect()
        if event.char == "w":

            if y1 < 1:
                return
            if y1 > 1:
                drawpad.move(gunModel, 0, -10)
                drawpad.move(player, 0, -10)
                drawpad.move(bulletModel, 0, -10)
                collide
        if event.char == "a":
            if x1 < 1:
                return
            if x1 > 1:
                drawpad.move(player, -10, 0)
                drawpad.move(gunModel, -10, 0)
                drawpad.move(bulletModel, -10, 0)
                collide
        if event.char == "s":

            if x2 > 1365:
                return
            if x2 < 1365:
                drawpad.move(player, 0, 10)
                drawpad.move(gunModel, 0, 10)
                drawpad.move(bulletModel, 0, 10)
                collide
        if event.char == "d":

            if y2 > 767:
                return
            if y2 < 767:
                drawpad.move(player, 10, 0)
                drawpad.move(gunModel, 10, 0)
                drawpad.move(bulletModel, 10, 0)
                collide
        if event.char == " ":
            if gun == True:
                if bullets != 0:
                    shot = True
    def weaponCrap(self):
        global bullets
        global gun
        global sword
        global mines
        global missiles
        global gunModel
        global bullets
        global drawpad
        startWeapon = 1
        if startWeapon == 1:       
            bullets = 6
             
    def collisionDetect(self):
        global player
        e1x1, e1y1, e1x2, e1y2 = drawpad.coords(self.enemy1)
        e2x1, e2y1, e2x2, e2y2 = drawpad.coords(self.enemy2)
        e3x1, e3y1, e3x2, e3y2 = drawpad.coords(self.enemy3)
        e4x1, e4y1, e4x2, e4y2 = drawpad.coords(self.enemy4)
        e5x1, e5y1, e5x2, e5y2 = drawpad.coords(self.enemy5)
        x1,y1,x2,y2 = drawpad.coords(player)
        if x1 > e1x1 and x2 < e1x2:
            if y1 > e1y1 and y2 < e1y2:
                drawpad.delete(player)
        if x1 > e2x1 and x2 < e2x2:
            if y1 > e2y1 and y2 < e2y2:
                drawpad.delete(player)
        if x1 > e3x1 and x2 < e3x2:
            if y1 > e3y1 and y2 < e3y2:
                drawpad.delete(player)
        if x1 > e4x1 and x2 < e4x2:
            if y1 > e4y1 and y2 < e4y2:
                drawpad.delete(player)
        if x1 > e5x1  and x2 < e5x2:
             if y1 > e5y1 and y2 < e5y2:
                drawpad.delete(player)
app = SuperPythonBox(root)
root.mainloop()