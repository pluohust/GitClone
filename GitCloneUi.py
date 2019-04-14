# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'git-clone.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(803, 193)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_url = QtWidgets.QLineEdit(Form)
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_url)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_dir = QtWidgets.QLineEdit(Form)
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dir)
        self.pushButton_select = QtWidgets.QPushButton(Form)
        self.pushButton_select.setObjectName("pushButton_select")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_select)
        self.pushButton_clone = QtWidgets.QPushButton(Form)
        self.pushButton_clone.setObjectName("pushButton_clone")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_clone)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Git克隆器"))
        self.label.setText(_translate("Form", "克隆地址："))
        self.label_2.setText(_translate("Form", "存储地址："))
        self.pushButton_select.setText(_translate("Form", "选择路径"))
        self.pushButton_clone.setText(_translate("Form", "开始克隆"))


