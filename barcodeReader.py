from pyzbar.pyzbar import decode

def getBarcodeData(imgScan):
    # width = 1920
    # height = 10801
    # resizedImg = cv2.resize(imgScan, (width//2, height//2))
    resizedImg = imgScan
    for barcode in decode(resizedImg):
        return barcode.data.decode('utf-8')
    else:
        return False