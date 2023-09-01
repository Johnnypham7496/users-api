# users-api
my **sample** flask api

1. create repository with `.gitignore and license`

2. create a virtual environment with `python -m venv venv/`

3. turn on virtual environment with `. venv/Scripts/activate`

4. install flask with `pip install flask` 
from here there should be a folder inside of the working directory with venv. 
To make sure the virtual environment is on --- `refer to step 3`, this implies everytime you close out of terminal meaning that you will need to always check for the `(venv)` at the bottom of the terminal to make sure that your VM is on

5. `pip freeze > requirement.txt` - will create a requirements text that is installed from the packages and dependencies such as flask in this case
This will also be the same command to update the requirements.txt when installing new packages
`pip install -r requirements.txt` - use this command when cloning a repository with an existing requirements.txt

6. added hello world code and run to test if the code runs




`What is a api?` - a way to automate request, how a computer communicates to another when requesting data, only a way to see and get data but not change it otherwise this will corrupt the code or cause data breaches

`What is a virtual environment?` - an area that yo can code freely without having the installed packages affect your computer. Ensuring that the code you have built with the packages/dependicies will run on someone elses computer just like it did with your own. 

`Why install Flask?` - flask is a premade package that someone else has alreay made to help make creating the API process faster otherwise you would write the code from scratch which is too time consuming. 


4 major calls in api/HTTP method
    `get`- retrieve a record <br>
    `post` - create a record <br>
    `put` - modify record <br>
    `delete` - deletes a record <br>



To run the application use: 
    python app.py


To go to the swagger page use: http://localhost:8000/api/ui