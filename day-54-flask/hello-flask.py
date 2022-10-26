from flask import Flask
import random
import time
app = Flask(__name__)
#indicates the file that is being run( __name__)
print(__name__)
print(random.__name__)
'''
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
'''
#nested functions
#decorator function wraps another function and gives it an additional functionality or modifies the functionality


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

#With the @syntactic sugar
@delay_decorator
def say_hello():
    print("Hello")
