from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "User Service is running 🚀"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Nihed"},
        {"id": 2, "name": "DevSecOps User"}
    ]
