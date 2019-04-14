#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog, QMessageBox
from GitCloneUi import *
import git


class MyWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.cwd = os.getcwd()
        self.pushButton_select.clicked.connect(self.selectDir)
        self.pushButton_clone.clicked.connect(self.startClone)

    def selectDir(self):
        dirUrl = QFileDialog.getExistingDirectory(self, "选取文件夹", self.cwd)
        self.lineEdit_dir.setText(dirUrl)

    def startClone(self):
        cloneUrl = self.lineEdit_url.text()
        storeDir = self.lineEdit_dir.text()
        if cloneUrl[-3:] != "git":
            QMessageBox.information(self, "警告", "请输入有效的克隆地址", QMessageBox.Ok)
            return
        if not os.path.exists(storeDir):
            QMessageBox.information(self, "警告", "请输入有效的存储位置", QMessageBox.Ok)
            return
        git.Git(storeDir).clone(cloneUrl)
        QMessageBox.information(self, "消息", "克隆成功！", QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
