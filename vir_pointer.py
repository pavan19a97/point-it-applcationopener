import numpy as np
import cv2
import imutils

# cap = cv2.VideoCapture("http://192.168.1.9:8080//video")


# while True:
def get_pointer_header(frame, header_lower_hsv_values, header_upper_hsv_values):
    lower_color = np.array(header_lower_hsv_values)
    upper_color = np.array(header_upper_hsv_values)
    green = (0, 255, 0)  # Green     - g/G
    cX, cY = "", ""

    # _, frame = cap.read()
    # frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_color, upper_color)

    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None
    if len(cnts) > 0:

        max_cnt = max(cnts, key=cv2.contourArea)
        c = max_cnt
        if cv2.contourArea(max_cnt) > 800:
            # Center of max contour
            # extLeft = tuple(c[c[:, :, 0].argmin()][0])
            # extRight = tuple(c[c[:, :, 0].argmax()][0])
            # extTop = tuple(c[c[:, :, 1].argmin()][0])
            extBot = tuple(c[c[:, :, 1].argmax()][0])
            cv2.circle(frame, extBot, 8, (255, 255, 0), -1)
            center = extBot
            # M = cv2.moments(max_cnt)
            # if M["m00"] != 0:
            #     cX = int(M["m10"] / M["m00"])
            #     cY = int(M["m01"] / M["m00"])
            #     cv2.circle(frame, (cX, cY), 4, green, 2)
            #     center = (cX, cY)


    cv2.imshow('Frame', frame)
    cv2.waitKey(1)
    return center
#     key = cv2.waitKey(1)
#     if key == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()