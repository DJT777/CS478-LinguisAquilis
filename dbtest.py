from  database import  database

myDb = database()

mylist = [
    {
        "course_dept": "ACCT",
        "course_number": "201",
        "course_title": "Accounting Principles I"
    },
    {
        "course_dept": "IME",
        "course_number": "331",
        "course_title": "Introduction to Statistical Quality Control"   
    },
    {
        "course_dept": "REST",
        "course_number": "325",
        "course_title": "Advanced Pulmonary Diseases"
    }
]

sampleCourse =     {
        "course_dept": "ACT",
        "course_number": "415",
        "course_title": "Auditing Theory and Practice"
}

myDb.path = './data/sql.db'
# myDb.testCursor()
#myDb.dropTable('classlist')
# myDb.createTable('classlist')
myDb.insertClass(mylist, 'classlist')
# myDb.closeConnection()
myDb.courseExists(sampleCourse, 'classlist')
# myDb.courseExists(sampleCourse, 'classlist')
# myDb.courseExists(sampleCourse, 'classlist')
myDb.getTopCourses('classlist')


myDb.createTable('selectClass')
myDb.createTable('describeClass')
myDb.createTable('describeMajor')