from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QTextTableCell
import os
import re

#in ui method
self.fileDialogButton.clicked.connect(self.fileDialogHandler)
self.searchButton.clicked.connect(self.search)

#methods
def fileDialogHandler(self):
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.Directory)
    dialog.exec()
    self.label_4.setText(self.label_4.text() + dialog.selectedFiles()[0])
    self.label_4.adjustSize()

    def search(self):

        if os.path.isdir(self.filePath):
            print('searching a folder')
            # for every file in this folder:
            # check if file is a file and has the extension
            # if so, checkFile(file, regex)
            # add new row to table
        else:
            print('searching a file')

    def checkFile(self, path, regex):
        print('hello')