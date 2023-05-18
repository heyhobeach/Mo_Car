from string import hexdigits

import cv2



capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,480)

while cv2.waitKey(33)<0:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)



if not capture.isOpened():
    print("not open webcam")
    exit()


while capture.isOpend():
    ret, frame = capture.read()

    if ret:
        cv2.imshow("VideoFrame",frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break





capture.release()
cv2.destroyAllWindows()
