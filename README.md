# pytest_example

Some basic knowledge on testing with Python:

https://realpython.com/python-testing/ 

For this example `pytest` lib has been chosen as a simpler and easier-to-code alternative to unittest. It is better supported and more widely used than `unittest` and `nose`.

The test are in `tests/unit` folder. The example is based on some operations with Postgresql and shows how to mock it.
Read more about mocks [here](https://www.toptal.com/python/an-introduction-to-mocking-in-python).

### Prepare environment and run tests

1. Install Python3

https://www.python.org/downloads/

2. Create [virtual environment](https://docs.python.org/3/library/venv.html) to isolate installed requirements

`python3 -m venv venv`

3. Activate virtual environment

`source venv/bin/activate`

4. Setup environmental variables 

5. From root dir run

`pytest --cov-report html --cov=hello_world_app tests/`

This command will run all the tests started with `test_` under `tests` dir and create html [coverage](https://pytest-cov.readthedocs.io/en/latest/reporting.html) report in `htmlcov` folder. Open `index.html` file in this folder via browser and you will see coverage report: how much code is covered with tests run.
