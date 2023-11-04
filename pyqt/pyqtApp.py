import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
print('import success')



#predict
X_scaled = [[ 0.82737724, -0.53037664,  0.43279337, -0.47367361, -0.50143844,  0.73769513,-1.44232155, -2.1037683,   0.58111394]]
predict = kNN.predict(X_scaled) #подаём уже отмасштабированные данные
if predict == 0:
    result = 'not survived'
else:
    result = 'survived'
print(f'Passanger is {result}')