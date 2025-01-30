# FlaskEmp
Flask CRUD app using REST API and MongoDB

## Setting up


## Research
### Choosing Pydantic
Researched upon which data validation library is the best and by popular opinion it is pydantic because of its immense features and above all scalability as it is 10x faster than some of the other options like marshmallow or jsonschema

### To build application for scalability
** References(major) : **
1. https://www.linkedin.com/pulse/10-tips-write-scalable-flask-applications-vijay-londhe-mxcoc/
2. https://medium.com/@joseleonsalgado/building-scalable-apis-with-flask-best-practices-for-software-engineers-c4305a687ed6

** Take aways **
1. Better structure your application. This means building reusable components and initializing extensions inside a separate function
2. Blueprints help to modularize your application Instead of one app, create separate blueprints for pieces of functionality such as authentication, user management, or APIs
3. The application factory pattern allows you to create multiple instances of your Flask application, each with its own configuration settings
4. Rate Limit API Requests: Use rate-limit solution to avoid abuse and handle spike in traffic. Use Libraries like Flask-Limiter<br>
https://flask-limiter.readthedocs.io/en/stable/<br>
Advanced rate limiting: Redis <br>
I have not used a storage but in production use we have to specify that<br>
5. Scalability is also about resilience: Flask-Talisman to enforce security headers, and ensure that user inputs are validated to prevent injection attacks<br>
https://pypi.org/project/flask-talisman/<br>
6. Set up logging with SENTRY or Flask-Logging. Use Prometheus and Grafana to provide observability to monitor performance and test bottlenecks
7. Deploy your Flask app in a Docker container for isolating environment dependencies
8. Use caching layers to minimize the stress on your Flask app and database. To cache responses for repeated requests, you can do it via extensions like Flask-Caching

Not within the scope of this project:
1. WSGI server: WSGI stands for Web Server Gateway Interface. It's a standard interface that allows web servers to communicate with Python web applications. WSGI is used to forward requests from a web server to a Python web application, and then pass the response back to the web server. Using gunicorn for apps in production
Gunicorn: This is a WSGI HTTP server for UNIX. It's designed to serve Python web applications by handling multiple requests concurrently. Gunicorn can efficiently manage multiple worker processes to handle large loads, making it a great choice for production deployments.

2. Secure Your API with JWT
3. Asynchronous Task Execution with Celery