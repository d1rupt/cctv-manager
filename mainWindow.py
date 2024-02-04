from PyQt6.QtWidgets import *
from newCamWindow import *
from cameraSettings import *

app = QApplication([])

#any settings changed - get written to a file
#the MainWindow then accesses this file

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(720,1000)

        self.button_is_checked = False
        self.setWindowTitle("CCTV")

        menu = QMenuBar(self)
        self.setMenuBar(menu)
        settings = QMenu("Settings",self)
        new = settings.addMenu("Add camera")

        change = settings.addMenu("Change camera")
        # TODO: read from settings file and display them under change addaction
        ip = new.addAction("IP")
        usb = new.addAction("USB")
        ip.triggered.connect(self.open_new_cam_ip)
        usb.triggered.connect(self.open_new_cap_usb)

        menu.addMenu(settings)
        layout = QGridLayout()

        #layout.addWidget(self.button,0,0)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def open_new_cam_ip(self):
        self.newcam = newCamWindow("IP")
        self.newcam.show()
    def open_new_cap_usb(self):
        self.newcam = newCamWindow("USB")
        self.newcam.show()

    def open_camera_sett(self, id):
        self.camerasett = cameraSettings(id)
        self.camerasett.show()



window = MainWindow()


window.show()
app.exec()