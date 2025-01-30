# FlaskEmp
Flask CRUD app using REST API and MongoDB

## Table of Contents
1. [Setting up](#setting-up)
2. [Research](#research)
   - [Choosing Pydantic](#choosing-pydantic)
   - [To build application for scalability](#to-build-application-for-scalability)
     - [References](#referencesmajor)
     - [Take aways](#take-aways)
3. [Not within the scope of this project](#not-within-the-scope-of-this-project)

## Prerequisites

- [Docker](https://www.docker.com/get-started) (with Docker Compose)
- [Postman](https://www.postman.com/downloads/) (for testing the API endpoints)

## Setting up

1. Clone the repository
2. Install dependencies
```
pip install -r requirements.txt
```
3. Build and run containers
```
docker-compose up --build
```
4. The Flask app should now be running on http://localhost:5000 and accessible from Postman or a browser.
5.  Go to ```http://localhost:5000/api/login``` and send
```
{
    "username": "admin",
    "password": "admin"
}
```
6. Copy the token from the response and in Authorization tab send the Bearer Token with that token value as a get request to ```http://localhost:5000/api/employee``` be authenticated as admin and see all employees

7. GET ```http://localhost:5000/api/employee?empid=xyz``` to see employee with that empid

8. POST ```http://localhost:5000/api/employee``` to add employee with schema
```
    empid: integer
    name: string
    email: email string
    pword: str = Minimum 6 chars long string

```
9. PUT to ```http://localhost:5000/api/employee?empid=xyz``` to update employee with same schema as above

10. DELETE to ```http://localhost:5000/api/employee?empid=xyz``` to delete employee

7. POST to ```http://localhost:5000/api/logout``` to log out of the admin session

## Research

### In this I have built the API from scratch 
But Flask-Smorest is a powerful extension for Flask that streamlines the development process for robust and well-structured RESTful APIs
Can research further on this: <br>
https://rest-apis-flask.teclado.com/docs/flask_smorest/why_flask_smorest/#:~:text=Of%20course%2C%20you%20can%20keep,still%20a%20totally%20viable%20option. <br>
https://datascienceafrica.medium.com/level-up-your-flask-apis-with-flask-smorest-3dc00dd7bc19  <br>
### Choosing Pydantic
Researched upon which data validation library is the best and by popular opinion it is pydantic because of its immense features and above all scalability as it is 10x faster than some of the other options like marshmallow or jsonschema

### To build application for scalability
#### References(major) :
1. https://www.linkedin.com/pulse/10-tips-write-scalable-flask-applications-vijay-londhe-mxcoc/
2. https://medium.com/@joseleonsalgado/building-scalable-apis-with-flask-best-practices-for-software-engineers-c4305a687ed6

#### Take awaysS
1. Better structure your application. This means building reusable components and initializing extensions inside a separate function

2. Blueprints help to modularize your application Instead of one app, create separate blueprints for pieces of functionality such as authentication, user management, or APIs

3. The application factory pattern allows you to create multiple instances of your Flask application, each with its own configuration settings

4. Rate Limit API Requests: Use rate-limit solution to avoid abuse and handle spike in traffic. Use Libraries like Flask-Limiter<br>
https://flask-limiter.readthedocs.io/en/stable/<br>
Advanced rate limiting: Redis <br>
I have not used a storage but in production use we have to specify that<br>

5. Scalability is also about resilience: Flask-Talisman to enforce security headers, and ensure that user inputs are validated to prevent injection attacks<br>
https://pypi.org/project/flask-talisman/<br>

6. Set up logging with SENTRY or Flask-Logging. Use Prometheus and Grafana to provide observability to monitor performance and test bottlenecks [NOT IMPLEMENTED]

7. Deploy your Flask app in a Docker container for isolating environment dependencies

8. Use caching layers to minimize the stress on your Flask app and database. To cache responses for repeated requests, you can do it via extensions like Flask-Caching [NOT IMPLEMENTED]

9. Secure Your API with JWT
https://flask-jwt-extended.readthedocs.io/en/stable/
https://flask-jwt-extended.readthedocs.io/en/stable/blocklist_and_token_revoking.html

### Not within the scope of this project:
1. WSGI server: WSGI stands for Web Server Gateway Interface. It's a standard interface that allows web servers to communicate with Python web applications. WSGI is used to forward requests from a web server to a Python web application, and then pass the response back to the web server. 
Using Gunicorn for apps in production. It is a WSGI HTTP server for UNIX. It's designed to serve Python web applications by handling multiple requests concurrently. Gunicorn can efficiently manage multiple worker processes to handle large loads, making it a great choice for production deployments.

2. Asynchronous Task Execution with Celery