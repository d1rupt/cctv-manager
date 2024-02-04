import cv2

def list_cameras_ids():
    index = 0
    arr = []
    for index in range(10):
        cap = cv2.VideoCapture(index,cv2.CAP_DSHOW)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr
