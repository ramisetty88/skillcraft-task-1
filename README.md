🏠 House Price Prediction using Linear Regression
📌 About the Project

This project predicts house prices using Linear Regression in Python.
The model uses:

Square foot area (sqft_living)

Number of bedrooms

Number of bathrooms

to predict the price of a house.

🛠 Tools Used

Python

Pandas

NumPy

Matplotlib

Scikit-learn

⚙️ How It Works

Load the dataset (kc_house_data.csv)

Select important columns

Split data into training and testing sets

Train Linear Regression model

Evaluate model using:

MSE (Mean Squared Error)

R² Score

Predict price for a new house

📊 Example Prediction

For a house with:

1800 sqft

3 bedrooms

2 bathrooms

The model predicts the estimated price.

▶ How to Run

Install required libraries:

pip install pandas numpy matplotlib seaborn scikit-learn

Place kc_house_data.csv in your folder.

Run the Python script.

📈 Output

Model coefficients

MSE and R² score

Scatter plot (Actual vs Predicted prices)

Predicted price for new input
