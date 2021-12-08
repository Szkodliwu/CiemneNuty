import sys
from PyQt5.QtWidgets import QApplication
from CiemneNutyWindow import NutyWindow


app = QApplication(sys.argv)
nutyCiemne = NutyWindow()
sys.exit(app.exec())

