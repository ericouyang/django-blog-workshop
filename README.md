# Workshop: Building a simple blog platform using Django 

In this short workshop, we'll be using [Django](https://www.djangoproject.com), an open-source web framework written in Python, to develop a simple blogging platform. 

## Installation 

### macOS 

1. If you don't have a recent version of Python installed, first install the [Brew package manager](http://brew.sh/), which helps you manage dependencies on macOS.

2. Install necessary dependencies: 
  
  `$ brew install python && brew install sqlite`

3. Install `virtualenv` globally via pip, the Python package manager. This tool allows to create virtual environments to help make development more manageable. 

  `$ pip install virtualenv`

4. Create a new virtualenv named `blog` in a convenient location on your machine:

  `$ virtualenv blog`

5. Navigate into the created `blog` folder using `cd blog` and activate the virtualenv:

  `$ source bin/activate`

6. Install Django via pip:

  `$ pip install Django`

7. Create a new Django project: 

  `django-admin startproject myblog`

8. Navigate into the created `myblog` project folder using `cd myblog`

9. Run the development server on port 8000

  `$ ./manage.py runserver`

10. Navigate in your browser to `http://localhost:8000`

11. (Optional) Install Visual Studio Code: https://code.visualstudio.com/docs/setup/mac

### Windows

Start by following the instructions for [installing Python, PIP, Setuptools, and Django](https://docs.djangoproject.com/en/1.11/howto/windows/).

1. If you don't have a recent version of Python install, first install the [Chocolatey package manager](https://chocolatey.org), which helps you manage dependencies on Windows. 

2. Install necessary dependencies: 
  
  `$ choco install python && choco install sqlite`

3. Install `virtualenv` globally via pip, the Python package manager. This tool allows to create virtual environments to help make development more manageable. 

  `$ pip install virtualenv`

4. Create a new virtualenv named `blog` in a convenient location on your machine:

  `$ virtualenv blog`

5. Navigate into the created `blog` folder using `cd blog` and activate the virtualenv:

  `$ Scripts\activate`

6. Install Django via pip:

  `$ pip install Django`
  
7. Create a new Django project: 

  `django-admin startproject myblog`

8. Navigate into the created `myblog` project folder using `cd myblog`

9. Run the development server on port 8000

  `$ ./manage.py runserver`

10. Navigate in your browser to `http://localhost:8000`

11. (Optional) Install Visual Studio Code: https://code.visualstudio.com/docs/setup/windows

