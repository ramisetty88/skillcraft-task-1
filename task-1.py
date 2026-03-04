import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
df = pd.read_csv(r"C:\Users\welcome\Downloads\kc_house_data.csv")
print("Dataset shape:", df.shape)
print(df.head())
df = df[["sqft_living", "bedrooms", "bathrooms", "price"]]
print("\nSelected columns:")
print(df.head())
print("\nMissing values:\n", df.isnull().sum())
X = df[["sqft_living", "bedrooms", "bathrooms"]]
y = df["price"]
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.2, random_state=42
)
print("\nTrain set size:", X_train.shape)
print("Test set size:", X_test.shape)
model = LinearRegression()
model.fit(X_train, y_train)
print("\nModel coefficients:")
print("Intercept:", model.intercept_)
print("sqft_living coef:", model.coef_[0])
print("bedrooms coef:", model.coef_[1])
print("bathrooms coef:", model.coef_[2])
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\nModel performance on test set:")
print("MSE:", mse)
print("R² score:", r2)
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.show()
new_house = [[1800, 3, 2]]
predicted_price = model.predict(new_house)
print("\nPredicted price for house", new_house, "is", predicted_price[0])
