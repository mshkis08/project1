from PyQt6.QtCore import Qt, QTime, QTimer, QUrl
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtMultimedia import QSoundEffect
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
    QAbstractSpinBox,
)
import os
import sys
import re

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()


        self.setWindowTitle('таймер')
        self.setFixedSize(400,300)


        id = QFontDatabase.addApplicationFont(resource_path("fonts/Inter-VariableFont_opsz,wght.ttf"))
        families = QFontDatabase.applicationFontFamilies(id)
        font_inter = QFont(families[0])
        id = QFontDatabase.addApplicationFont(resource_path("fonts/Onest-VariableFont_wght.ttf"))
        families = QFontDatabase.applicationFontFamilies(id)
        font_onest = QFont(families[0])


        self.title_1 = 'Запустить'
        self.title_2 = 'Очистить'
        self.cur = '00:00:00'


        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile(resource_path('sound/s1.wav')))


        self.button1 = QPushButton(self.title_1)
        self.button1.setFixedHeight(50)
        self.button1.setObjectName('button1')
        self.button1.setAutoDefault(True)
        self.button1.setFont(font_inter)


        self.button2 = QPushButton(self.title_2)
        self.button2.setFixedHeight(50)
        self.button2.setObjectName('button2')
        self.button2.setAutoDefault(True)
        self.button2.setFont(font_inter)
        self.button2.setEnabled(False)


        self.timer = QTimeEdit()    
        self.timer.setFixedHeight(30)
        self.timer.setDisplayFormat('hh:mm:ss')
        self.timer.setObjectName('timer')
        self.timer.setFont(font_inter)


        self.tru_timer = QTimer(self)
        

        self.label = QLabel('0')
        self.label.setObjectName('label')
        self.label.setFont(font_onest)


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


        self.container = QWidget()
        self.container.setLayout(layout)
        self.container.setObjectName('container')


        self.setCentralWidget(self.container)


    def time_changed(self, x):
        self.cur = str(self.timer.time().toPyTime())

        for i in range(len(self.cur)):
            if self.cur[i] == '0' or self.cur[i] == ':':
                pass
            else:
                break
        self.mas = self.cur[i:]

        self.label.setText(self.mas)


    def but1_clicked(self):
        self.button2.setEnabled(True)
        if self.title_1 == 'Запустить' or self.title_1 == 'Продолжить':
            self.title_1 = 'Остановить'
            self.button1.setText(self.title_1)
            self.button1.clearFocus()

            self.timer.setStyleSheet("background-color: transparent; color: transparent; border: 0px")
            self.timer.setEnabled(False)

            self.tru_timer.start(1000)

        else:
            self.title_1 = 'Продолжить'
            self.button1.setText(self.title_1)
            self.button1.clearFocus()

            self.tru_timer.stop()


    def but2_clicked(self):
        self.title_1 = 'Запустить'
        self.button1.setText(self.title_1)
        self.button1.setEnabled(True)
            

        self.timer.setVisible(True)
        self.timer.setTime(QTime(0, 0, 0))
        self.timer.setStyleSheet("background-color: #FFF; color: #088; border: 1px solid #EAEAEA")
        self.timer.setEnabled(True)


        self.label.setObjectName('label')

        image_path = resource_path("pics/man.jpg").replace("\\", "/")
        self.container.setStyleSheet(f"#container {{background-image: url('{image_path}');}}")


        self.button2.setEnabled(False)


        self.tru_timer.stop()


        self.sound.stop()


    def start_count(self):
        self.el1 = int(self.cur[:2])
        self.el2 = int(self.cur[3:5])
        self.el3 = int(self.cur[6:])


        if self.el3 != 0:
            self.el3 -= 1
        elif self.el2 != 0:
            self.el2 -= 1
            self.el3 = 59
        elif self.el1 != 0:
            self.el1 -= 1
            self.el2 = 59
            self.el3 = 59
        else:
            self.tru_timer.stop()

            image_path = resource_path("pics/man1.jpg").replace("\\", "/")
            self.container.setStyleSheet(f"#container {{background-image: url('{image_path}');}}")

            self.sound.play()

            self.title_1 = 'Запустить'
            self.button1.setText(self.title_1)
            self.button1.setEnabled(False)


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


        for i in range(len(self.cur)):
            if self.cur[i] == '0' or self.cur[i] == ':':
                pass
            else:
                break
        self.mas = self.cur[i:]
            

        self.label.setText(self.mas)

    

app = QApplication([])

with open(resource_path('style.css')) as fout:
    css = fout.read()
    
    def rewrite_url(match):
        rel_path = match.group(1).strip('\'"') 
        abs_path = resource_path(rel_path).replace("\\", "/")  
        return f'url("{abs_path}")'

    css = re.sub(r'url\((.*?)\)', rewrite_url, css)
    app.setStyleSheet(css)

window = MainWindow()
window.show()

app.exec()