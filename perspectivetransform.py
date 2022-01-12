import numpy as np
from cv2 import cv2


def takeSecond(elem):
    return elem[1]


def reverse_points(src_points, a, b):
    temp_point = src_points[a]
    src_points[a] = src_points[b]
    src_points[b] = temp_point


def sort_points(src_points):
    avg_points = []
    for i in range(0, len(src_points)):
        avg_points.append((i, src_points[i][0] + src_points[i][1]))
    avg_points.sort(key=takeSecond)
    temp_points = [0, 0, 0, 0]
    for i in range(len(avg_points)):
        temp_points[i] = src_points[avg_points[i][0]]

    reverse_points(temp_points, 2, 3)
    if temp_points[1][0] > temp_points[3][0]:
        reverse_points(temp_points, 1, 3)
    src_points = temp_points
    return src_points

def get_perspective_transform(src_points, image):
    try:
        src_points = sort_points(src_points)
        print(src_points)
        src_points = np.float32([src_points[0], src_points[1], src_points[2], src_points[3]])
        dst_points = np.float32([[0, 0], [0, 1080], [1920, 1080], [1920, 0]])
        M = cv2.getPerspectiveTransform(src_points, dst_points)
        wrap_image = cv2.warpPerspective(image, M, (1920, 1080))
        cv2.imshow("wrap_image", cv2.resize(wrap_image, (1920//2, 1080//2)))

        return M, wrap_image
    except Exception as e:
        print(e)
