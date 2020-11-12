import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'PATH_TO_tesseract.exe'
img = cv2.imread('/test-images/sample5.jpg')

imgH, imgW, _ = img.shape

#Detecting Characters
boxes = pytesseract.image_to_boxes(img)

for box in boxes.splitlines():
    box = box.split(' ')
    #print(box)
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    name = box[0]
    cv2.rectangle(img, (x, imgH-y), (w, imgH-h), (50,50,255), 1)
    cv2.putText(img, name, (x, imgH-y+25), cv2.FONT_HERSHEY_PLAIN, 1, (50,50,255), 2)

cv2.imshow('Text-Detection', img)
key = cv2.waitKey(0)
