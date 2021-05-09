from tkinter import *
from Fucnts import *
import Images

root = Tk()
root.title("Memory Game")
root.geometry("650x500")
root.resizable(False, False)
root.iconbitmap("IMg.ico")
root.configure(background = "white")

ImgFrame = Frame(root, background = "blue", bd = 3, width = 450)
ImgFrame.pack(side = LEFT)
ImgFrame.pack(fill = "y")

ColumValue, RowValue = 0, 0
Pred = PhotoImage(file = "Predefined.PNG")
BtnList = []

for i in range(20):
 BtnImg = Button(ImgFrame, width = 75, height = 110, image = Pred, cursor = "hand2")
 BtnImg.grid(row = ColumValue, column = RowValue, pady = 4, padx = 3)
 BtnList.append(BtnImg)
 if ColumValue == 3:
     RowValue += 1
     ColumValue = 0
 else:
     ColumValue += 1

# Funciones por cada boton 
BtnList[0].config(command = lambda: Turn_Card(0, ListImg, BtnList[0]))
BtnList[1].config(command = lambda: Turn_Card(1, ListImg, BtnList[1]))
BtnList[2].config(command = lambda: Turn_Card(2, ListImg, BtnList[2]))
BtnList[3].config(command = lambda: Turn_Card(3, ListImg, BtnList[3]))
BtnList[4].config(command = lambda: Turn_Card(4, ListImg, BtnList[4]))
BtnList[5].config(command = lambda: Turn_Card(5, ListImg, BtnList[5]))
BtnList[6].config(command = lambda: Turn_Card(6, ListImg, BtnList[6]))
BtnList[7].config(command = lambda: Turn_Card(7, ListImg, BtnList[7]))
BtnList[8].config(command = lambda: Turn_Card(8, ListImg, BtnList[8]))
BtnList[9].config(command = lambda: Turn_Card(9, ListImg, BtnList[9]))
BtnList[10].config(command = lambda: Turn_Card(10, ListImg, BtnList[10]))
BtnList[11].config(command = lambda: Turn_Card(11, ListImg, BtnList[11]))
BtnList[12].config(command = lambda: Turn_Card(12, ListImg, BtnList[12]))
BtnList[13].config(command = lambda: Turn_Card(13, ListImg, BtnList[13]))
BtnList[14].config(command = lambda: Turn_Card(14, ListImg, BtnList[14]))
BtnList[15].config(command = lambda: Turn_Card(15, ListImg, BtnList[15]))
BtnList[16].config(command = lambda: Turn_Card(16, ListImg, BtnList[16]))
BtnList[17].config(command = lambda: Turn_Card(17, ListImg, BtnList[17]))
BtnList[18].config(command = lambda: Turn_Card(18, ListImg, BtnList[18]))
BtnList[19].config(command = lambda: Turn_Card(19, ListImg, BtnList[19]))

Sec = IntVar(value = 0)
Mins = IntVar(value = 0)
Hours = IntVar(value = 0)
LabelTimer = Label(root, font = ("Arial", 25), background = "white")
LabelTimer.pack(side = RIGHT, anchor = "center", padx = (0, 20))

Imgs = []
# Neccesary images for the program working
for i in range(10):
    img = PhotoImage(file = Images.ImgList[i])
    Imgs.append(img)

Timer(Hours, Mins, Sec, LabelTimer)
ListImg = Img_Select_Position(Imgs)

for i in range(len(ListImg)):
    print(ListImg[i])

root.mainloop()