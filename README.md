# ToDo Web App for Users

Our service allows users to create and manage notes with ease. You can easily register and login to start creating notes. With our service, you can create new notes or delete old ones with just a few clicks.

Tech Stack
This project uses the following technologies:

- Python 3.10 - The programming language used for the backend.
- FastAPI - The web framework used for the backend.
- HTML, CSS, and JavaScript - The front-end languages used to create the user interface.

## Want to use this project?

1. Fork/Clone

1. Install python venv:

    ```sh
    apt install python3.10-venv
    ```

1. Create and activate a virtual environment:

    ```sh
    python3 -m venv venv && source venv/bin/activate
    ```

1. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

1. Run the app:

    ```sh
    (venv)$ python main.py
    ```

1. Test at [http://localhost:8081/docs](http://localhost:8081/docs)

To start the program in the background, use this command:
```sh
nohup python main.py &
```

To stop:
```sh
ps aux | grep main.py
```
```sh
kill <PID>
```

# Some helpful hints:

If some port already busy (test on ubuntu) = sudo fuser -k 8000/tcp
To clear all container images              = sudo docker system prune -a --volumes

Links:
remember general flow:
https://fastapi-users.github.io/fastapi-users/10.4/usage/flow/


sources:
https://testdriven.io/blog/fastapi-jwt-auth/
https://github.com/testdrivenio/fastapi-jwt
Securing FastAPI with JWT Token-based Authentication
Check out the [post](https://testdriven.io/blog/fastapi-jwt-auth/).