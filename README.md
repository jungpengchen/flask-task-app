## To build image
        docker-compose build
## To start the flask api server
1. Set up `FLASK_APP_HOST_PORT` (default: 8080) on `.env` file to expose port for the flask api server.
2. Start the flask app with docker compose:

        docker-compose run --service-ports app
## To run the unittest
run command below in the container:

        pytest -v --cov=./
## To check the coverage report
open `index.html` under the htmlcov.

        pytest -v --cov=./ --cov-report=html
## To check the swagger document
you can see the swagger document on http://localhost:8080/apidocs/ after start the flask api server
## Before deploy the flask app to production
set up `FLASK_DEBUG` (default: 1) and `SWAGGER_ON` (default: 1) by the deployment environment. (refer to `env/develop`)