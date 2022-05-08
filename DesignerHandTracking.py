# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesignerHandTracking.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



import sys
import numpy as np
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import mediapipe
import autopy
import math
import subprocess
import pyautogui
from User import Ui_MainWindow
from PyQt5.QtWidgets import *

initHand = mediapipe.solutions.hands  # Initializing mediapipe
# Object of mediapipe with "arguments for the hands module"
mainHand = initHand.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
draw = mediapipe.solutions.drawing_utils  # Object to draw the connections between each finger index
wScr, hScr = autopy.screen.size()  # Outputs the high and width of the screen


class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setObjectName("Dialog")
        Dialog.resize(958, 501)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);\n")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 951, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(742, 495))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/QUYGAMING/Downloads/tri_tue_nhan_tao.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.setStretch(0, 7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(190, 145))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/QUYGAMING/Downloads/z3360920595987_e152134d58ff58d28d5f3f9922a4ac40.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.verticalLayout_8)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.cbHCam = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.cbHCam.setEnabled(True)
        self.cbHCam.setStyleSheet("font-family: century gothic;\n"
"font-size: 16px;\n"
"color: rgb(31, 52, 110);")
        self.cbHCam.setObjectName("cbHCam")
        self.verticalLayout_9.addWidget(self.cbHCam)
        self.verticalLayout_9.setStretch(0, 2)
        self.verticalLayout_5.addLayout(self.verticalLayout_9)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btnActivate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnActivate.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(31, 52, 110);\n"
"border-radius: 10px;\n"
"border: 2px solid #f6d70a;\n"
"padding: 5px;\n"                                        
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(245, 197, 4);\n"
"}")
        self.btnActivate.setObjectName("btnActivate")
        self.verticalLayout_6.addWidget(self.btnActivate)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.btnUManual = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnUManual.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(31, 52, 110);\n"
"border-radius: 10px;\n"
"border: 2px solid #f6d70a;\n"
"padding: 5px;\n"                                        
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(245, 197, 4);\n"
"}")
        self.btnUManual.setObjectName("btnUManual")
        self.verticalLayout_6.addWidget(self.btnUManual)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.btnQuit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnQuit.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(31, 52, 110);\n"
"border-radius: 10px;\n"
"border: 2px solid #f6d70a;\n"
"padding: 5px;\n"  
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(245, 197, 4);\n"
"}")
        self.btnQuit.setObjectName("btnQuit")
        self.verticalLayout_6.addWidget(self.btnQuit)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(2, 2)
        self.verticalLayout_6.setStretch(4, 2)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_5.setStretch(0, 4)
        self.verticalLayout_5.setStretch(2, 7)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(2, 7)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.setStretch(0, 12)
        self.horizontalLayout.setStretch(1, 3)
        self.btnQuit.clicked.connect(self.fQuit)

        self.btnActivate.clicked.connect(self.fOpenCam)

        self.cbHCam.stateChanged.connect(self.fHCam)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def fHCam(self):
        if self.cbHCam.isChecked():
            self.label_2.hide()
        else:
            self.label_2.show()
    def fQuit(self):
        exit(0)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Hand Tracking"))
        self.cbHCam.setText(_translate("Dialog", "Hide Camera"))
        self.btnActivate.setText(_translate("Dialog", "Activate"))
        self.btnUManual.setText(_translate("Dialog", "User Manual"))
        self.btnQuit.setText(_translate("Dialog", "Quit"))

    def handLandmarks(self,colorImg):
        landmarkList = []  # Default values if no landmarks are tracked

        landmarkPositions = mainHand.process(colorImg)  # Object for processing the video input
        landmarkCheck = landmarkPositions.multi_hand_landmarks  # Stores the out of the processing object (returns False on empty)
        if landmarkCheck:  # Checks if landmarks are tracked
            for hand in landmarkCheck:  # Landmarks for each hand
                for index, landmark in enumerate(
                        hand.landmark):  # Loops through the 21 indexes and outputs their landmark coordinates (x, y, & z)
                    draw.draw_landmarks(self.frame, hand,
                                        initHand.HAND_CONNECTIONS)  # Draws each individual index on the hand with connections
                    h, w, c = self.frame.shape  # Height, width and channel on the image
                    centerX, centerY = int(landmark.x * w), int(
                        landmark.y * h)  # Converts the decimal coordinates relative to the image for each index
                    landmarkList.append([index, centerX, centerY])  # Adding index and its coordinates to a list

        return landmarkList

    def fingers(self,landmarks):
        fingerTips = []  # To store 4 sets of 1s or 0s
        tipIds = [4, 8, 12, 16, 20]  # Indexes for the tips of each finger

        # Check if thumb is up
        if landmarks[tipIds[0]][1] > landmarks[tipIds[0] - 1][1]:
            fingerTips.append(1)
        else:
            fingerTips.append(0)

        # Check if fingers are up except the thumb
        for id in range(1, 5):
            if landmarks[tipIds[id]][2] < landmarks[tipIds[id] - 3][
                2]:  # Checks to see if the tip of the finger is higher than the joint
                fingerTips.append(1)
            else:
                fingerTips.append(0)

        return fingerTips
    def fOpenCam(self):
        wCam, hCam = 750, 495
        smoothening = 5

        pX, pY = 0, 0
        cX, cY = 0, 0
        cam = True
        if cam:
            self.vid = cv2.VideoCapture(0)
            self.vid.set(3,wCam)
            self.vid.set(4,hCam)
        else:
            print("khong mo duoc cam")
        while True:
            OK, self.frame = self.vid.read()
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            lmList = self.handLandmarks(self.frame)
            cv2.rectangle(self.frame, (40, 40), (wCam - 150, hCam - 120), (255, 0, 255), 2)


            if len(lmList) != 0:
                x1, y1 = lmList[8][1:]  # Gets index 8s x and y values (skips index value because it starts from 1)
                # x2, y2 = lmList[12][1:]  # Gets index 12s x and y values (skips index value because it starts from 1)
                # x3, y3 = lmList[4][1:]
                finger = self.fingers(lmList)  # Calling the fingers function to check which fingers are up


                if finger[1] == 1 and finger[2] == 0 and finger[0] == 0 and finger[3] == 0 and finger[
                    4] == 0:  # Checks to see if the pointing finger is up and thumb finger is down


                   try:
                       x3 = np.interp(x1, (40, wCam - 150),
                                      (0, wScr))  # Converts the width of the window relative to the screen width
                       y3 = np.interp(y1, (40, hCam - 150),
                                      (0, hScr))  # Converts the height of the window relative to the screen height
                       # cX = pX + (x3 - pX) / 7  # Stores previous x locations to update current x location
                       # cY = pY + (y3 - pY) / 7  # Stores previous y locations to update current y location
                       cX = pX + (x3 - pX) / smoothening
                       cY = pY + (y3 - pY) / smoothening
                       autopy.mouse.move(wScr - x3,
                                         y3)  # Function to move the mouse to the x3 and y3 values (wSrc inverts the direction)
                       cv2.circle(self.frame, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
                       pX, pY = cX, cY
                   except Exception as ex:
                       print(ex)
                    # pX, pY = cX, cY  # Stores the current x and y location as previous x and y location for next loop
                def kc(a, b):
                    x1, y1 = lmList[a][1:]  # Gets index 8s x and y values (skips index value because it starts from 1)
                    x2, y2 = lmList[b][1:]
                    return math.hypot(x2 - x1, y2 - y1)



                # LeftClick
                if finger[1] == 1 and finger[2] == 1:  # Checks to see if the pointer finger is down and thumb finger is up
                    length = kc(8, 5)
                    #print(length)
                    if length < 30:
                        autopy.mouse.click()

                length3 = kc(4, 20)
                length4 = kc(4,8)

                    #open Chrome
                if finger[1] == 1 and finger[2] == 1 and finger[0] == 1 and finger[3] == 1 and finger[4] == 1:

                    if length3 > 270:
                        proc = subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')
                length2 = kc(8, 12)
                #     #RightClick
                if finger[0] == 0 and finger[1] == 1 and finger[2] == 1 and finger[3] == 0 and finger[4] == 0:
                    if length2 < 19:
                        autopy.mouse.click(autopy.mouse.Button.RIGHT)

                    #Scroll
                if finger[0] == 1 and finger[1] == 0 and finger[2] == 0 and finger[3] == 0 and finger[4] == 0:
                    if length4 < 25:
                        pyautogui.scroll(-100)


                if finger[0] == 1 and finger[1] == 0 and finger[2] == 1 and finger[3] == 1 and finger[4] == 1:
                    if length4 < 25:
                        pyautogui.scroll(100)

            self.update()

            if cv2.waitKey(1) &0xFF == ord('q'):
                break



    def update(self):


        self.setPhoto(self.frame)


    def setPhoto(self, image):
        image = cv2.resize(image,(750,495))
        img = QtGui.QImage(image, image.shape[1], image.shape[0], image.strides[0],
                           QtGui.QImage.Format_RGB888)
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(img))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    Dialog =QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
