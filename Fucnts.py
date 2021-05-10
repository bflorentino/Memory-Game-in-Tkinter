from random import randint as rd
from time import sleep
import threading
import playsound
from tkinter import messagebox

FirstImageTurned = False
ListImagesSelected = []
Mistakes = 0
FoundPairs = 0
RunTime = True

def Init_Values(lbltimer):
    global ListImagesSelected, Mistakes, FoundPairs, FirstImageTurned, RunTime
    Mistakes = 0
    FoundPairs = 0
    FirstImageTurned = False
    RunTime = False
    ListImagesSelected = []
    lbltimer.pack(padx = (0, 20))

# This works as the game timer
def Timer(Hrs, Mins, Sec, label):
    hrs, mins, sec = Hrs.get(), Mins.get(), Sec.get()
    def InnerTimer():
      global RunTime
      minutes = "00"
      seconds = "00"
      if RunTime:
        nonlocal hrs, mins, sec
        sec += 1
        if sec == 60:
            mins += 1
            sec = 0
            if mins == 60:
                hrs += 1
                mins = 0
        if sec < 10:
            seconds = "0" + str(sec)
        else:
            seconds = str(sec)
        if mins < 10:
            minutes = "0" + str(mins)
        else:
            minutes = str(mins)
      else:
        hrs, mins, sec = 0, 0, 0
        RunTime = True
      label.config(text = str(hrs) + ":" + minutes + ":" + seconds)
      label.after(1000, InnerTimer)
    InnerTimer()

# This function puts twice every image received within another list in ramdon positions.
# The returned list from this function is the one that will be used in the game to collocate all images
# in buttons 
def Img_Select_Position(Img: list):
    ImgPosition = list(range(20))
    ImgColocation =  list(range(20))
    Maxpos = len(ImgPosition) - 1
    for i in range(10):
        # First position of image 
        randonPos = rd(0, Maxpos)
        Position = ImgPosition[randonPos]
        ImgColocation[Position] = Img[i]
        del ImgPosition[randonPos]
        Maxpos -= 1
        # Second position of image 
        randonPos = rd(0, Maxpos)
        Position = ImgPosition[randonPos]
        ImgColocation[Position] = Img[i]
        del ImgPosition[randonPos]
        Maxpos -= 1
    return ImgColocation

# This function is an intermediary function
def Turn_Card(n: int, img: list, btn, pred, LabelTimer):
    threading.Thread(target=lambda: Turned_Card(n, img, btn, pred, LabelTimer)).start()

# It turns every pressed button, so that the image associated with it can be seen 
def Turned_Card(n: int, img: list, btn, pred, LabelTimer):
    if len(ListImagesSelected) <= 2:
     btn.config(image = img[n])
     CheckStatus(n, img, btn, pred, LabelTimer)
    playsound.playsound("blackjack_1.mp3") #Sound when any button is pressed

# This function will check if there is only 1 button turned
def CheckStatus(n: int, img: list, btn, pred, LabelTimer):
    global FirstImageTurned, ListImagesSelected
    if FirstImageTurned == False:
        FirstImageTurned = True
        ListImagesSelected.extend([img[n], btn])
    else:
        ListImagesSelected.extend([img[n], btn])
        Verify_Images_Selected(ListImagesSelected, pred, LabelTimer)
        FirstImageTurned = False

# This function verifies that 2 pressed buttons have the same image  
def Verify_Images_Selected(List, pred, LabelTimer):
    if List[0] == List[2] and List[1] != List[3]:
        Disable_Buttons(List[1], List[3], LabelTimer)
    else:
        sleep(0.5)
        ListChangeImgpred = [List[1], List[3]]
        Change_To_Default_Image(ListChangeImgpred, pred)

# If both buttons have the same image the buttons will be disabled, so that we can't press them over
def Disable_Buttons(btn1, btn2, LabelTimer):
    global ListImagesSelected
    playsound.playsound("cartoon130.mp3") # Sound when a pair of images are found
    btn1.config(state = "disabled")
    btn2.config(state = "disabled")
    ListImagesSelected = []
    Correct(LabelTimer)

# If the pressed buttons images are diff the buttons image will be the predefined one
# This function works for all images too 
def Change_To_Default_Image(ListChangeImgpred, pred):
    global ListImagesSelected
    for i in range(len(ListChangeImgpred)):
        ListChangeImgpred[i].config(image = pred, state = "active")
    # We have to make sure the list received has only the pressed buttons at the moment
    if len(ListChangeImgpred) == 2:
     ListImagesSelected = []
     Mistakes_(ListChangeImgpred[0], ListChangeImgpred[1])

# When images are the same increases the value of found pairs (10 pairs in total)
def Correct(LabelTimer):
    global FoundPairs
    FoundPairs += 1
    if FoundPairs == 10:
        Finished_Game(LabelTimer)

# When images are diff increases the value of mistakes.
def Mistakes_(btn1, btn2):
    if btn1 != btn2:
        global Mistakes
        Mistakes += 1

def Finished_Game(LabelTimer):
     LabelTimer.pack_forget()
     messagebox.showinfo("Good", "You have finished the game.\n \nTotal time: " + LabelTimer.cget("text") + "\n \nErrors: " + str(Mistakes))