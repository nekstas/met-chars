# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameMenu(object):
    def setupUi(self, GameMenu):
        GameMenu.setObjectName("GameMenu")
        GameMenu.resize(360, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GameMenu.sizePolicy().hasHeightForWidth())
        GameMenu.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(GameMenu)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.app_name_label = QtWidgets.QLabel(GameMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_name_label.sizePolicy().hasHeightForWidth())
        self.app_name_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.app_name_label.setFont(font)
        self.app_name_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.app_name_label.setObjectName("app_name_label")
        self.main_layout.addWidget(self.app_name_label)
        self.buttons = QtWidgets.QWidget(GameMenu)
        self.buttons.setObjectName("buttons")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.buttons)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.play_btn = QtWidgets.QPushButton(self.buttons)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.play_btn.setFont(font)
        self.play_btn.setStyleSheet("padding: 10px;")
        self.play_btn.setObjectName("play_btn")
        self.verticalLayout.addWidget(self.play_btn)
        self.players_btn = QtWidgets.QPushButton(self.buttons)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.players_btn.setFont(font)
        self.players_btn.setStyleSheet("padding: 10px;")
        self.players_btn.setObjectName("players_btn")
        self.verticalLayout.addWidget(self.players_btn)
        self.exit_btn = QtWidgets.QPushButton(self.buttons)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("padding: 10px;")
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout.addWidget(self.exit_btn)
        self.main_layout.addWidget(self.buttons)
        self.player_name_label = QtWidgets.QLabel(GameMenu)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.player_name_label.setFont(font)
        self.player_name_label.setText("")
        self.player_name_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.player_name_label.setWordWrap(True)
        self.player_name_label.setObjectName("player_name_label")
        self.main_layout.addWidget(self.player_name_label)
        self.author_label = QtWidgets.QLabel(GameMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.author_label.sizePolicy().hasHeightForWidth())
        self.author_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.author_label.setFont(font)
        self.author_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.author_label.setObjectName("author_label")
        self.main_layout.addWidget(self.author_label)
        self.gridLayout.addLayout(self.main_layout, 0, 0, 1, 1)

        self.retranslateUi(GameMenu)
        QtCore.QMetaObject.connectSlotsByName(GameMenu)

    def retranslateUi(self, GameMenu):
        _translate = QtCore.QCoreApplication.translate
        GameMenu.setWindowTitle(_translate("GameMenu", "MetChars - Меню"))
        self.app_name_label.setText(_translate("GameMenu", "MetChars"))
        self.play_btn.setText(_translate("GameMenu", "Играть"))
        self.players_btn.setText(_translate("GameMenu", "Игроки"))
        self.exit_btn.setText(_translate("GameMenu", "Выход"))
        self.author_label.setText(_translate("GameMenu", "ЯЛ - Некрасов Станислав 2021"))