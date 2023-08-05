## Clone Repo

    # git clone git@github.emcrubicon.com:AAI/ONBFactory.git


## Virtual Environment

    ### Create

    $ virtualenv <name-of-folder>

    ### Activate

    $ source <path-to-folder>/bin/activate

    ### Deactivate

    $ deactivate


## Install requirements

    $ pip3 install -r requirements.txt


## Command to run the Project

    ### Local
    $ python manage.py runserver

    ### production
    $ gunicorn --bind 0.0.0.0:$PORT --access-logfile - ONBFactory.wsgi:application


## Run Flake8 before commit (run on the root of the project)

    $ flake8


## Apps.py - What is this and how it is used

    https://docs.djangoproject.com/en/2.0/ref/applications/#application-configuration

