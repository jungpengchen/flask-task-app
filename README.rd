To build image:
        docker-compose build
Set up FLASK_APP_HOST_PORT (default: 8080) on .env file to expose port for the flask api server.
To start the flask app with docker compose:
        docker-compose run --service-ports app
To run the unittest, run command below in the container:
        pytest -v --cov=./
To check the coverage report, open index.html under the htmlcov.
        pytest -v --cov=./ --cov-report=html
After start the flask, you can see the swagger document on http://localhost:8080/apidocs/.
Before deploy the flask app to production, set up FLASK_DEBUG (default: 1) and SWAGGER_ON (default: 1) by the deployment environment. (refer to env/develop)