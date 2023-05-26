from string import hexdigits

import cvzone
import cv2


cap = cv2.VideoCapture(0)
success, img = cap.read()


imgFront=cv2.imread('Rear View Mirror.png',cv2.IMREAD_UNCHANGED)
imgFront=cv2.resize(imgFront,(0,0),None,0.05,0.05)



hf, wf,cf=imgFront.shape#현재 크기 받아옴 쉽게 생각하면 너비 예를들어 720x1280 3채널 같은 정보 받아옴 rear view mirror 이미지
hb,wb,cb=img.shape#현재 크기 받아옴 쉽게 생각하면 너비 예를들어 720x1280 3채널 같은 정보 받아옴



print("hf: %f , wf: %f ,cf: %f"%(hf,wf,cf))#정보 출력
print("hb: %f , wb: %f ,cb: %f"%(hb,wb,cb))

while True:
    success, img = cap.read()
    #img=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA) 해당 부분을 지워야 화면이 나옴
    imgFront=cv2.cvtColor(imgFront,cv2.COLOR_BGR2BGRA)
    imgResult = cvzone.overlayPNG(img,imgFront,[0, hb-hf])# 해당 부분은 있어야함


    cv2.imshow("Image",imgResult)
    imgResult=cv2.cvtColor(imgFront,cv2.COLOR_BGR2BGRA)
    
    if cv2.waitKey(0):
        break
    



cap.release()
cv2.destroyAllWindows()
