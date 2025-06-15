import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Step 1: Create CSV if not exists
if not os.path.exists("student_data.csv"):
    data = {
        "Hours_Studied": np.random.randint(1, 10, 100),
        "Attendance": np.random.randint(60, 100, 100),
        "Previous_Grades": np.random.randint(40, 100, 100)
    }

    data["Final_Result"] = [
        1 if (h > 5 and a > 75 and g > 60) else 0
        for h, a, g in zip(data["Hours_Studied"], data["Attendance"], data["Previous_Grades"])
    ]

    df = pd.DataFrame(data)
    df.to_csv("student_data.csv", index=False)
    print("✅ student_data.csv created.")
else:
    print("✅ student_data.csv already exists.")

# Step 2: Train model
df = pd.read_csv("student_data.csv")
X = df[["Hours_Studied", "Attendance", "Previous_Grades"]]
y = df["Final_Result"]

model = LogisticRegression()
model.fit(X, y)

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model trained and saved as model.pkl")
