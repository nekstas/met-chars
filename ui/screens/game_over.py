# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_over.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameOverScreen(object):
    def setupUi(self, GameOverScreen):
        GameOverScreen.setObjectName("GameOverScreen")
        GameOverScreen.resize(360, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GameOverScreen.sizePolicy().hasHeightForWidth())
        GameOverScreen.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(GameOverScreen)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.game_over_label = QtWidgets.QLabel(GameOverScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_over_label.sizePolicy().hasHeightForWidth())
        self.game_over_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.game_over_label.setFont(font)
        self.game_over_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.game_over_label.setObjectName("game_over_label")
        self.verticalLayout.addWidget(self.game_over_label)
        self.game_over_text_label = QtWidgets.QLabel(GameOverScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.game_over_text_label.sizePolicy().hasHeightForWidth())
        self.game_over_text_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.game_over_text_label.setFont(font)
        self.game_over_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.game_over_text_label.setWordWrap(True)
        self.game_over_text_label.setObjectName("game_over_text_label")
        self.verticalLayout.addWidget(self.game_over_text_label)
        self.go_levels_btn = QtWidgets.QPushButton(GameOverScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.go_levels_btn.sizePolicy().hasHeightForWidth())
        self.go_levels_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.go_levels_btn.setFont(font)
        self.go_levels_btn.setStyleSheet("padding: 5px;")
        self.go_levels_btn.setObjectName("go_levels_btn")
        self.verticalLayout.addWidget(self.go_levels_btn)
        self.exit_btn = QtWidgets.QPushButton(GameOverScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("padding: 5px;")
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout.addWidget(self.exit_btn)

        self.retranslateUi(GameOverScreen)
        QtCore.QMetaObject.connectSlotsByName(GameOverScreen)

    def retranslateUi(self, GameOverScreen):
        _translate = QtCore.QCoreApplication.translate
        GameOverScreen.setWindowTitle(_translate("GameOverScreen", "MetChars - Игра пройдена!"))
        self.game_over_label.setText(_translate("GameOverScreen", "Игра пройдена!"))
        self.game_over_text_label.setText(_translate("GameOverScreen", "<поздравительный текст>"))
        self.go_levels_btn.setText(_translate("GameOverScreen", "К списку уровней"))
        self.exit_btn.setText(_translate("GameOverScreen", "Выйти из игры"))