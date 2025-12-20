# ---------------------------------------
# House Price Prediction with User Input
# Author: Fresher ML Project
# Language: Python
# ---------------------------------------

# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# -------------------------------
# Step 1: Create Dataset
# -------------------------------
data = {
    'Area': [800, 900, 1000, 1100, 1200, 1300, 1500, 1800, 2000, 2200],
    'Bedrooms': [1, 2, 2, 2, 3, 3, 3, 4, 4, 5],
    'Bathrooms': [1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
    'Price': [40, 45, 55, 60, 70, 75, 85, 100, 120, 140]
}

df = pd.DataFrame(data)

# -------------------------------
# Step 2: Features & Target
# -------------------------------
X = df[['Area', 'Bedrooms', 'Bathrooms']]
y = df['Price']

# -------------------------------
# Step 3: Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Step 4: Train Model
# -------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# Step 5: Model Evaluation
# -------------------------------
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance")
print("------------------")
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# -------------------------------
# Step 6: USER INPUT
# -------------------------------
print("\nEnter House Details")

area = float(input("Enter Area (in sq.ft): "))
bedrooms = int(input("Enter Number of Bedrooms: "))
bathrooms = int(input("Enter Number of Bathrooms: "))

# Convert user input to array
user_house = np.array([[area, bedrooms, bathrooms]])

# -------------------------------
# Step 7: Predict Price
# -------------------------------
predicted_price = model.predict(user_house)

print("\nHouse Details Entered:")
print("Area:", area)
print("Bedrooms:", bedrooms)
print("Bathrooms:", bathrooms)

print("\nPredicted House Price:", round(predicted_price[0], 2), "Lakhs")

# -------------------------------
# End of Program
# -------------------------------
