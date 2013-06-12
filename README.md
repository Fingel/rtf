restorethefourth.website
========================

###ABOUT THIS REPO:

Official repo for designing/developing the restorethefourth.net website.
For now, the basic wireframe, layout, and information will be worked on.

This repo was made in direction and response with [http://www.reddit.com/r/restorethefourth/](http://www.reddit.com/r/restorethefourth/)

# Getting up to speed.

We're using [Django](https://www.djangoproject.com). If you aren't familiar it's very well documented.

### How to run the dev site on OS X (should work on Linux as well)
This is mostly command line stuff:

If you plan on contributing code you should fork the repo, I will assume you are familiar with that process.

First, make a directory for the project
    
    mkdir restorethefourth

Now clone the repo, it will clone into a directory named rtf, for the sake of convenience rename this directory to fourth.

    git clone https://github.com/100010001/rtf.git
    mv rtf fourth


Make sure you've [installed virtualenv](https://jamiecurle.co.uk/blog/installing-pip-virtualenv-and-virtualenvwrapper-on-os-x/).

Now create a virtualenv:

    virtualenv venv

Install requirements:

    pip install -r fourth/requirements.txt

Create your local_settings.py file

    cp fourth/rtf/local_settings.default fourth/rtf/local_settings.py

From the "fourth" directory, create a database:
    
    ./manage.py createdb

Now run the server:
    
    ./manage.py runserver

The dev site is now your browser:
[http://localhost:8000](http://localhost:8000)

###COMMUNICATION:

####IRC Channels:

The Dev channel is #r4dev on irc.snoonet.org
The general channel is #restorethefourth on irc.snoonet.org

## Goals and Plans

#### What we don't want to do:

We don't want this site to become bloated or watered down. We want to keep it simple and get it up and running quickly to support what's going on in reddit. We want to chose a technology that more than one or two people know so we've got a base that can work on it.


###Current Domain Names online:

* [restorethefourth.net](http://www.restorethefourth.net/)