# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlayerItem(object):
    def setupUi(self, PlayerItem):
        PlayerItem.setObjectName("PlayerItem")
        PlayerItem.resize(400, 100)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(PlayerItem)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.player_name_label = QtWidgets.QLabel(PlayerItem)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.player_name_label.setFont(font)
        self.player_name_label.setObjectName("player_name_label")
        self.verticalLayout_2.addWidget(self.player_name_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.selected_label = QtWidgets.QLabel(PlayerItem)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selected_label.setFont(font)
        self.selected_label.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_label.setObjectName("selected_label")
        self.horizontalLayout_3.addWidget(self.selected_label)
        self.select_btn = QtWidgets.QPushButton(PlayerItem)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.select_btn.setFont(font)
        self.select_btn.setObjectName("select_btn")
        self.horizontalLayout_3.addWidget(self.select_btn)
        self.change_name_btn = QtWidgets.QPushButton(PlayerItem)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.change_name_btn.setFont(font)
        self.change_name_btn.setObjectName("change_name_btn")
        self.horizontalLayout_3.addWidget(self.change_name_btn)
        self.delete_btn = QtWidgets.QPushButton(PlayerItem)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.delete_btn.setFont(font)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_3.addWidget(self.delete_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(PlayerItem)
        QtCore.QMetaObject.connectSlotsByName(PlayerItem)

    def retranslateUi(self, PlayerItem):
        _translate = QtCore.QCoreApplication.translate
        PlayerItem.setWindowTitle(_translate("PlayerItem", "Form"))
        self.player_name_label.setText(_translate("PlayerItem", "<Имя игрока>"))
        self.selected_label.setText(_translate("PlayerItem", "Выбран"))
        self.select_btn.setText(_translate("PlayerItem", "Выбрать"))
        self.change_name_btn.setText(_translate("PlayerItem", "Изменить имя"))
        self.delete_btn.setText(_translate("PlayerItem", "Удалить"))