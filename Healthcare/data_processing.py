import pandas as pd
import random
import faker
import pickle
import joblib

fake = faker.Faker()
num_patients = 10000
data = []

for _ in range(num_patients):
    data.append({
        "Name": fake.name(),
        "Age": random.randint(20, 80),
        "BP": random.randint(90, 180),
        "Sugar Level": round(random.uniform(70, 200), 1),
        "Cholesterol": round(random.uniform(100, 300), 1),
        "Hemoglobin": round(random.uniform(10, 18), 1)
    })

df = pd.DataFrame(data)
df.to_csv("", index=False)

with open("patient_data.pkl", "wb") as f:
    pickle.dump(df, f)

joblib.dump(df, "patient_data.joblib")
