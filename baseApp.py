import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
print('import success')

#load models
cabin_LE = pickle.load(open('../models/tech_models/Cabin_LE.pkl', 'rb'))
embarked_LE = pickle.load(open('../models/tech_models/Embarked_LE.pkl', 'rb'))
sex_LE = pickle.load(open('../models/tech_models/Sex_LE.pkl', 'rb'))
ticket_LE = pickle.load(open('../models/tech_models/Ticket_LE.pkl', 'rb'))
num_scaler = pickle.load(open('../models/tech_models/num_scaler.pkl', 'rb'))
print('models loaded')


