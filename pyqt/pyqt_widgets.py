import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import(QApplication,
                            QCheckBox,
                            QComboBox,
                            QDateEdit,
                            QDateTimeEdit,
                            QDial,
                            QMainWindow,
                            QProgressBar,
                            QPushButton,
                            QRadioButton,
                            QSlider,
                            QSpinBox,
                            QTimeEdit,
                            QVBoxLayout,
                            QWidget,
                            QDoubleSpinBox,
                            QLabel)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Demo window')

        layout = QVBoxLayout()
        widgets = (QCheckBox,
                   QComboBox,
                   QDateEdit,
                   QDateTimeEdit,
                   QTimeEdit,
                   QDial,
                   QDoubleSpinBox,
                   QSpinBox,
                   QLabel,
                   QSlider,
                   QRadioButton,
                   QProgressBar,
                   QPushButton
                   )
        for i in widgets:
            layout.addWidget(i())
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = Window()
window.show()

app.exec()