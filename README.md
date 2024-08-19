# Limit Content Types in Django Model

This repository demonstrates how to limit content types in Django model (ORM).

For more information check out the [post](https://testdriven.io/blog/django-limiting-content-types/).

## Want to use this project?

1. Fork/Clone

1. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

1. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

1. Apply the migrations:

    ```sh
    (venv)$ python manage.py migrate
    ```

1. Create a superuser and populate the database by loading the fixture: 

    ```sh
    (venv)$ python manage.py createsuperuser
    (venv)$ python manage.py loaddata ./dealership/fixtures/initial_data.json
    ```

1. Run the server:

    ```sh
    (venv)$ python manage.py runserver
    ```

1. Navigate to [http://localhost:8000/admin](http://localhost:8000/admin) in your favorite browser. The content type in
   `Sale` model should be limited to `Car`, `ElectricCar`, and `Motorcycle`.
