import numpy as np
from cv2 import cv2
import vir_pointer
from applicationOpener import applicationOpener
from barcodeReader import getBarcodeData
from perspectivetransform import get_perspective_transform
class processPaperandHeader:
    def func_getPerspectiveTransform(self, src_points, image, header_lower, header_upper, application_names, roi, command):


        # src_points.reverse()
        # reverse_points(src_points, 1,2)
        # reverse_points(src_points, 2,3)

        try:
            M, warp_image = get_perspective_transform(src_points, image)
            points = vir_pointer.get_pointer_header(image, header_lower, header_upper)
            # points = getIndexFingerPoints(image)
            barcode_data = getBarcodeData(warp_image)
            if barcode_data:
                print(points)
                if points:
                    print("this is it")
                    single_vec = [[points[0]], [points[1]], [1]]
                    # single_vec=[[1269], [668], [1]]
                    result = np.dot(M, single_vec)
                    result = result.astype(int)
                    print(result.astype(int))
                    if result[0]>0  and result[0]<1980 and result[1]>0 and result[1]<1080:
                        # open the application pointed
                        applicationOpener().open_application(result, barcode_data, application_names, roi, command)
                        print("in range")
                    else:
                        print("out of range")
        except Exception as error:
            print(error)