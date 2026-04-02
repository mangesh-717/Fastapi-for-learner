from fastapi import FastAPI, Depends, HTTPException
from auth import generate_token, get_current_user 
from models import User, LoginResponse, Profile

app = FastAPI()

# Dummy user data for demonstration purposes
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "password": "secret",
        "email": "johndoe@example.com"
    }
}

@app.post("/register")
async def register(user: User):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    
    fake_users_db[user.username] = {"username": user.username, "password": user.password, "email": ""}
    return {"message": "User registered successfully"}

@app.post("/token", response_model=LoginResponse)
async def login(user: User):
    db_user = fake_users_db.get(user.username)
    if db_user is None or db_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = generate_token({"username": user.username})
    return LoginResponse(access_token=access_token)

@app.get("/profile", response_model=Profile)
async def access_profile(current_user:Profile = Depends(get_current_user)):
    db_user = fake_users_db.get(current_user.username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return Profile(username=db_user["username"], email=db_user["email"] )

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI!"}
