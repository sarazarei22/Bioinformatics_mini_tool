from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def train_disease_prediction_model():
  """Trains a Logistic Regression model to predict disease risk based

  on simulated clinical and genetic biomarker features, evaluating its
  performance.
  """
  # Generate synthetic clinical classification dataset
  X, y = make_classification(
      n_samples=500, n_features=6, n_informative=4, random_state=42
  )

  # Split dataset into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=42
  )

  # Scale features for optimal model performance
  scaler = StandardScaler()
  X_train_scaled = scaler.fit_transform(X_train)
  X_test_scaled = scaler.transform(X_test)

  # Initialize and train Logistic Regression model
  model = LogisticRegression(random_state=42)
  model.fit(X_train_scaled, y_train)

  # Predict and evaluate
  y_pred = model.predict(X_test_scaled)
  acc = accuracy_score(y_test, y_pred)

  print(f'Model Accuracy: {acc * 100:.2f}%')
  print('Classification Report:')
  print(classification_report(y_test, y_pred))

  return model


if __name__ == '__main__':
  print('Running Machine Learning Disease Risk Predictor...')
  train_disease_prediction_model()
