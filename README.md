# Automated Testing with Selenium and Python
This is a simple example of how to use Selenium with Python to automate testing of a web application. The example is based on the [Selenium Python Bindings](https://selenium-python.readthedocs.io/).

## Setting up the Example Project
The example project is a simple University Management System (UMS) that allows you to add, edit, and delete students, faculties, courses, notices and manage user profiles. The project is written in PHP and JavaScript using the MVC architecture.

- Open XAMPP and start the Apache and MySQL servers.
- Clone the project into the 'htdocs' folder of XAMPP.
- Create a new database in MySQL and name it 'webtech'.
- Import the 'webtech.sql' file into the newly created MySQL database.
- From your browser, go to 'http://localhost/{folder_name}/view' to see the project.

## Starting the Automated Testing
- Open the terminal and cd into the tests folder.
- Run the following command to start the automated testing:
```
python -m unittest sel_v3.py
```