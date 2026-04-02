# Combining query and path parameter's
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


from typing import Optional
@app.get('/get_students_by_name_and_id/{student_id}')
def student_details(student_id: int , name : Optional[str] = None):

    for studentid in data:
        if data[studentid]['name']==name and studentid==student_id:
            return data[studentid]

    return { "Data":"Not found"}