# django-to-do

django-to-do is a simple web application created using Django. It served me as a learning project for understanding and implementing Django functionalities.

## Cloud Hosting

The application is hosted on PythonAnywhere. You can access it here: [adhiraj.pythonanywhere.com](https://adhiraj.pythonanywhere.com/).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Features](#features)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [About](#about)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/adhirajcs/django-to-do.git
    cd django-to-do
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:
    ```bash
    python manage.py migrate
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Usage

- **Home Page:** View and manage your to-do items.
- **Add To-Do:** Use the form to add a new to-do item.
- **Edit To-Do:** Edit an existing to-do item.
- **Complete/Uncomplete To-Do:** Mark a to-do item as completed or uncompleted.
- **Delete To-Do:** Remove a to-do item.

## Folder Structure

The project directory structure is as follows:

```
django-to-do/
│
├── myapp/
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── templates/
│ ├── base.html
│ ├── edit.html
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ └── ...
│
├── todo/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── venv/
│ └── ...
│
├── win_venv/
│ └── ...
│
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

## Features

- User authentication (Register, Login, Logout)
- Add, edit, complete/uncomplete, and delete to-do items
- Responsive design using Bootstrap


## License

It is not under any license and is purely for educational purposes.
