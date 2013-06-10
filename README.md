restorethefourth.website
========================

##GENERAL INFO:

See here for a list of planned July 4th, 2013 protests organized by State.
We do NOT condone violence in any way. Posts or comments inciting violence are subject to removal.
If you agree with these demands, then please subscribe:
By exercising our right to vote and peacefully protest, the removal from office of any official in government who acted against our fourth amendment rights. No apologies, no amends, simply removal from office.

Repeal the patriot act and other similar laws. If our currently elected representatives will not do so (highly unlikely), than we shall in the course of time elect those who will.

The implementation of a transparent government which respects the fourth amendment and represents the interests of the people of the United States of America.


###ABOUT THIS REPO:

official/currently used for designing/developing the restorethefourth.net website.
The official website wether it be restoretheforth, restorethe4th.com, or others will desided until due notice.
For now, the basic wireframe, layout, and information will be worked on.

This repo was made in direction and response with http://www.reddit.com/r/restorethefourth/

####Basic design:(In Progress)

1. A Basic Home/landing page with the list of bills by ID and name, perhaps a short description to help identfy their intent.

#### What we don't want to do:

We don't want this site to become bloated or watered down. We want to keep it simple and get it up and running quickly to support what's going on in reddit. We want to chose a technology that more than one or two people know so we've got a base that can work on it.

###COMMUNICATION:

####Email: 
When using email always try to use GPG encryption.
All available collaborator's public PGP keys will be in the PGP keys file.

* To Get on OSX: https://gpgtools.org
* To Get on Windows: http://www.gpg4win.org/
* To Get on Linux: https://www.apache.org/dev/openpgp.html

####IRC Channels:

We currently have 2 irc channels:
* General Discussion: http://webchat.snoonet.org/?channels=restorethefourth
* Dev Discussion: http://webchat.snoonet.org/?channels=r4dev

##Teams:

In the present moment we have ~2 teams:

###1. WEB DEVELOPMENT:

If you are a dev, Web Development will be currently worked on (this) repo.

###2. PR/Content Team


####Basic design:(In Progress)

1. A Basic Home/landing page with the list of bills by ID and name, perhaps a short description to help identfy their intent.

#### What we don't want to do:

We don't want this site to become bloated or watered down. We want to keep it simple and get it up and running quickly to support what's going on in reddit. We want to chose a technology that more than one or two people know so we've got a base that can work on it.

## Available domain names
* restorethefourth.us
* restorethe4th.com
* restorethe4th.la
* restorethefourthamendment.com
* restorethefourth.net

###Current Domain Names online: 
* http://www.restorethefourth.net/


## MEZZANINE BASELINE PROJECT
### How to run the dev site on OS X
This is mostly command line stuff:

First off [install virtualenv wrapper](https://jamiecurle.co.uk/blog/installing-pip-virtualenv-and-virtualenvwrapper-on-os-x/).

Now create a virtualenv:
`mkvirtualenv restorethefourth`

Install requirements:
`pip install -r fourth/requirements.txt`

From the "fourth" directory, create a database:
`./manage.py createdb`

Now run the server:
`./manage.py runserver`

In your browser:
http://localhost:8000

### Before deploying

* Change value of settings.SECRET_KEY
