import sklearn
from sklearn.linear_model import LinearRegression

# Assuming 'Gross' is a column in the 'salaries' DataFrame
model = LinearRegression()

# Select features (assuming 'Department' is a string column)
features = salaries[["Gender", "Age", "Department_Code", "Years_exp", "Tenure (months)"]]

# Drop 'Department' (if it's a string column) and 'Gross' from features
features = features.drop(["Department", "Gross"], axis=1)  # Corrected typo

# Target variable (assuming 'Gross' is the column for salary)
target = salaries["Gross"]

model.fit(features, target)
r_squared = model.score(features, target)  # Using r_squared for model evaluation
print("R-squared:", r_squared)  # Print the R-squared score

# Predict on new data
predictions = model.predict(new_data)

# Get regression coefficients (consider using feature names instead of indices)
coefficients = model.coef_
print("Coefficients:", coefficients)

# Get intercept
intercept = model.intercept_
print("Intercept:", intercept)
