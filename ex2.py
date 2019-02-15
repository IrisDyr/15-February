
from flask import Flask
app = Flask(__name__)


@app.route('/courses', methods =['GET', 'POST'])
my_list = []
def courses():
    if request.metho == 'Post':
        return my_list
    else:
        return my_list.append("Course")
