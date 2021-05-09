import Images
from random import randint as rd

# This works as the game timer
def Timer(Hrs, Mins, Sec, label):
    hrs, mins, sec = Hrs.get(), Mins.get(), Sec.get()
    def InnerTimer():
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
        label.config(text = str(hrs) + ":" + minutes + ":" + seconds)
        label.after(1000, InnerTimer)
    InnerTimer()

def Img_Select_Position(Img: list):
    ImgPosition = list(range(20))
    Maxpos = len(ImgPosition) - 1
    for i in range(10):
        # First position of image 
        randonPos = rd(0, Maxpos)
        ImgPosition[randonPos] = Img[i]
        # Deleted = ImgPosition.pop(ImgPosition[randonPos])
        ImgPosition.append(ImgPosition[randonPos])
        del ImgPosition[randonPos]
        Maxpos -= 1
        # Second position of image 
        randonPos = rd(0, Maxpos)
        ImgPosition[randonPos] = Img[i]
        ImgPosition.append(ImgPosition[randonPos])
        del ImgPosition[randonPos]
        Maxpos -= 1
    print(len(ImgPosition))
    return ImgPosition

def Turn_Card(n: int, img: list, btn):
    # print(img[n])
    btn.config(image = img[n])