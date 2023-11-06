# import
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from flask import (Flask,
                   render_template,
                   jsonify,
                   request)

# load models
sex_LE = pickle.load(open('../models/tech_models/Sex_LE.pkl', 'rb'))
ticket_LE = pickle.load(open('../models/tech_models/Ticket_LE.pkl', 'rb'))
cabin_LE = pickle.load(open('../models/tech_models/Cabin_LE.pkl', 'rb'))
embarked_LE = pickle.load(open('../models/tech_models/Embarked_LE.pkl', 'rb'))
num_scaler = pickle.load(open('../models/tech_models/num_scaler.pkl', 'rb'))
kNN = pickle.load(open('../models/ml_models/kNN.pkl', 'rb'))
print('models loaded success')

# app
app = Flask(__name__)

# route pages


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('main.html')
    if request.method == 'POST':
        # get data from html form
        Pclass = float(request.form['Pclass'])
        Age = float(request.form['Age'])
        SibSp = float(request.form['SibSp'])
        Parch = float(request.form['Parch'])
        Fare = float(request.form['Fare'])
        Sex = str(request.form['Sex'])
        Ticket = str(request.form['Ticket'])
        Cabin = str(request.form['Cabin'])
        Embarked = str(request.form['Embarked'])

        # Получаем список признаков с формы
        x_list = [Pclass,
                  Age,
                  SibSp,
                  Parch,
                  Fare,
                  Sex,
                  Ticket,
                  Cabin,
                  Embarked]
        # наши категориальные признаки, которые получили в форме
        x_cat_list = x_list[5:]
        le_list = [sex_LE, ticket_LE, cabin_LE, embarked_LE]
        x_cat_le = []  # пустой список под закодированые признаки
        for i in range(len(x_cat_list)):
            x_cat = le_list[i].transform([x_cat_list[i]])[0]
            # print(x_cat)
            x_cat_le.append(x_cat)
            print('x_le: ', x_cat_le)
        X = []
        x_num = x_list[:5]
        X.extend(x_num)
        X.extend(x_cat_le)  # добавляем УЖЕ закодированные признаки
        X_scaled = num_scaler.transform([X])
        print('X_scaled: ', X_scaled)
        # predict
        # X_scaled = [[ 0.82737724, -0.53037664,  0.43279337, -0.47367361, -0.50143844,  0.73769513,-1.44232155, -2.1037683,   0.58111394]]
        predict = kNN.predict(X_scaled)  # подаём уже отмасштабированные данные
        # print(predict)
        return render_template('main.html', result=predict)

# API


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
