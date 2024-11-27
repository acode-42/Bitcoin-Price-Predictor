
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


data = pd.read_csv("BTC-USD.csv")
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

data['Previous Close'] = data['Close'].shift(1)
data.dropna(inplace=True)


X = data[['Previous Close']]
y = data['Close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)


with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Model trained and saved!")
