# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StatisticsScreen(object):
    def setupUi(self, StatisticsScreen):
        StatisticsScreen.setObjectName("StatisticsScreen")
        StatisticsScreen.resize(360, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StatisticsScreen.sizePolicy().hasHeightForWidth())
        StatisticsScreen.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(StatisticsScreen)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.statistics_label = QtWidgets.QLabel(StatisticsScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statistics_label.sizePolicy().hasHeightForWidth())
        self.statistics_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.statistics_label.setFont(font)
        self.statistics_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.statistics_label.setObjectName("statistics_label")
        self.verticalLayout.addWidget(self.statistics_label)
        self.word_label = QtWidgets.QLabel(StatisticsScreen)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.word_label.setFont(font)
        self.word_label.setAlignment(QtCore.Qt.AlignCenter)
        self.word_label.setObjectName("word_label")
        self.verticalLayout.addWidget(self.word_label)
        self.statistics_table = QtWidgets.QTableWidget(StatisticsScreen)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.statistics_table.setFont(font)
        self.statistics_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.statistics_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.statistics_table.setTextElideMode(QtCore.Qt.ElideRight)
        self.statistics_table.setObjectName("statistics_table")
        self.statistics_table.setColumnCount(3)
        self.statistics_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        item.setFont(font)
        self.statistics_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.statistics_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.statistics_table.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.statistics_table)
        self.only_best_results_checkbox = QtWidgets.QCheckBox(StatisticsScreen)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.only_best_results_checkbox.setFont(font)
        self.only_best_results_checkbox.setChecked(True)
        self.only_best_results_checkbox.setTristate(False)
        self.only_best_results_checkbox.setObjectName("only_best_results_checkbox")
        self.verticalLayout.addWidget(self.only_best_results_checkbox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sort_by_label = QtWidgets.QLabel(StatisticsScreen)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.sort_by_label.setFont(font)
        self.sort_by_label.setObjectName("sort_by_label")
        self.horizontalLayout.addWidget(self.sort_by_label)
        self.by_moves_rb = QtWidgets.QRadioButton(StatisticsScreen)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.by_moves_rb.setFont(font)
        self.by_moves_rb.setChecked(True)
        self.by_moves_rb.setObjectName("by_moves_rb")
        self.horizontalLayout.addWidget(self.by_moves_rb)
        self.by_time_rb = QtWidgets.QRadioButton(StatisticsScreen)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.by_time_rb.setFont(font)
        self.by_time_rb.setObjectName("by_time_rb")
        self.horizontalLayout.addWidget(self.by_time_rb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.go_back_btn = QtWidgets.QPushButton(StatisticsScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.go_back_btn.sizePolicy().hasHeightForWidth())
        self.go_back_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.go_back_btn.setFont(font)
        self.go_back_btn.setStyleSheet("")
        self.go_back_btn.setObjectName("go_back_btn")
        self.verticalLayout.addWidget(self.go_back_btn)

        self.retranslateUi(StatisticsScreen)
        QtCore.QMetaObject.connectSlotsByName(StatisticsScreen)

    def retranslateUi(self, StatisticsScreen):
        _translate = QtCore.QCoreApplication.translate
        StatisticsScreen.setWindowTitle(_translate("StatisticsScreen", "MetChars - Статистика"))
        self.statistics_label.setText(_translate("StatisticsScreen", "Статистика по слову"))
        self.word_label.setText(_translate("StatisticsScreen", "<слово>"))
        self.statistics_table.setSortingEnabled(False)
        item = self.statistics_table.horizontalHeaderItem(0)
        item.setText(_translate("StatisticsScreen", "Имя игрока"))
        item = self.statistics_table.horizontalHeaderItem(1)
        item.setText(_translate("StatisticsScreen", "Ходы"))
        item = self.statistics_table.horizontalHeaderItem(2)
        item.setText(_translate("StatisticsScreen", "Время"))
        self.only_best_results_checkbox.setText(_translate("StatisticsScreen", "Только лучшие результаты"))
        self.sort_by_label.setText(_translate("StatisticsScreen", "Сортировать по"))
        self.by_moves_rb.setText(_translate("StatisticsScreen", "кол-ву ходов"))
        self.by_time_rb.setText(_translate("StatisticsScreen", "времени"))
        self.go_back_btn.setText(_translate("StatisticsScreen", "Назад"))
