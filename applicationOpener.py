import time
class applicationOpener:

    def open_application(self, point, barcode_data, application_names, roi, command):
        # pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
        application_name=application_names

        region_of_text = roi
        # path = 'resources/rema.jpg'
        # imgShow = cv2.imread(path)
        # img = cv2.resize(imgShow, (1920, 1080))
        # imgMask = np.zeros_like(imgShow)
        # TODO: in opencv2 if point in rectangle opp points .....
        i=0
        for proi in region_of_text:
            if point[0]>proi[0][0] and point[0]<proi[1][0] and point[1]>proi[0][1] and point[1]<proi[1][1]:
                print(point)
                # print("google")
                # imgShow = cv2.addWeighted(imgShow, 0.99, imgMask, 0.1, 0)/
                # imgCrop = img[proi[0][1]:proi[1][1], proi[0][0]:proi[1][0]]
                # myData = (pytesseract.image_to_string(imgCrop))
                # print(myData)
                # return myData
                print(proi)
                print(application_name[i][0])
                # open using command
                if application_name[i][1] or application_name[i][1] == "empty" or application_name[i][1]=="exit":
                    command = command
                    command[f'{application_name[i][1]}'](application_name[i][2])
                if application_name[i][1] == "exit":
                    break
                time.sleep(10)

            else:
                print("not go")
            i += 1