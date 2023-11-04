import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
print('import success')

#load models
sex_LE = pickle.load(open('../models/tech_models/Sex_LE.pkl', 'rb'))
ticket_LE = pickle.load(open('../models/tech_models/Ticket_LE.pkl', 'rb'))
cabin_LE = pickle.load(open('../models/tech_models/Cabin_LE.pkl', 'rb'))
embarked_LE = pickle.load(open('../models/tech_models/Embarked_LE.pkl', 'rb'))
num_scaler = pickle.load(open('../models/tech_models/num_scaler.pkl', 'rb'))
kNN = pickle.load(open('../models/ml_models/kNN.pkl', 'rb'))
print('models loaded')

x_list = ['Pclass',
          'Age',	
          'SibSp',	
          'Parch',	
          'Fare',	
          'Sex',	
          'Ticket',	
          'Cabin',	
          'Embarked']

'''
Pclass	Sex	    Age	    SibSp	Parch	Ticket	    Fare	Cabin	Embarked									
3		male	22.0	1	    0	    113803	    7.2500	C123	    S
'''

#input num
Pclass = float(input('Pclass: '))
Age = float(input('Age: '))	
SibSp = float(input('SibSp: '))	
Parch = float(input('Parch: '))	
Fare = float(input('Fare: '))
#input cat
sex = input('input_sex: ')
ticket = input('input_ticket: ')
cabin = input('input_cabin: ')
embarked = input('input_embarked: ')
#le_transform
x_cat_list = [sex, ticket, cabin, embarked] 
le_list = [sex_LE, ticket_LE, cabin_LE, embarked_LE]
x_cat_le =[] #пустой список под закодированые признаки
for i in range(len(x_cat_list)):
    x_cat = le_list[i].transform([x_cat_list[i]])[0]
    print(x_cat)
    x_cat_le.append(x_cat)
#print('x_le: ', x_cat_le)
#create Х for predict
X = []
x_num = [Pclass, Age, SibSp, Parch, Fare]
X.extend(x_num)
X.extend(x_cat_le) #добавляем УЖЕ закодированные признаки 
X_scaled = num_scaler.transform([X])
#print('X_scaled: ', X_scaled)

#predict
predict = kNN.predict(X_scaled) #подаём уже отмасштабированные данные
if predict == 0:
    result = 'not survived'
else:
    result = 'survived'
print(f'Passanger is {result}')
