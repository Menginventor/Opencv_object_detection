import numpy as np
import cv2
import yaml
def nothing(x):

    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('min_Hue', 'image', 0, 180, nothing)
cv2.createTrackbar('max_Hue', 'image', 0, 180, nothing)
cv2.createTrackbar('min_Sat', 'image', 0, 255, nothing)
cv2.createTrackbar('max_Sat', 'image', 0, 255, nothing)
cv2.createTrackbar('min_Val', 'image', 0, 255, nothing)
cv2.createTrackbar('max_Val', 'image', 0, 255, nothing)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Display the resulting frame
    #cv2.imshow('gray',gray)
    #r = cv2.getTrackbarPos('R', 'image')
    #g = cv2.getTrackbarPos('G', 'image')
    #b = cv2.getTrackbarPos('B', 'image')
    cv2.imshow('image', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()
exit()
