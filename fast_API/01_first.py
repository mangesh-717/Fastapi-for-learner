from fastapi import FastAPI

# Create a FastAPI application
app = FastAPI()

# Define a route at the root web address ("/")
@app.get("/")
def first_Api():
	return {"message": "Hello, FastAPI!"}
