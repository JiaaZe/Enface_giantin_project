# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'golgi_details_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Golgi_details(object):
    def setupUi(self, Golgi_details):
        # Golgi_details.setObjectName("Golgi_details")
        Golgi_details.resize(1261, 508)
        Golgi_details.setStyleSheet("")
        self.gridLayout_2 = QtWidgets.QGridLayout(Golgi_details)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(Golgi_details)
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.golgi_content_widget = QtWidgets.QWidget(self.frame)
        self.golgi_content_widget.setStyleSheet("border: 1px solid b")
        self.golgi_content_widget.setObjectName("golgi_content_widget")
        self.horizontalLayout_3.addWidget(self.golgi_content_widget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 186, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.c1_sub_horizontalLayout = QtWidgets.QHBoxLayout()
        self.c1_sub_horizontalLayout.setObjectName("c1_sub_horizontalLayout")
        self.label_c1 = QtWidgets.QLabel(self.frame)
        self.label_c1.setMinimumSize(QtCore.QSize(20, 0))
        self.label_c1.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_c1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c1.setObjectName("label_c1")
        self.c1_sub_horizontalLayout.addWidget(self.label_c1)
        self.sub_value_c1 = QtWidgets.QLineEdit(self.frame)
        self.sub_value_c1.setMinimumSize(QtCore.QSize(70, 28))
        self.sub_value_c1.setMaximumSize(QtCore.QSize(70, 28))
        self.sub_value_c1.setObjectName("sub_value_c1")
        self.c1_sub_horizontalLayout.addWidget(self.sub_value_c1)
        self.btn_sub_c1 = QtWidgets.QPushButton(self.frame)
        self.btn_sub_c1.setMinimumSize(QtCore.QSize(70, 30))
        self.btn_sub_c1.setMaximumSize(QtCore.QSize(70, 30))
        self.btn_sub_c1.setObjectName("btn_sub_c1")
        self.c1_sub_horizontalLayout.addWidget(self.btn_sub_c1)
        self.verticalLayout.addLayout(self.c1_sub_horizontalLayout)
        self.c2_sub_horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.c2_sub_horizontalLayout_2.setObjectName("c2_sub_horizontalLayout_2")
        self.label_c2 = QtWidgets.QLabel(self.frame)
        self.label_c2.setMinimumSize(QtCore.QSize(20, 0))
        self.label_c2.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_c2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c2.setObjectName("label_c2")
        self.c2_sub_horizontalLayout_2.addWidget(self.label_c2)
        self.sub_value_c2 = QtWidgets.QLineEdit(self.frame)
        self.sub_value_c2.setMinimumSize(QtCore.QSize(70, 28))
        self.sub_value_c2.setMaximumSize(QtCore.QSize(70, 28))
        self.sub_value_c2.setObjectName("sub_value_c2")
        self.c2_sub_horizontalLayout_2.addWidget(self.sub_value_c2)
        self.btn_sub_c2 = QtWidgets.QPushButton(self.frame)
        self.btn_sub_c2.setMinimumSize(QtCore.QSize(70, 30))
        self.btn_sub_c2.setMaximumSize(QtCore.QSize(70, 30))
        self.btn_sub_c2.setObjectName("btn_sub_c2")
        self.c2_sub_horizontalLayout_2.addWidget(self.btn_sub_c2)
        self.verticalLayout.addLayout(self.c2_sub_horizontalLayout_2)
        self.c3_sub_horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.c3_sub_horizontalLayout_3.setObjectName("c3_sub_horizontalLayout_3")
        self.label_c3 = QtWidgets.QLabel(self.frame)
        self.label_c3.setMinimumSize(QtCore.QSize(20, 0))
        self.label_c3.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_c3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c3.setObjectName("label_c3")
        self.c3_sub_horizontalLayout_3.addWidget(self.label_c3)
        self.sub_value_c3 = QtWidgets.QLineEdit(self.frame)
        self.sub_value_c3.setMinimumSize(QtCore.QSize(70, 28))
        self.sub_value_c3.setMaximumSize(QtCore.QSize(70, 28))
        self.sub_value_c3.setObjectName("sub_value_c3")
        self.c3_sub_horizontalLayout_3.addWidget(self.sub_value_c3)
        self.btn_sub_c3 = QtWidgets.QPushButton(self.frame)
        self.btn_sub_c3.setMinimumSize(QtCore.QSize(70, 30))
        self.btn_sub_c3.setMaximumSize(QtCore.QSize(70, 30))
        self.btn_sub_c3.setObjectName("btn_sub_c3")
        self.c3_sub_horizontalLayout_3.addWidget(self.btn_sub_c3)
        self.verticalLayout.addLayout(self.c3_sub_horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.check_save_horizontalLayout = QtWidgets.QHBoxLayout()
        self.check_save_horizontalLayout.setObjectName("check_save_horizontalLayout")
        self.btn_check = QtWidgets.QPushButton(self.frame)
        self.btn_check.setMinimumSize(QtCore.QSize(70, 30))
        self.btn_check.setMaximumSize(QtCore.QSize(70, 30))
        self.btn_check.setObjectName("btn_check")
        self.check_save_horizontalLayout.addWidget(self.btn_check)
        self.btn_export = QtWidgets.QPushButton(self.frame)
        self.btn_export.setMinimumSize(QtCore.QSize(70, 30))
        self.btn_export.setMaximumSize(QtCore.QSize(70, 30))
        self.btn_export.setObjectName("btn_export")
        self.check_save_horizontalLayout.addWidget(self.btn_export)
        self.btn_save = QtWidgets.QPushButton(self.frame)
        self.btn_save.setMinimumSize(QtCore.QSize(70, 30))
        self.btn_save.setMaximumSize(QtCore.QSize(70, 30))
        self.btn_save.setObjectName("btn_save")
        self.check_save_horizontalLayout.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.check_save_horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 186, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Golgi_details)
        self.sub_value_c1.returnPressed.connect(self.btn_sub_c1.click)
        self.sub_value_c2.returnPressed.connect(self.btn_sub_c2.click)
        self.sub_value_c3.returnPressed.connect(self.btn_sub_c3.click)
        QtCore.QMetaObject.connectSlotsByName(Golgi_details)

    def retranslateUi(self, Golgi_details):
        _translate = QtCore.QCoreApplication.translate
        Golgi_details.setWindowTitle(_translate("Golgi_details", "Golgi Details"))
        self.label_c1.setText(_translate("Golgi_details", "C1:"))
        self.btn_sub_c1.setText(_translate("Golgi_details", "Subtract"))
        self.label_c2.setText(_translate("Golgi_details", "C2:"))
        self.btn_sub_c2.setText(_translate("Golgi_details", "Subtract"))
        self.label_c3.setText(_translate("Golgi_details", "C3:"))
        self.btn_sub_c3.setText(_translate("Golgi_details", "Subtract"))
        self.btn_check.setText(_translate("Golgi_details", "Check"))
        self.btn_export.setText(_translate("Golgi_details", "Export Data"))
        self.btn_save.setText(_translate("Golgi_details", "Save"))
