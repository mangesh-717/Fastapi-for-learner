from fastapi import FastAPI

app=FastAPI()

data={
    1:{
        "name":"Mangesh Sathe",
        "email":"Mangeshsathe1353@gmail.com",
        "Phone":7218920354,
        "Location":"Bandra" }
}

@app.get("/{id}")
def inderx_get(id : int):
    return data[id]



from pydantic import BaseModel
# This library is used to define Post method

class Student():
    name:str
    email:str
    Phone:int
    Location:str

@app.post("/create-student{student_id}")
def create_instance(student_id : int, student : Student ):
    if student_id in data:
        return {"Errror":"student Exist"}
    data[student_id]=student
    return data[student_id]




from typing import Optional
# Updating instance
class Update_student(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    Phone : Optional[int] = None
    Location : Optional[str]=None

@app.put("/update_instance/{student_id}")
def update_student(student_id:int , update_student : Update_student):
    if student_id not in data:
        return {"Error":"Student record is not exist"}
    data[student_id]=update_student
    return data[student_id]




# Delete method 
@app.delete("/Delete_instance/{student_id}")
def selete_instance(student_id:int):
    if student_id not in data:
        return {"Error":"instance is not exist in database"}
    
    del data[student_id]
    return {"Messege":"Student deleted successfully"}