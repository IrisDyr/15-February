
from flask import Flask
app = Flask(__name__)



my_course= [
    {"id":"1", "name: Python "}
    {"id":"2", "name: Flask "}
]
def post_course(course_id):
    my_courses.append({"id": course_id, "name":})

def get_course(id):
    for ocurse in my_course:
        if course["course_id"] == course_id:
            return course  
        else:
            return {"course": None}



@app.route('/courses', methods =['GET', 'POST'])
def courses(id, name):
    if request.metho == 'Post':
        return post_course(id, name)
    else:
        return post.course(id)