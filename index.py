from PyQt6.QtCore import Qt, QTime, QTimer
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('таймер')
        self.setFixedSize(400,300)


        id = QFontDatabase.addApplicationFont("fonts/Inter-VariableFont_opsz,wght.ttf")
        families = QFontDatabase.applicationFontFamilies(id)
        font_inter = QFont(families[0])
        id = QFontDatabase.addApplicationFont("fonts/Climate_Crisis/ClimateCrisis-Regular-VariableFont_YEAR.ttf")
        families = QFontDatabase.applicationFontFamilies(id)
        font_climate = QFont(families[0])


        self.title_1 = 'Запустить'
        self.title_2 = 'restart'
        self.cur = '00:00:00'


        self.button1 = QPushButton(self.title_1)
        self.button1.setFixedHeight(50)
        self.button1.setObjectName('button1')
        self.button1.setAutoDefault(True)
        self.button1.setFont(font_inter)


        self.button2 = QPushButton(self.title_2)
        self.button2.setFixedHeight(50)
        self.button2.setObjectName('button2')
        self.button2.setVisible(False)
        self.button2.setEnabled(False)
        self.button2.setAutoDefault(False)
        self.button2.setFont(font_inter)


        self.timer = QTimeEdit()    
        self.timer.setFixedHeight(30)
        self.timer.setDisplayFormat('hh:mm:ss')
        self.timer.setObjectName('timer')
        self.timer.setFont(font_inter)


        self.tru_timer = QTimer(self)
        

        self.label = QLabel('00:00:00')
        self.label.setObjectName('label')
        self.label.setFont(font_climate)


        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignHCenter) 
        layout.addWidget(self.timer)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.setSpacing(10)
        layout.setContentsMargins(20,20,20,20)


        self.timer.timeChanged.connect(self.time_changed)
        self.button1.clicked.connect(self.but1_clicked)
        self.button2.clicked.connect(self.but2_clicked)
        self.tru_timer.timeout.connect(self.start_count)


        container = QWidget()
        container.setLayout(layout)
        container.setObjectName('container')


        self.setCentralWidget(container)


    def time_changed(self, x):
        self.cur = str(self.timer.time().toPyTime())
        self.label.setText(self.cur)


    def but1_clicked(self):
        if self.title_1 == 'Запустить':
            self.title_1 = 'stop'
            self.button1.setText(self.title_1)

            self.timer.setVisible(False)

            self.tru_timer.start(1000)

        else:
            self.title_1 = 'Запустить'
            self.button1.setText(self.title_1)

            self.timer.setVisible(True)

            self.tru_timer.stop()


    def but2_clicked(self):
        self.title_1 = 'Запустить'
        self.button1.setText(self.title_1)
        self.button1.setVisible(True)
        self.button1.setEnabled(True)
        self.button1.setAutoDefault(True)
            
        self.button2.setVisible(False)
        self.button2.setEnabled(False)
        self.button2.setAutoDefault(False)

        self.timer.setVisible(True)
        self.timer.setTime(QTime(0, 0, 0))

        self.tru_timer.stop()


    def start_count(self):
        self.el1 = int(self.cur[:2])
        self.el2 = int(self.cur[3:5])
        self.el3 = int(self.cur[6:])


        if self.el3 != 0:
            self.el3 -= 1
        elif self.el2 != 0:
            self.el2 -= 1
            if self.el2 == 0:
                self.el3 = 59
        elif self.el1 != 0:
            self.el1 -= 1
            if self.el1 == 0:
                self.el2 = 59
        else:
            self.tru_timer.stop()

            self.button1.setVisible(False)
            self.button1.setEnabled(False)
            self.title_1 = 'Запустить'
            self.button1.setText(self.title_1)
            self.button1.setAutoDefault(False)

            self.button2.setVisible(True)
            self.button2.setEnabled(True)
            self.button2.setAutoDefault(True)

            self.button2.setFocus()


        self.cur1 = str(self.el1)
        self.cur2 = str(self.el2)
        self.cur3 = str(self.el3)


        if len(str(self.el1)) == 1:
            self.cur1 = '0' + str(self.el1)
        if len(str(self.el2)) == 1:
            self.cur2 = '0' + str(self.el2)
        if len(str(self.el3)) == 1:
            self.cur3 = '0' + str(self.el3)
        else:
            pass
    

        self.cur = self.cur1 + ':' + self.cur2 + ':' + self.cur3


        self.label.setText(self.cur)

    


app = QApplication([])

with open('style.css') as fout:
    app.setStyleSheet(fout.read())

window = MainWindow()
window.show()

app.exec()