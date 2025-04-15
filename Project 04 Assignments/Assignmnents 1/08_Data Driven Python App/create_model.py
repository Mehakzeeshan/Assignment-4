import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Step 1: Prepare training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])  # target values follow y = 2x

# Step 2: Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Step 3: Save the model to a .pkl file
joblib.dump(model, 'linear_regression_model.pkl')

print("Model trained and saved successfully!")
