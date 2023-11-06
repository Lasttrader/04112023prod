import sys

from PyQt6.QtWidgets import (QApplication, 
                             QLabel,
                             QWidget)

#app
app = QApplication([])

#create window
window = QWidget()
window.setWindowTitle('Моё первое приложение на PyQt')
window.setGeometry(200,200, 560,160)
window_message = QLabel('<h1> Hello World </h1>', parent = window)

window.show()

sys.exit(app.exec())