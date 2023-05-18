from string import hexdigits
from tkinter import *
from turtle import shape
import cv2


app =Tk()
width = 600
height = 400
pos_x = width/2
pos_y = height/2
canvas = Canvas(app, width=width,height=height,bg="white")
canvas.pack(padx=10,pady=10)#실제로 화면 너비가 아닌 그냥 창 padding 같은느낌

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,480)

while cv2.waitKey(33)<0:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)




def make_square():#event 없이 생성 이벤트 필요하다면 인자로 event 입력
    global shapes
    shapes = canvas.create_polygon(width/2, height/2, pos_x+50,height/2,pos_x+50,pos_y+50,width/2,pos_y+50,fill="black")


def move_up(event):
    pos_x=0
    pos_y=-10
    canvas.move(shapes,pos_x,pos_y)

def move_down(event):
    pos_x=0
    pos_y=10
    canvas.move(shapes,pos_x,pos_y)


def move_right(event):
    pos_x=10
    pos_y=0
    canvas.move(shapes,pos_x,pos_y)

def move_left(event):
    pos_x=-10
    pos_y=0
    canvas.move(shapes,pos_x,pos_y)


app.bind("<Up>",move_up)
app.bind("<Down>",move_down)
app.bind("<Right>",move_right)
app.bind("<Left>",move_left)

    


make_square()


app.mainloop()


capture.release()#메모리 해제
cv2.destroyAllWindows()#윈도우창 닫음