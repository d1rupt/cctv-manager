from PyQt6.QtWidgets import *
from detectCameras import list_cameras_ids

class newCamWindow(QMainWindow):
    def __init__(self, type):
        super().__init__()
        self.setWindowTitle(f"New camera - {type}")
        self.setMinimumSize(500, 500)
        self.layout = QGridLayout()
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)


        if type == "IP":
            self.label0 = QLabel("Connection protocol")
            self.protocol = QComboBox()
            self.protocol.addItem("HTTP")
            self.protocol.addItem("RSTP")

            self.label1 = QLabel("Url \n <ip>:<port>/<uri>")
            self.ip = QLineEdit()
            self.ip.textEdited.connect(self.ip_check)

            self.label2 = QLabel("Requires authorization")
            self.hascreds = QCheckBox()
            self.hascreds.stateChanged.connect(self.show_creds_fields)

            self.label3 = QLabel("Username")
            self.user = QLineEdit()


            self.label4 = QLabel("Password")
            self.passw = QLineEdit()
            self.passw.setEchoMode(QLineEdit.EchoMode.Password)


            self.list_creds = [self.label3, self.user, self.label4, self.passw]

            self.hide_show(self.list_creds, False)

            self.layout.addWidget(self.label0,0,0)
            self.layout.addWidget(self.protocol,0,1)
            self.layout.addWidget(self.label1,1,0)
            self.layout.addWidget(self.ip,1,1)
            self.layout.addWidget(self.label2,2,0)
            self.layout.addWidget(self.hascreds, 2,1)
            self.layout.addWidget(self.label3, 3,0)
            self.layout.addWidget(self.user, 3,1)
            self.layout.addWidget(self.label4,4,0)
            self.layout.addWidget(self.passw,4,1)

        else:
            self.label5 = QLabel("Available cameras")
            ids = list_cameras_ids()
            self.idchoice = QComboBox()
            for id in ids:
                self.idchoice.addItem(str(id))

            self.layout.addWidget(self.label5,0,0)
            self.layout.addWidget(self.idchoice,0,1)


        self.label6 = QLabel("Movement detection")
        self.movdetect = QCheckBox()
        self.movdetect.stateChanged.connect(self.show_movdetect_options)

        self.layout.addWidget(self.label6,20,0)
        self.layout.addWidget(self.movdetect,20,1)

        self.label7 = QLabel("Absolute path to video storage")
        self.path = QLineEdit()

        self.label8 = QLabel("Notify using pop-ups when motion is detected")
        self.popup = QCheckBox()

        self.layout.addWidget(self.label7, 21,0)
        self.layout.addWidget(self.path,21,1)
        self.layout.addWidget(self.label8,22,0)
        self.layout.addWidget(self.popup,22,1)

        self.list_movdetect = [self.label7, self.path, self.label8, self.popup]
        self.hide_show(self.list_movdetect, False)

        self.apply = QPushButton("Apply")
        self.apply.clicked.connect(self.apply_close)
        self.layout.addWidget(self.apply,30,1)

    def apply_close(self):
        #write to a file configurations
        self.close()

    def ip_check(self,ip):
        #TODO: check ip for correctness
        pass

    def show_creds_fields(self):
        self.hide_show(self.list_creds, self.hascreds.isChecked())

    def hide_show(self,list, show):
        if show == True:
            for i in list:
                i.show()

        else:
            for i in list:
                i.hide()

    def show_movdetect_options(self):
        self.hide_show(self.list_movdetect, self.movdetect.isChecked())