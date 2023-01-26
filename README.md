## Create a directory path that you're comfortable with,
## then install a virtual environment and activate it!
    CMD :\comyf_path> py -m venv .venv
    CMD :\comyf_path> .\.venv\scripts\activate

## Clone this repo into a new folder named src:
    CMD :\comyf_path\src> git clone https://github.com/lundchristian/flask_api_v3

## Install Flask and dotenv, like so:
    CMD :\comyf_path> pip install Flask
    CMD :\comyf_path> pip install python-dotenv

## We are aiming for a directory hierarchy like this:
    .
    └── comfypath/
        ├── .venv
        ├── src/
        │   ├── controller/...
        │   ├── database/...
        │   ├── static/...
        │   ├── model/...
        │   ├── view/...
        │   └── __init__.py
        ├── .env
        └── wsgi.py


## Create database and run the application
    CMD > flask --app src Database.initialize
    CMD > py -B wsgi.py
