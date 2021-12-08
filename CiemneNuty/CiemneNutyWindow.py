import sys
from CiemneNuty import Ui_CiemneNuty
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

class NutyWindow(QtWidgets.QMainWindow, Ui_CiemneNuty):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.New.triggered.connect(self.fileNew)
        self.actionOpen.triggered.connect(self.file_open)
                
        self.show()

    def fileNew(self):
        self.textEdit.clear()

#    def openFile(self):
#       filename = QFileDialog().getOpenFileName(self, 'Открыть файл', '/home')
#
#        if filename[0]:
#            f = open(filename[0], 'r')
#
#
#            with f:
#                data = f.read()
#
#                self.textEdit.setText(data)

    def file_open(self):
      path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "HTML documents (*.html);Text documents (*.txt);All files (*.*)")

      try:
          with open(path, 'rU') as f:
              text = f.read()

      except Exception as e:
          self.dialog_critical(str(e))

      else:
          self.path = path
          # Qt will automatically try and guess the format as txt/html
          self.editor.setText(text)
          self.update_title()
     
