from string import hexdigits

import cvzone
import cv2


capture = cv2.VideoCapture(0)
ret, frame = capture.read()

blue=(255,0,0)

mirror_img=cv2.imread('Rear View Mirror.png',cv2.IMREAD_UNCHANGED)
#mirror_img=cv2.resize(mirror_img,dsize=(100,70),interpolation=cv2.INTER_LINEAR)
mirror_img=cv2.resize(mirror_img,(0,0),None,0.3,0.3)

hf, wf,cf=mirror_img.shape
hb,wb,cv=frame.shape

while True:
    ret, frame = capture.read()
    img_result = cvzone.overlayPNG(frame,mirror_img,[0,hb-hf])

    cv2.imshow("Image",img_result)
    cv2.waitKey(1)


    #cv2.imshow("VideoFrame", frame)
    #img =cv2.rectangle(frame,(10,10),(100,100),blue,3)
    
    
    #print(img.shape)
    
    #cv2.imshow("videoFrame", resized_img)
    #c=cv2.waitKey(1)
    #if c==27:
    #    break

capture.release()
cv2.destroyAllWindows()

print('hello')