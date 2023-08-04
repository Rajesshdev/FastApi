def studentEntity(db_item)-> dict:
    return {
        "id":str(db_item["_id"]),
        # "studentid":str(db_item["student_id"]),
        "name":str(db_item["student_name"]),
        "email":str(db_item["student_email"]),
        "phone":str(db_item["student_phone"])

    }
def listOfStudentEntity(db_item_list)->list:
    list_stud_entity=[]
    for item in db_item_list:
        list_stud_entity.append(studentEntity(item))
    return list_stud_entity