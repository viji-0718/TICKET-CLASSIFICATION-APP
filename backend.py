from fastapi import FastAPI, UploadFile, File
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

app = FastAPI()
model = None

@app.post("/retrain")
async def retrain(file: UploadFile = File(...)):
    # Read uploaded CSV
    df = pd.read_csv(file.file)
    X = df["text"]
    y = df["label"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Simple model (example)
    global model
    model = LogisticRegression()
    model.fit(X_train.values.reshape(-1,1), y_train)

    return {"message": "Model retrained successfully!"}