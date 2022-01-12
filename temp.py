
import numpy as np
import cv2

def main():
        while True:
            try:
                webcam = cv2.VideoCapture(3)
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
                

                _, imageFrame = webcam.read()
                # imageFrame = cv2.rotate(imageFrame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                cv2.imshow("imagekbarcode", imageFrame)
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    webcam.release()
                    cv2.destroyAllWindows()
                    break
            except Exception as e:
                print(e)
           

if __name__ == "__main__":
    main()