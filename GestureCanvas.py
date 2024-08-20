import cv2
import numpy as np
import os
import HandTrackingModule as htm

brushThickness = 8
eraserThickness = 100

FIRSTCOLOR = (108, 108, 108)
SECONDCOLOR = (252, 172, 226)
THIRDCOLOR = (85, 251, 146)

folderPath = "Header"
myList = os.listdir(folderPath)
myList.remove(".DS_Store")
overlayList = []
for imPath in myList:
    image = cv2.imread(f"{folderPath}/{imPath}")
    overlayList.append(image)
header = overlayList[3]
drawColor = FIRSTCOLOR

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.65, maxHands=1)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList[0]) != 0:

        if len(lmList[0]) > 12:
            x1, y1 = lmList[0][8][1:]
            x2, y2 = lmList[0][12][1:]

            fingers = detector.fingersUp()

            if fingers[1] and fingers[2]:
                xp, yp = 0, 0
                if y1 < 125:
                    if 60 < x1 < 180:
                        header = overlayList[3]
                        drawColor = FIRSTCOLOR
                    elif 280 < x1 < 400:
                        header = overlayList[1]
                        drawColor = SECONDCOLOR
                    elif 500 < x1 < 630:
                        header = overlayList[2]
                        drawColor = THIRDCOLOR
                    elif 730 < x1 < 815:
                        if drawColor == (0, 0, 0):
                            if eraserThickness > 30:
                                eraserThickness -= 1
                        else:
                            if brushThickness > 5:
                                brushThickness -= 1
                    elif 880 < x1 < 980:
                        if drawColor == (0, 0, 0):
                            if eraserThickness < 200:
                                eraserThickness += 1
                        else:
                            if brushThickness < 100:
                                brushThickness += 1
                    elif 1090 < x1 < 1210:
                        header = overlayList[0]
                        drawColor = (0, 0, 0)
                cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

            if not fingers[1]:
                xp, yp = 0, 0
            if fingers[1] and not fingers[2]:
                cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
                if xp == 0 and yp == 0:
                    xp, yp = x1, y1
                if drawColor == (0, 0, 0):
                    cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
                else:
                    cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

                xp, yp = x1, y1

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    img[0:125, 0:1280] = header

    cv2.imshow("GestureCanvas", img)
    # cv2.imshow("Canvas", imgCanvas)
    # cv2.imshow("Inv", imgInv)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
