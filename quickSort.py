# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quick_sort.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

def main():
    class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(995, 970)
            MainWindow.setMinimumSize(QtCore.QSize(994, 965))
            MainWindow.setMaximumSize(QtCore.QSize(995, 970))
            MainWindow.setStyleSheet('background:#001219; color:#ee9b00')

            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
            self.scrollArea.setGeometry(QtCore.QRect(1, 2, 991, 951))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
            self.scrollArea.setSizePolicy(sizePolicy)
            self.scrollArea.setMinimumSize(QtCore.QSize(0, 500))
            self.scrollArea.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.WaitCursor))
            self.scrollArea.setAcceptDrops(False)
            self.scrollArea.setAutoFillBackground(True)
            self.scrollArea.setStyleSheet("border:none;\n"
    "QScrollBar\n"
    "{\n"
    "background : lightgreen;}")
            self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.scrollArea.setObjectName("scrollArea")
            self.scrollAreaWidgetContents = QtWidgets.QWidget()
            self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -367, 970, 1318))
            self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            self.frame.setMinimumSize(QtCore.QSize(0, 1300))
            self.frame.setAcceptDrops(False)
            self.frame.setStyleSheet("border:none")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
            self.frame.setObjectName("frame")
            self.complexity_table = QtWidgets.QTableWidget(self.frame)
            self.complexity_table.setGeometry(QtCore.QRect(30, 1140, 501, 61))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(12)
            self.complexity_table.setFont(font)
            self.complexity_table.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.complexity_table.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.complexity_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.complexity_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.complexity_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.complexity_table.setGridStyle(QtCore.Qt.SolidLine)
            self.complexity_table.setObjectName("complexity_table")
            self.complexity_table.setColumnCount(5)
            self.complexity_table.setRowCount(1)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(12)
            item.setFont(font)
            item.setBackground(QtGui.QColor(255, 255, 255))
            self.complexity_table.setVerticalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(12)
            item.setFont(font)
            self.complexity_table.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.complexity_table.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            self.complexity_table.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            self.complexity_table.setHorizontalHeaderItem(3, item)
            item = QtWidgets.QTableWidgetItem()
            self.complexity_table.setHorizontalHeaderItem(4, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.complexity_table.setItem(0, 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.complexity_table.setItem(0, 1, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.complexity_table.setItem(0, 2, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.complexity_table.setItem(0, 3, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.complexity_table.setItem(0, 4, item)
            self.complexity_table.horizontalHeader().setVisible(True)
            self.complexity_table.horizontalHeader().setCascadingSectionResizes(False)
            self.complexity_table.horizontalHeader().setHighlightSections(True)
            self.complexity_table.verticalHeader().setVisible(False)
            self.complexity_table.verticalHeader().setHighlightSections(True)
            self.complexity = QtWidgets.QLabel(self.frame)
            self.complexity.setGeometry(QtCore.QRect(20, 1080, 211, 41))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.complexity.setFont(font)
            self.complexity.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.complexity.setTextFormat(QtCore.Qt.PlainText)
            self.complexity.setObjectName("complexity")
            self.algo_header = QtWidgets.QLabel(self.frame)
            self.algo_header.setGeometry(QtCore.QRect(20, 530, 331, 41))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.algo_header.setFont(font)
            self.algo_header.setObjectName("algo_header")
            self.header_label = QtWidgets.QLabel(self.frame)
            self.header_label.setGeometry(QtCore.QRect(10, 0, 251, 51))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(25)
            font.setBold(True)
            font.setWeight(75)
            self.header_label.setFont(font)
            self.header_label.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.header_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.header_label.setObjectName("header_label")
            self.algorithm = QtWidgets.QLabel(self.frame)
            self.algorithm.setGeometry(QtCore.QRect(20, 580, 911, 471))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(14)
            self.algorithm.setFont(font)
            self.algorithm.setTextFormat(QtCore.Qt.AutoText)
            self.algorithm.setScaledContents(True)
            self.algorithm.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.algorithm.setWordWrap(True)
            self.algorithm.setObjectName("algorithm")
            self.gif_label = QtWidgets.QLabel(self.frame)
            self.gif_label.setGeometry(QtCore.QRect(30, 310, 401, 201))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(14)
            self.gif_label.setFont(font)
            self.gif_label.setScaledContents(True)
            self.gif_label.setObjectName("gif_label")
            self.header_info_label = QtWidgets.QLabel(self.frame)
            self.header_info_label.setGeometry(QtCore.QRect(20, 70, 911, 221))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(14)
            font.setBold(False)
            font.setWeight(50)
            self.header_info_label.setFont(font)
            self.header_info_label.setFocusPolicy(QtCore.Qt.NoFocus)
            self.header_info_label.setTextFormat(QtCore.Qt.AutoText)
            self.header_info_label.setScaledContents(False)
            self.header_info_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
            self.header_info_label.setWordWrap(True)
            self.header_info_label.setIndent(1)
            self.header_info_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
            self.header_info_label.setObjectName("header_info_label")
            self.verticalLayout_2.addWidget(self.frame)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            MainWindow.setCentralWidget(self.centralwidget)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "Quick Sort"))
            item = self.complexity_table.verticalHeaderItem(0)
            item.setText(_translate("MainWindow", "Mergesort"))
            item = self.complexity_table.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Best"))
            item = self.complexity_table.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Average"))
            item = self.complexity_table.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "Worst"))
            item = self.complexity_table.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "Memory"))
            item = self.complexity_table.horizontalHeaderItem(4)
            item.setText(_translate("MainWindow", "Stable"))
            __sortingEnabled = self.complexity_table.isSortingEnabled()
            self.complexity_table.setSortingEnabled(False)
            item = self.complexity_table.item(0, 0)
            item.setText(_translate("MainWindow", "n log (n)"))
            item = self.complexity_table.item(0, 1)
            item.setText(_translate("MainWindow", "n log (n)"))
            item = self.complexity_table.item(0, 2)
            item.setText(_translate("MainWindow", "n log (n)"))
            item = self.complexity_table.item(0, 3)
            item.setText(_translate("MainWindow", "n"))
            item = self.complexity_table.item(0, 4)
            item.setText(_translate("MainWindow", "Yes"))
            self.complexity_table.setSortingEnabled(__sortingEnabled)
            self.complexity.setText(_translate("MainWindow", "Complexity"))
            self.algo_header.setText(_translate("MainWindow", "Algorithm:"))
            self.header_label.setText(_translate("MainWindow", "QuickSort"))
            self.algorithm.setText(_translate("MainWindow", "Quick Sort Pivot Algorithm \n"
    "\n"
    "Step 1 − Choose the highest index value has pivot\n"
    "Step 2 − Take two variables to point left and right of the list excluding pivot\n"
    "Step 3 − left points to the low index\n"
    "Step 4 − right points to the high\n"
    "Step 5 − while value at left is less than pivot move right\n"
    "Step 6 − while value at right is greater than pivot move left\n"
    "Step 7 − if both step 5 and step 6 does not match swap left and right\n"
    "Step 8 − if left ≥ right, the point where they met is new pivot.\n"
    "\n"
    "Quick Sort Algorithm\n"
    "\n"
    "Step 1 − Make the right-most index value pivot\n"
    "Step 2 − partition the array using pivot value\n"
    "Step 3 − quicksort left partition recursively\n"
    "Step 4 − quicksort right partition recursively"))
            self.gif_label.setText(_translate("MainWindow", "Quick-sort-gif-example"))
            self.movie = QMovie(r".\gifs\Quick-sort.gif")
            self.gif_label.setMovie(self.movie)
            self.movie.start()

            self.header_info_label.setText(_translate("MainWindow", "Quick sort is a highly efficient sorting algorithm and is based on partitioning of array of data into smaller arrays. A large array is partitioned into two arrays one of which holds values smaller than the specified value, say pivot, based on which the partition is made and another array holds values greater than the pivot value.\n"
    "\n"
    "Quicksort partitions an array and then calls itself recursively twice to sort the two resulting subarrays. This algorithm is quite efficient for large-sized data sets as its average and worst-case complexity are O(n2), respectively."))



    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
