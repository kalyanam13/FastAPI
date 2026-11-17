from fastapi import FastAPI

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

# About route
@app.get("/about")
def about():
    return {"message": "This is about page of the FastAPI application."}

# Users route

#@app.get("/users")
#def users():
#    return {
#        "users": ["Mohit", "John", "Alice", "Bob"]
#    }


# User detail route
@app.get("/users/{user_id}")
def user_detail(user_id:int):
    return {"user_id":user_id}



