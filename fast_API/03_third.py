# Qury parameters
# Query is used to pass value into the URL

from fastapi import FastAPI

app=FastAPI()



data={
    1:{
        "name":"Mangesh sathe",
        "Role":"Software developer trainee",
        "Location":"Mumbai"
    },
    2:{
        "name":"Tushar sanap",
        "Role":"Python developer",
        "Location":"Goregaon"
    }
}



@app.get("/get-by-name")
# here None will make that name is not required 
def get_student(name : str = None ):
    for  student_id in data:
        if data[student_id]['name']==name:
            return data[student_id]
    return {"data":"Not found"}


