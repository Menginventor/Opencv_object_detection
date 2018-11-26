import numpy as np
import cv2
import yaml
import yamlordereddictloader

def nothing(x):

    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow('image')
min_Hue = 0
max_Hue = 180
min_Sat = 0
max_Sat = 255
min_Val = 0
max_Val = 255
# create trackbars for color change
cv2.createTrackbar('min_Hue', 'image', 0, 180, nothing)
cv2.createTrackbar('max_Hue', 'image', 0, 180, nothing)
cv2.createTrackbar('min_Sat', 'image', 0, 255, nothing)
cv2.createTrackbar('max_Sat', 'image', 0, 255, nothing)
cv2.createTrackbar('min_Val', 'image', 0, 255, nothing)
cv2.createTrackbar('max_Val', 'image', 0, 255, nothing)
with open("HSV_range.yml") as f:
    yaml_data = yaml.load(f, Loader=yamlordereddictloader.Loader)


cv2.setTrackbarPos('min_Hue', 'image', yaml_data['min_Hue'])
cv2.setTrackbarPos('max_Hue', 'image', yaml_data['max_Hue'])
cv2.setTrackbarPos('min_Sat', 'image', yaml_data['min_Sat'])
cv2.setTrackbarPos('max_Sat', 'image', yaml_data['max_Sat'])
cv2.setTrackbarPos('min_Val', 'image', yaml_data['min_Val'])
cv2.setTrackbarPos('max_Val', 'image', yaml_data['max_Val'])
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    min_Hue = cv2.getTrackbarPos('min_Hue', 'image')
    max_Hue = cv2.getTrackbarPos('max_Hue', 'image')
    min_Sat = cv2.getTrackbarPos('min_Sat', 'image')
    max_Sat = cv2.getTrackbarPos('max_Sat', 'image')
    min_Val = cv2.getTrackbarPos('min_Val', 'image')
    max_Val = cv2.getTrackbarPos('max_Val', 'image')
    lower_bound = np.array([min_Hue,min_Sat,min_Val])
    upper_bound = np.array([max_Hue, max_Sat, max_Val])
    mask = cv2.inRange(imgHSV,lower_bound,upper_bound)
    cv2.imshow('image', mask)
    cv2.imshow('org',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
data = {}
data['min_Hue'] = min_Hue
data['max_Hue'] = max_Hue
data['min_Sat'] = min_Sat
data['max_Sat'] = max_Sat
data['min_Val'] = min_Val
data['max_Val'] = max_Val
cv2.imwrite('result.jpg',mask)
cv2.imwrite('orig.jpg',frame)
with open('HSV_range.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)
cv2.destroyAllWindows()
exit()
