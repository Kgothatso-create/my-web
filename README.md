# My website project
Welcome to my website project built using Django.

## Requirements
* Python 3.11
* Django 3.2.4

## Installation
* Clone the repository or download the zip file.
* Install the required packages: pip install -r requirements.txt
* Run the server: python manage.py runserver
* Navigate to http://127.0.0.1:8000/ to view the website.

## Creating a secret key
To generate a new Django secret key, you can use the built-in get_random_secret_key function provided by Django.
Remember to keep your secret key safe after it is provided. 
You can execute the following code in a Python interpreter:
* from django.core.management.utils import get_random_secret_key
* print(get_random_secret_key())

## Documentation
Documentation for this project was created using Sphinx. 
You can find the documentation by opening the docs/_build/html/index.html file in your browser.

## Docker
I have also created a Docker image for this project. 
To run the Docker image, follow these steps:

## Build and Run Application with Docker
* Clone the repository: git clone https://github.com/Kgothatso-create/my-website.git
* Navigate to the repository directory: cd your-repo
* Build the Docker image: docker build -t my-app .
* Run the Docker container: docker run -p 8000:8000 my-app
* Open your web browser and navigate to http://localhost:8000/ to view the application.
