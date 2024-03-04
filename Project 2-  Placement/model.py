import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
from sklearn.preprocessing import StandardScaler
data = pd.read_csv('collegePlace.csv')
data['Gender'] = data['Gender'].map({'Male':1,'Female':0})

Stream_mapping = {
    'Electronics And Communication': 0,
    'Computer Science': 1,
    'Mechanical': 2,
    'Civil': 3,
    'Information Technology': 4,
    'Electrical': 5
}

data['Stream'] = data['Stream'].map(Stream_mapping)

X = data.drop('PlacedOrNot', axis=1)
print(X)
y = data['PlacedOrNot']


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,y_train)

pickle.dump(lr, open('model2.pkl', 'wb'))
model = pickle.load(open('model2.pkl', 'rb'))