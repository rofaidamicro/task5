import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Load the SDN traffic CSV dataset
file_path = 'C:/Users/nezza/Downloads/SDN_traffic.csv'  # Update with your file path
data = pd.read_csv(file_path)

# Drop columns that are not useful for model training (e.g., non-numeric columns)
X = data.drop(columns=['id_flow', 'nw_src', 'nw_dst', 'category'])  # Drop non-numeric or identifier columns
y = data['category'].astype('category').cat.codes  # Convert the 'category' column to numeric labels

# Handle missing data (if any) by filling with mean
X = X.fillna(X.mean())

# Remove rows where 'forward_bps_var' has invalid (non-numeric) values
X['forward_bps_var'] = pd.to_numeric(X['forward_bps_var'], errors='coerce')
valid_rows = X['forward_bps_var'].notnull()
X_cleaned = X[valid_rows]
y_cleaned = y[valid_rows]

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_cleaned, y_cleaned, test_size=0.2, random_state=42)

# Initialize and train Decision Tree classifiers using ID3 (using 'entropy') and CART (using 'gini')
id3_model = DecisionTreeClassifier(criterion='entropy', random_state=42)
cart_model = DecisionTreeClassifier(criterion='gini', random_state=42)

# Train the models
id3_model.fit(X_train, y_train)
cart_model.fit(X_train, y_train)

# Predict using both models
id3_predictions = id3_model.predict(X_test)
cart_predictions = cart_model.predict(X_test)

# Get classification metrics for both models
id3_metrics = classification_report(y_test, id3_predictions)
cart_metrics = classification_report(y_test, cart_predictions)

# Display the classification reports
print("ID3 (Entropy) Classification Report:\n", id3_metrics)
print("CART (Gini) Classification Report:\n", cart_metrics)
