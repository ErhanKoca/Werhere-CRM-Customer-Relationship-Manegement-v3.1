# Form implementation generated from reading ui file 'd:\VsCode_Gitbub\Werhere-CRM-Customer-Relationship-Manegement-v3.1\Ui\interviews_page.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_interviews_page_MainWindow(object):
    def setupUi(self, interviews_page_MainWindow):
        interviews_page_MainWindow.setObjectName("interviews_page_MainWindow")
        interviews_page_MainWindow.resize(636, 650)
        interviews_page_MainWindow.setMinimumSize(QtCore.QSize(636, 650))
        interviews_page_MainWindow.setMaximumSize(QtCore.QSize(636, 711))
        self.centralwidget = QtWidgets.QWidget(parent=interviews_page_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(600, 650))
        self.frame.setMaximumSize(QtCore.QSize(600, 650))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.search_lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.search_lineEdit.setGeometry(QtCore.QRect(10, 160, 421, 31))
        self.search_lineEdit.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.search_lineEdit.setAccessibleName("")
        self.search_lineEdit.setAccessibleDescription("")
        self.search_lineEdit.setAutoFillBackground(False)
        self.search_lineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.search_lineEdit.setInputMask("")
        self.search_lineEdit.setText("")
        self.search_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.search_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.search_lineEdit.setDragEnabled(False)
        self.search_lineEdit.setReadOnly(False)
        self.search_lineEdit.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.search_lineEdit.setClearButtonEnabled(False)
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.search_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.search_pushButton.setGeometry(QtCore.QRect(470, 160, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.search_pushButton.setFont(font)
        self.search_pushButton.setStyleSheet("\n"
"QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }\n"
"")
        self.search_pushButton.setObjectName("search_pushButton")
        self.submitted_projects_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.submitted_projects_pushButton.setGeometry(QtCore.QRect(10, 220, 181, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.submitted_projects_pushButton.setFont(font)
        self.submitted_projects_pushButton.setStyleSheet("\n"
"QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }\n"
"")
        self.submitted_projects_pushButton.setObjectName("submitted_projects_pushButton")
        self.back_to_preferences_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.back_to_preferences_pushButton.setGeometry(QtCore.QRect(10, 270, 181, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.back_to_preferences_pushButton.setFont(font)
        self.back_to_preferences_pushButton.setStyleSheet("\n"
"QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }\n"
"")
        self.back_to_preferences_pushButton.setObjectName("back_to_preferences_pushButton")
        self.arrived_projects_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.arrived_projects_pushButton.setGeometry(QtCore.QRect(410, 220, 181, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.arrived_projects_pushButton.setFont(font)
        self.arrived_projects_pushButton.setStyleSheet("\n"
"QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }\n"
"")
        self.arrived_projects_pushButton.setObjectName("arrived_projects_pushButton")
        self.exit_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.exit_pushButton.setGeometry(QtCore.QRect(410, 270, 181, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.exit_pushButton.setFont(font)
        self.exit_pushButton.setStyleSheet("\n"
"QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }\n"
"")
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.interviews_page_tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.interviews_page_tableWidget.setGeometry(QtCore.QRect(10, 340, 581, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interviews_page_tableWidget.sizePolicy().hasHeightForWidth())
        self.interviews_page_tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        self.interviews_page_tableWidget.setFont(font)
        self.interviews_page_tableWidget.setLineWidth(0)
        self.interviews_page_tableWidget.setMidLineWidth(0)
        self.interviews_page_tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.interviews_page_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.interviews_page_tableWidget.setAutoScroll(True)
        self.interviews_page_tableWidget.setObjectName("interviews_page_tableWidget")
        self.interviews_page_tableWidget.setColumnCount(3)
        self.interviews_page_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.interviews_page_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.interviews_page_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.interviews_page_tableWidget.setHorizontalHeaderItem(2, item)
        self.interviews_page_tableWidget.horizontalHeader().setVisible(True)
        self.interviews_page_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.interviews_page_tableWidget.horizontalHeader().setDefaultSectionSize(193)
        self.interviews_page_tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.interviews_page_tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.interviews_page_tableWidget.verticalHeader().setMinimumSectionSize(24)
        self.interviews_image_label = QtWidgets.QLabel(parent=self.frame)
        self.interviews_image_label.setGeometry(QtCore.QRect(20, 0, 551, 141))
        self.interviews_image_label.setText("")
        self.interviews_image_label.setPixmap(QtGui.QPixmap("d:\\VsCode_Gitbub\\Werhere-CRM-Customer-Relationship-Manegement-v3.1\\Ui\\werhere_image.png"))
        self.interviews_image_label.setObjectName("interviews_image_label")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        interviews_page_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=interviews_page_MainWindow)
        self.statusbar.setObjectName("statusbar")
        interviews_page_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(interviews_page_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(interviews_page_MainWindow)

    def retranslateUi(self, interviews_page_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        interviews_page_MainWindow.setWindowTitle(_translate("interviews_page_MainWindow", "                                                        INTERVIEWS PAGE"))
        self.search_pushButton.setText(_translate("interviews_page_MainWindow", "SEARCH"))
        self.submitted_projects_pushButton.setText(_translate("interviews_page_MainWindow", "SUBMITTED PROJECTS"))
        self.back_to_preferences_pushButton.setText(_translate("interviews_page_MainWindow", "BACK TO PREFERENCES"))
        self.arrived_projects_pushButton.setText(_translate("interviews_page_MainWindow", "ARRIVED PROJECTS"))
        self.exit_pushButton.setText(_translate("interviews_page_MainWindow", "EXIT"))
        item = self.interviews_page_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("interviews_page_MainWindow", "Name"))
        item = self.interviews_page_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("interviews_page_MainWindow", "Project Submission Date"))
        item = self.interviews_page_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("interviews_page_MainWindow", "Project Arrival Date"))