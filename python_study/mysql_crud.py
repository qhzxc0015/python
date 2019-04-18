from orm_mysql import Teacher, Course

Course.create_table()
Teacher.create_table()
Course.create(id=3, title="333", period=3320, description="3333")
Teacher.create(name="ccc", gender=True, address="333", course_id=3)