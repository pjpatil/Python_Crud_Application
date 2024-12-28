# Python_Crud_Application
Disciption :create Employee application on pyhon with database connection Mysql

## Floder structure:

Employee_app/ 
│ 
├── app.py                # Main application file (your current code)
├── templates/            # Folder to store HTML templates
│   ├── index.html        # Template for the homepage (list of employees)
│   ├── create.html       # Template for the "Create" page
│   └── update.html       # Template for the "Update" page
├── static/               # Folder to store static files like CSS, JS, images
│   ├── style.css

## Create Sql table Query:

use itwork;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    department VARCHAR(255)
);
