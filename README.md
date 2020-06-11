# RATER PROJECT

## Author
**Clare Richards**

## This is a Django Web Application where you can post and/or view different projects and rate them according to design,usability and content.


## Description
This is a Django Web Application where you can post and/or view different projects and rate them according to design,usability and content.


## Link to deployed site


## Setup and installations
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided

## Running the tests

Explain how to run the automated tests for this system

## Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

## And coding style tests

Explain what these tests test and why

```
Give an example
```


### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    - Django

## Clone the Repo and rename it to suit your needs.
```bash
git clone [https://github.com/SaintieMonte10/Rater.git]
```
## Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

## Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

## Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='rdtfyguihjohucbdsjnc'
DEBUG=True
DB_NAME='awards'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

## Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

## Make and run migrations
```bash
python3.6 manage.py check
python manage.py makemigrations awards
python3.6 manage.py sqlmigrate awards 0001
python3.6 manage.py migrate
```

## Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)


## Support and contact details
Contact [Clare Richards](claremonte53@gmail.com) for further help/support

### License
[MIT LICENSE](LICENSE)

Copyright (c)2020 **Clare Richards**