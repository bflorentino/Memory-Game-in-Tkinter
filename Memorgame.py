from tkinter import *
from Fucnts import *
from PIL import ImageTk, Image
import Images

def Initialize_Game():
 global Sec, Mins, Hours
 global ListImg
 Sec.set(value = 0)
 Mins.set(value = 0)
 Hours.set(value = 0)
 Change_To_Default_Image(BtnList, Pred)
 Init_Values(LabelTimer)
 ListImg = Img_Select_Position(Imgs)

root = Tk()
root.title("Memory Game")
root.geometry("650x500")
root.resizable(False, False)
root.iconbitmap("IMg.ico")
root.configure(background = "white")

# This frame will be the container for all the buttons 
ImgFrame = Frame(root, background = "blue", bd = 3, width = 450)
ImgFrame.pack(side = LEFT)
ImgFrame.pack(fill = "y")

# This image is gonna be the predefined one for every button 
Pred = Image.open("Predefined.PNG")
Pred = ImageTk.PhotoImage(Pred)

ColumValue, RowValue = 0, 0
BtnList = []

# Buttons Creation
for i in range(20):
 BtnImg = Button(ImgFrame, width = 110, height = 85, cursor = "hand2")
 BtnImg.grid(row = RowValue, column = ColumValue, pady = 4, padx = 3)
 BtnList.append(BtnImg)
 if ColumValue == 3:
     RowValue += 1
     ColumValue = 0
 else:
     ColumValue += 1

# Rigth Zone of the window
RightZone = Frame(root, background = "white")
RightZone.pack(side = RIGHT, anchor = "center")
BtnReinicio = Button(RightZone, text = "Reiniciar", background = "white", pady = 3, padx = 5, command = lambda: Initialize_Game())
BtnReinicio.pack()

# Timer 
Sec = IntVar(value = 0)
Mins = IntVar(value = 0)
Hours = IntVar(value = 0)
LabelTimer = Label(RightZone, font = ("Arial", 25), background = "white")
LabelTimer.pack(padx = (0, 20))

# Function for every button
BtnList[0].config(command = lambda: Turn_Card(0, ListImg, BtnList[0], Pred, LabelTimer))
BtnList[1].config(command = lambda: Turn_Card(1, ListImg, BtnList[1], Pred, LabelTimer))
BtnList[2].config(command = lambda: Turn_Card(2, ListImg, BtnList[2], Pred, LabelTimer))
BtnList[3].config(command = lambda: Turn_Card(3, ListImg, BtnList[3], Pred, LabelTimer))
BtnList[4].config(command = lambda: Turn_Card(4, ListImg, BtnList[4], Pred, LabelTimer))
BtnList[5].config(command = lambda: Turn_Card(5, ListImg, BtnList[5], Pred, LabelTimer))
BtnList[6].config(command = lambda: Turn_Card(6, ListImg, BtnList[6], Pred, LabelTimer))
BtnList[7].config(command = lambda: Turn_Card(7, ListImg, BtnList[7], Pred, LabelTimer))
BtnList[8].config(command = lambda: Turn_Card(8, ListImg, BtnList[8], Pred, LabelTimer))
BtnList[9].config(command = lambda: Turn_Card(9, ListImg, BtnList[9], Pred, LabelTimer))
BtnList[10].config(command = lambda: Turn_Card(10, ListImg, BtnList[10], Pred, LabelTimer))
BtnList[11].config(command = lambda: Turn_Card(11, ListImg, BtnList[11], Pred, LabelTimer))
BtnList[12].config(command = lambda: Turn_Card(12, ListImg, BtnList[12], Pred, LabelTimer))
BtnList[13].config(command = lambda: Turn_Card(13, ListImg, BtnList[13], Pred, LabelTimer))
BtnList[14].config(command = lambda: Turn_Card(14, ListImg, BtnList[14], Pred, LabelTimer))
BtnList[15].config(command = lambda: Turn_Card(15, ListImg, BtnList[15], Pred, LabelTimer))
BtnList[16].config(command = lambda: Turn_Card(16, ListImg, BtnList[16], Pred, LabelTimer))
BtnList[17].config(command = lambda: Turn_Card(17, ListImg, BtnList[17], Pred, LabelTimer))
BtnList[18].config(command = lambda: Turn_Card(18, ListImg, BtnList[18], Pred, LabelTimer))
BtnList[19].config(command = lambda: Turn_Card(19, ListImg, BtnList[19], Pred, LabelTimer))

# We get the images from the module "Images"
Imgs = []
for i in range(10):
    img = Image.open(Images.ImgList[i])
    img = img.resize((110, 85))
    img = ImageTk.PhotoImage(img)
    Imgs.append(img)

# Functions call to start the application
Initialize_Game()
Timer(Hours, Mins, Sec, LabelTimer)

root.mainloop()