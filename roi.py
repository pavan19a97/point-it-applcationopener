import cv2
import random
import main
from main import config
from perspectivetransform import get_perspective_transform

path = 'resources/rema.jpg'
scale = 0.1
circles = []
counter = 0
counter2 = 0
point1=[]
point2=[]
myPoints = []
myColor=[]
def mousePoints(event,x,y,flags,params):
    global counter,point1,point2,counter2,circles,myColor
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter==0:
            point1=int(x),int(y)
            counter +=1
            myColor = (random.randint(0,2)*200,random.randint(0,2)*200,random.randint(0,2)*200 )
        elif counter ==1:
            point2=int(x),int(y)
            # type = input('Enter Type')
            # name = input ('Enter Name ')
            myPoints.append([point1,point2])
            counter=0
        circles.append([x,y,myColor])
        counter2 += 1

# img = cv2.imread(path)
cam  = cv2.VideoCapture(config.camera)
while True:
    suc, img = cam.read()
    center_points, imgframe = main.get_center_points_of_four_rectangles(img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        cam.release()
        break
cv2.imshow("img",imgframe)
if len(center_points) == 4:
    M, warp_image = get_perspective_transform(center_points, imgframe)

img = warp_image
img = cv2.resize(img, (1980, 1080))

print(img.shape)

while True:
    # To Display points
    for x,y,color in circles:
        cv2.circle(img,(x,y),3,color,cv2.FILLED)
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print(myPoints)
        break