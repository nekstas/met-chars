# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameScreen(object):
    def setupUi(self, GameScreen):
        GameScreen.setObjectName("GameScreen")
        GameScreen.resize(360, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GameScreen.sizePolicy().hasHeightForWidth())
        GameScreen.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(GameScreen)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.displays = QtWidgets.QWidget(GameScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.displays.sizePolicy().hasHeightForWidth())
        self.displays.setSizePolicy(sizePolicy)
        self.displays.setObjectName("displays")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.displays)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_display = QtWidgets.QTextBrowser(self.displays)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.main_display.sizePolicy().hasHeightForWidth())
        self.main_display.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.main_display.setFont(font)
        self.main_display.setStyleSheet("")
        self.main_display.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_display.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_display.setReadOnly(True)
        self.main_display.setObjectName("main_display")
        self.verticalLayout.addWidget(self.main_display)
        self.sub_display = QtWidgets.QLabel(self.displays)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sub_display.sizePolicy().hasHeightForWidth())
        self.sub_display.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.sub_display.setFont(font)
        self.sub_display.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sub_display.setText("")
        self.sub_display.setAlignment(QtCore.Qt.AlignCenter)
        self.sub_display.setObjectName("sub_display")
        self.verticalLayout.addWidget(self.sub_display)
        self.main_layout.addWidget(self.displays)
        self.cells_widget = QtWidgets.QWidget(GameScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.cells_widget.sizePolicy().hasHeightForWidth())
        self.cells_widget.setSizePolicy(sizePolicy)
        self.cells_widget.setObjectName("cells_widget")
        self.cells_layout = QtWidgets.QGridLayout(self.cells_widget)
        self.cells_layout.setContentsMargins(0, 0, 0, 0)
        self.cells_layout.setSpacing(10)
        self.cells_layout.setObjectName("cells_layout")
        self.main_layout.addWidget(self.cells_widget)
        self.status_labels = QtWidgets.QWidget(GameScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_labels.sizePolicy().hasHeightForWidth())
        self.status_labels.setSizePolicy(sizePolicy)
        self.status_labels.setObjectName("status_labels")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.status_labels)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.moves_count_label = QtWidgets.QLabel(self.status_labels)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moves_count_label.sizePolicy().hasHeightForWidth())
        self.moves_count_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.moves_count_label.setFont(font)
        self.moves_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.moves_count_label.setObjectName("moves_count_label")
        self.horizontalLayout_2.addWidget(self.moves_count_label)
        self.level_num_label = QtWidgets.QLabel(self.status_labels)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.level_num_label.sizePolicy().hasHeightForWidth())
        self.level_num_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.level_num_label.setFont(font)
        self.level_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.level_num_label.setObjectName("level_num_label")
        self.horizontalLayout_2.addWidget(self.level_num_label)
        self.time_label = QtWidgets.QLabel(self.status_labels)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.time_label.setFont(font)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_2.addWidget(self.time_label)
        self.main_layout.addWidget(self.status_labels)
        self.buttons = QtWidgets.QWidget(GameScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy)
        self.buttons.setObjectName("buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttons)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.go_back_btn = QtWidgets.QPushButton(self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_back_btn.sizePolicy().hasHeightForWidth())
        self.go_back_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.go_back_btn.setFont(font)
        self.go_back_btn.setObjectName("go_back_btn")
        self.horizontalLayout.addWidget(self.go_back_btn)
        self.restart_level_btn = QtWidgets.QPushButton(self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restart_level_btn.sizePolicy().hasHeightForWidth())
        self.restart_level_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.restart_level_btn.setFont(font)
        self.restart_level_btn.setObjectName("restart_level_btn")
        self.horizontalLayout.addWidget(self.restart_level_btn)
        self.main_layout.addWidget(self.buttons)
        self.gridLayout.addLayout(self.main_layout, 0, 0, 1, 1)

        self.retranslateUi(GameScreen)
        QtCore.QMetaObject.connectSlotsByName(GameScreen)

    def retranslateUi(self, GameScreen):
        _translate = QtCore.QCoreApplication.translate
        GameScreen.setWindowTitle(_translate("GameScreen", "MetChars - Игра"))
        self.main_display.setHtml(_translate("GameScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.moves_count_label.setText(_translate("GameScreen", "<ходы>"))
        self.level_num_label.setText(_translate("GameScreen", "<уровень>"))
        self.time_label.setText(_translate("GameScreen", "<время>"))
        self.go_back_btn.setText(_translate("GameScreen", "Назад"))
        self.restart_level_btn.setText(_translate("GameScreen", "Перезапустить уровень"))
