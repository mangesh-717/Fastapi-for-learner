# Defining path parameters
from fastapi import FastAPI , Path


app=FastAPI()

@app.get("/")
def index():
    return {"name":"Mangesh Sathe"}


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


# here the queryparameter is defined
@app.get("/employee_data/{employee_id}")
def employee_(employee_id: int):
    return data[employee_id]


# here the queryparameter is defined
@app.get("/employee_filtered_data/{employee_id}")
def employee_most_filtered_details(employee_id: int = Path( description="The Id of the employe that you want to view", gt=0, lt=3)):
    return data[employee_id]


