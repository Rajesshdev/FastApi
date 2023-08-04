from fastapi import APIRouter
from modules.student import Student
from config.database import connection
from schemas.student import studentEntity,listOfStudentEntity
from bson import ObjectId
student_router=APIRouter()
@student_router.get('/students')
async def find_all_student():
        return listOfStudentEntity(connection.local.student.find())
@student_router.get('/students{studentid}')
async def Find_one_student(studentid):
        return studentEntity(connection.local.student.find_one({"_id":ObjectId(studentid)}))
#create a student
@student_router.post('/students')
async def create_student(student:Student):
        connection.local.student.insert_one(dict(student))
        return listOfStudentEntity(connection.local.student.find())
#
@student_router.put('/students{studentid}')
async def update_student(studentid,student:Student):
        connection.local.student.find_one_and_update(
                {"_id": ObjectId(studentid)},
                {"$set":dict(student)})
@student_router.delete('/students')
async  def delete_students(studentid):
       return studentEntity(connection.local.student.find_one_and_delete({"_id":ObjectId(studentid)}))