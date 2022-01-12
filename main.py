import numpy as np
import cv2
import imp
from processPaperandHeader import processPaperandHeader
import detectPaper
from pyzbar.pyzbar import decode
from math import floor

import time


class config:

    def __init__(self):
        self.var = self.get_barcodedata()
        details = __import__(f'{self.var}')
        self.roi = details.roi
        self.lower_hsv = details.paper_lower_hsv
        self.upper_hsv = details.paper_upper_hsv
        self.application_names = details.application_names
        self.command = details.command

        self.outputresolution = [[0, 0], [0, 1080], [1920, 1080], [1920, 0]]

        self.header_lower_hsv_values = details.header_lower_hsv_values
        self.header_upper_hsv_values = details.header_upper_hsv_values

    def get_barcodedata(self):
        while True:
            try:
                webcam = cv2.VideoCapture("http://192.168.1.9:8080//video")
                _, imgScan = webcam.read()
                resizedImg = imgScan
                for barcode in decode(resizedImg):
                    return barcode.data.decode('utf-8')
                print("barcode not detected")
                cv2.imshow("imagekbarcode", imgScan)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    webcam.release()
                    cv2.destroyAllWindows()
            except Exception as error:
                print(error)

    def main(self):
        while True:
            webcam = cv2.VideoCapture("http://192.168.1.9:8080//video")
            # while (1):
            #     _, imageFrame = webcam.read()
            #     try:
            #         getIndexFingerPoints(imageFrame)
            #     except Exception as e:
            #         print(e)
            #     if cv2.waitKey(10) & 0xFF == ord('q'):
            #         webcam.release()
            #         cv2.destroyAllWindows()
            #         break
            i=200
            while (i):

                _, imageFrame = webcam.read()
                # imageFrame = cv2.rotate(imageFrame, cv2.ROTATE_90_COUNTERCLOCKWISE)

                center_points, imageFrame = detectPaper.get_center_points_of_four_rectangles(imageFrame)
                if len(center_points) == 4:
                    processPaperandHeader().func_getPerspectiveTransform(center_points, imageFrame, self.header_lower_hsv_values, self.header_upper_hsv_values, self.application_names, self.roi, self.command)

                if cv2.waitKey(100) & 0xFF == ord('q'):
                    webcam.release()
                    cv2.destroyAllWindows()
                    break
                i -= 1
            webcam.release()
            cv2.destroyAllWindows()
            time.sleep(10)

if __name__ == "__main__":
    config().main()