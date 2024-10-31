# This file includes global variables that will be available inside your project
# 1. In the front end code you can access this variables like this: console.log(process.env.VARIABLE_NAME)
# 1. In the back end code you access the variable by importing os and then typing print(os.getenv('VARIABLE_NAME'))

# Back-End Variables
DATABASE_URL=postgres://gitpod:postgres@localhost:5432/example
FLASK_APP_KEY="any key works"
FLASK_APP=src/app.py
FLASK_DEBUG=1
DEBUG=TRUE

# Front-End Variables
BASENAME=/
BACKEND_URL=https://sample-service-name-w3sa.onrender.com/api

export FLASK_APP="src/app.py"