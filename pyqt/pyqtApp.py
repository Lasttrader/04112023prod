import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier

import sys
from PyQt6.QtWidgets import (QApplication,
                             QDialog,
                             QDialogButtonBox,
                             QFormLayout,
                             QLineEdit,
                             QVBoxLayout,
                             QGroupBox,
                             QLabel,
                             QMessageBox)
print('import success')

#load models
sex_LE = pickle.load(open('../models/tech_models/Sex_LE.pkl', 'rb'))
ticket_LE = pickle.load(open('../models/tech_models/Ticket_LE.pkl', 'rb'))
cabin_LE = pickle.load(open('../models/tech_models/Cabin_LE.pkl', 'rb'))
embarked_LE = pickle.load(open('../models/tech_models/Embarked_LE.pkl', 'rb'))
num_scaler = pickle.load(open('../models/tech_models/num_scaler.pkl', 'rb'))
kNN = pickle.load(open('../models/ml_models/kNN.pkl', 'rb'))
print('models loaded success')

#class Dialog
class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox() #создать
        self.x_for_predict = {}
        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok |
                                     QDialogButtonBox.StandardButton.Cancel)
        buttonBox.accepted.connect(self.my_predict) #самописная реакция на кнопку
        buttonBox.rejected.connect(self.reject) #выход из приложения
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle('Titanic passenger predict')

    def createFormGroupBox(self):
        '''
        поля для ввода
        '''
        self.formGroupBox = QGroupBox('Input passanger data')
        self.layout = QFormLayout()

        self.Pclass =QLineEdit()
        self.Pclass.textEdited.connect(self.create_x_for_predict(1))
        self.layout.addRow(QLabel('Pclass'), self.Pclass)

        self.Age =QLineEdit()
        self.Age.textEdited.connect(self.create_x_for_predict(2))
        self.layout.addRow(QLabel('Age'), self.Age)

        self.SibSp =QLineEdit()
        self.SibSp.textEdited.connect(self.create_x_for_predict(3))
        self.layout.addRow(QLabel('SibSp'), self.SibSp)

        self.Parch =QLineEdit()
        self.Parch.textEdited.connect(self.create_x_for_predict(4))
        self.layout.addRow(QLabel('Parch'), self.Parch)

        self.Fare =QLineEdit()
        self.Fare.textEdited.connect(self.create_x_for_predict(5))
        self.layout.addRow(QLabel('Fare'), self.Fare)

        self.sex =QLineEdit()
        self.sex.textEdited.connect(self.create_x_for_predict(6))
        self.layout.addRow(QLabel('sex'), self.sex)

        self.ticket =QLineEdit()
        self.ticket.textEdited.connect(self.create_x_for_predict(7))
        self.layout.addRow(QLabel('ticket'), self.ticket)

        self.embarked =QLineEdit()
        self.embarked.textEdited.connect(self.create_x_for_predict(8))
        self.layout.addRow(QLabel('embarked'), self.embarked)

        self.formGroupBox.setLayout(self.layout)

    
    def create_x_for_predict(self,x):
        '''
        функция которая собирает Х для прогноза
        '''
        def savedX(text):
            self.x_for_predict[x] = text
        return savedX

    def my_predict(self):
        '''
        функция для ML
        '''
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Your predict")
        
        #predict
        X_scaled = [[ 0.82737724, -0.53037664,  0.43279337, -0.47367361, -0.50143844,  0.73769513,-1.44232155, -2.1037683,   0.58111394]]
        predict = kNN.predict(X_scaled) #подаём уже отмасштабированные данные
        if predict == 0:
            result = 'not survived'
        else:
            result = 'survived'
        dlg.setText(f'Passanger is {result}')
        dlg.exec()


#запуск и закрытие приложения
app = QApplication(sys.argv)
dialog = Dialog()
dialog.exec()
#print(dialog.x_for_predict{})
app.exit()