import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class HousePriceModel:
    def __init__(self):
        self.model = None

    def load_data(self, filepath):
        return pd.read_csv(filepath)

    def preprocess_data(self, data):
        # Assuming no missing values for simplicity
        return data

    def train(self, data):
        X = data[['sqft', 'bedrooms', 'bathrooms']]
        y = data['price']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f'Mean Squared Error: {mse}')

    def predict(self, data):
        if self.model is None:
            raise ValueError("Model has not been trained yet.")
        X = data[['sqft', 'bedrooms', 'bathrooms']]
        return self.model.predict(X)
