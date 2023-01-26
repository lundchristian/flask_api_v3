## Generate stories with artificial intelligence :space_invader:

Simple flask application where you can create a story and add chapters. You can either add your own chapter, or let the AI create one that is based on the story so far! You can edit the chapters as you like or leave the be, have fun!

![](https://github.com/lundchristian/flask_api_v3/blob/master/GIF.gif)

#### Create a directory path that you're comfortable with, then install a virtual environment and activate it!
    CMD :\comyf_path> py -m venv .venv
    CMD :\comyf_path> .\.venv\scripts\activate

#### Clone this repo into a new folder named src:
    CMD :\comyf_path\src> git clone https://github.com/lundchristian/flask_api_v3

#### Install Flask and dotenv, like so:
    CMD :\comyf_path> pip install Flask
    CMD :\comyf_path> pip install python-dotenv
    CMD :\comyf_path> pip install openai

#### We are aiming for a directory hierarchy like this:
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

#### Inside the .env file you need to refer to your OpenAi API key:
    # .env file
    OPENAI_API_KEY=your_secret_key

#### Create database and run the application
    CMD > flask --app src Database.initialize
    CMD > py -B wsgi.py
