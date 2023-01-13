# using packages from venv by telling this file where is it and what to import 
from flask import Flask, Response
# creating a variable
app = Flask(__name__)

# this is the address to the webpage. If you were to change the string inside route to /johnny then it would route this to http://localhost:5000/johnny 
# with just '/' means that the web address ends with '/' = http://localhost:5000'/'
# App Routing means mapping the URLs to a specific function that will handle the logic for that URL
@app.route('/')    
# create or define a function
def welcome():
    response_text = '{"message": "Hello, welcome to Johnny\'s flask-api"}' 
    response = Response(response_text, 200, mimetype='applications/json')  # returning the reponse type as json 
    return response


# if statement to run app it '__name__' meets the matches '__main__'
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True) # port numbers can only be used once so will not be able to use 5000 again, debug is set to True to let users know about errors if there are any
