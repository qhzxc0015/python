
from peewee import *


# db=MySQLDatabase("pythonDB.db")
db = MySQLDatabase('pythonDB', **{'host': 'localhost', 'password': '123', 'port': 3306, 'user': 'root'})

class BaseModel(Model):
    class Meta:
        database = db

class Course(BaseModel):
    id = PrimaryKeyField()
    title = CharField()
    period = IntegerField()
    class Meta:
        order_by = ("title",)
        db_table = 'course'

class Teacher(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    gender = BooleanField()
    address = CharField()
    course_id = ForeignKeyField(Course, to_field="id", related_name="course")

    class Meta:
        order_by = ('name',)
        db_table = 'teacher'





