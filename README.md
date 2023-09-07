# Stellar Elements Technical Exercise
Juan Pablo Moreno's answer for the Technical Exercise for Stellar Elements company.

## Installation
Assuming you are using a MAC laptop, follow the steps below:
- prerequisites: python3 > 3.7.0 installed
- download the code
- go to terminal and execute the following commands:
  - cd path_to_project
  - python3 -m venv venv (this creates the virtual environment called venv)
  - source venv/bin/activate
  - pip install -r requirements.txt (this installs all the required libraries into the virtual environment)

## Execution
### Running Backend tests (API tests)
Go to terminal (with the virtual environment activated) and execute the following command:
- pytest --html=report.html --self-contained-html
<br>This runs the tests and creates a report.html file. Open it to see the results.
### Running load test
Go to terminal (with the virtual environment activated) and execute the following command:
- locust -f load_tests/load_testing.py 
- go to browser and open http://0.0.0.0:8089
- set number of users = 160 and Spawn rate 10. click on Start swarming
- wait... after 17 seconds, once the users reach the 160 the api call starts to fail with error 140	GET	/api/productsList	HTTPError('503 Server Error: Service Unavailable for url: /api/productsList')

