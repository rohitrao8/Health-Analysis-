import pandas as pd
import pickle
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("patient_data.csv")
X = df[["Age", "BP", "Sugar Level", "Cholesterol"]]
y = df["Hemoglobin"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

joblib.dump(model, "model.joblib")
