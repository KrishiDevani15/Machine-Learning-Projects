from flask import Flask
app=Flask(__name__) #Special Attribute __name__ --> the name of class,functions,methods,descriptor or generator instance.

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run() # du to this we dont need to write set FLASK_APP = hello.py, flask run ---> Instead directly write hello.py in cmd