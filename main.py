from fastapi import FastAPI , Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students={
    1: {"name": "John", "age": 20, "class": "12th"},
    2: {"name": "Jane", "age": 22, "class": "11th"},
}

class Student(BaseModel):
    name:str
    age:int
    year:str

class Update_student(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    year:Optional[str]=None

@app.get("/home")
def index():
    return 'this is the home page'

@app.get("/get-student/{student_id}")
def get_student(student_id: int=Path(...,description="The ID of the student to retrieve",gt=0,lt=4)):
    return students[student_id]

@app.get("/get-by-name")
def get_student_by_name(name:Optional[str]=None):
    for student_id in students:
        if students[student_id]['name']==name:
            return students[student_id]
        
@app.post("/create-students/{student_id}")
def create_student(student_id:int,student:Student):
    if student_id in students:
        return {'Error, student already exists'}
    
    students[student_id]=student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id:int,student:Update_student):
    if student_id not in students:
        return{'this student does not exist'}
    
    if student.name !=None:
        students[student_id].name=student.name
    if student.age !=None:
        students[student_id].age=student.age
    if student.year[student_id] !=None:
        students[student_id].year=student.year
    
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return{"error, the student is not in list"}

    del students[student_id]
    return {'student is deleted successfully'}