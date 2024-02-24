import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
from sklearn.preprocessing import StandardScaler
data = pd.read_csv('add.csv')

X = data[['x','y']]
y = data['sum']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33,random_state = 42)

model = LinearRegression()
model.fit(X_train,y_train)

pickle.dump(model, open('model.pkl',"wb"))
