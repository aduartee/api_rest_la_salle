### Welcome to my project
- In this project, I've created a simple API using Python, Flask, and MongoDB. 

### Purpose of the API
- This API serves as an endpoint for a mobile application. The application utilizes this API to manage questions and get correct responses.

### What you find in this API?
With this API, you can perform basic CRUD operations:

    (C) - Create 
    (R) - Read 
    (U) - Update 
    (D) - Delete 

## Getting Started
To run the API locally, follow these steps:


## How can you test the API? 
Run this commands in temrminal:
1. List all questions (GET):
`
curl -X GET http://localhost:5000/questions
`

2. Get a specific question by ID (GET):
`
curl -X GET http://localhost:5000/questions/<question_id>
`

3. Add a new question (POST):
`
curl -X POST -H "Content-Type: application/json" -d '{"title": "New Question", "questions": ["Option 1", "Option 2", "Option 3"], "response": 0}' http://localhost:5000/questions
`

4. Update an existing question (PUT):
`
curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Question", "questions": ["New Option 1", "New Option 2", "New Option 3"], "response": 1}' http://localhost:5000/questions/<question_id>
` 

5. Delete an existing question (DELETE):
`
curl -X DELETE http://localhost:5000/questions/<question_id>
`

### Project Running
![image](https://github.com/aduartee/api_rest_la_salle/assets/103082913/1a2c9d77-8331-4e68-be94-a1971bfbbc33)

## How can you run this project?

1. Clone the project repository to your local system:

    ```bash
    git clone https://github.com/aduartee/api_rest_la_salle.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-project
    ```

3. Create a Python virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Linux/macOS:

    ```bash
    source venv/bin/activate
    ```

5. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Start the Flask server:

    ```bash
    python rest_api.py
    ```

    This will start the Flask server on the default port `5000`.


### References
- https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#std-label-install-mdb-community-ubuntu
- https://medium.com/featurepreneur/mongodb-crud-with-flask-e5700ad7996e
- https://www.moesif.com/blog/technical/restful/Guide-to-Creating-RESTful-APIs-using-Python-Flask-and-MongoDB/
- https://flask.palletsprojects.com/en/3.0.x/#api-reference
- https://www.youtube.com/watch?v=6KscmgLZFic
- https://www.geeksforgeeks.org/how-to-connect-mongodb-compass-to-flask/
