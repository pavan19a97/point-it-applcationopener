from cv2 import cv2
import numpy as np
from main import config


def get_center_points_of_four_rectangles(imageFrame):
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    # 26 51 186 255 163 255
    blue_lower = np.array(config().lower_hsv, np.uint8)
    blue_upper = np.array(config().upper_hsv, np.uint8)
    #
    # hsvFrame = cv2.cvtColor(imageFrame.copy(), cv2.COLOR_BGR2HSV)
    #
    # mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
    #
    # mask = cv2.erode(mask, None, iterations=2)
    # mask = cv2.dilate(mask, None, iterations=2)

    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    kernal = np.ones((5, 5), "uint8")

    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame,
                               mask=blue_mask)

    contours, hierarchy = cv2.findContours(blue_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    center_points = []
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 500):
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                x = cX
                y = cY

                # cv2.circle(frame, (cX, cY), 4, green, 2)
                center_points.append([cX, cY])
                imageFrame = cv2.rectangle(imageFrame, (x, y), (x, y), (255, 0, 0), 2)
                cv2.putText(imageFrame, f"{x, y}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))
            # x, y, w, h = cv2.boundingRect(contour)
            # imageFrame = cv2.rectangle(imageFrame, (x, y),
            #                            (x + w, y + h),
            #                            (255, 0, 0), 2)
            # cv2.putText(imageFrame, f"{x,y}", (x, y),
            #             cv2.FONT_HERSHEY_SIMPLEX,
            #             1.0, (255, 0, 0))
            # center_points.append([x+w//2, y+h//2])

    # Program Termination
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    print(center_points)
    return center_points, imageFrame