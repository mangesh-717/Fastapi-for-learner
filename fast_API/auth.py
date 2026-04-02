from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

# App initialization
app = FastAPI()

# Secret key for JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECONDS = 200

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# In-memory user data (replace with database in production)
fake_users_db = {
    "user1": {
        "username": "user1",
        "password": "password1",  # Store hashed passwords in production
    }
}

# Helper function to verify user credentials
def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or user["password"] != password:
        return False
    return user

# Create access token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Dependency to verify token
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Token endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Multiple HTTP methods with token authentication
@app.get("/items")
async def read_items(current_user: str = Depends(get_current_user)):
    return {"message": f"GET request successful. User: {current_user}"}

@app.post("/items")
async def create_item(item: dict, current_user: str = Depends(get_current_user)):
    return {"message": f"POST request successful. User: {current_user}", "item": item}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict, current_user: str = Depends(get_current_user)):
    return {"message": f"PUT request successful. User: {current_user}", "item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, current_user: str = Depends(get_current_user)):
    return {"message": f"DELETE request successful. User: {current_user}", "item_id": item_id}


