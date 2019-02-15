from flask import Flask 
 app = Flask(_name_)

@app.route('/')
def HelloWorld():
    return "Hello, World"