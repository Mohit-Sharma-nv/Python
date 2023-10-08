import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the dataset
df = pd.read_csv('telecom_customer_churn.csv')

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('Churn', axis=1), df['Churn'], test_size=0.25, random_state=42)

# Create a logistic regression model
model = LogisticRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict_proba(X_test)[:, 1]

# Evaluate the model performance
accuracy = model.score(X_test, y_test)

# Print the accuracy
print('Accuracy:', accuracy)

# Analyze the trends in customer churn
# ...
