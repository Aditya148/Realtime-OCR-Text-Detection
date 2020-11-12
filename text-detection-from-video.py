import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
cap = cv2.VideoCapture('C:/Users/adih4/OneDrive/Desktop/Projects/PyProjects/Text-Detection/test-video/sample3.mp4') 

while True:
    ret, frame = cap.read()

    imgH, imgW, _ = frame.shape

    #Detecting Characters
    boxes = pytesseract.image_to_boxes(frame)

    for box in boxes.splitlines():
        box = box.split(' ')
        #print(box)
        x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
        name = box[0]
        cv2.rectangle(frame, (x, imgH-y), (w, imgH-h), (50,50,255), 1)
        cv2.putText(frame, name, (x, imgH-y+25), cv2.FONT_HERSHEY_PLAIN, 1, (50,50,255), 2)

    cv2.imshow('Text-Detection', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()