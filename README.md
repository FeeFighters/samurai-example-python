This is a sample app which showcases the use of python library for the [Samurai API](http://feefighters.com/samurai) from [Fee
Fighters](http://feefighters.com).

Here are the steps to run this app in a python virtualenv. Using virtualenv instead of installing everything on your
machine is always a good idea

Steps:
* Install python-setuptools - ```sudo apt-get install python-setuptools```
* Install pip - ```sudo easy_install pip```
* Install virtualenv - ```sudo pip install virtualenv```
* Make a virtual env directory - ```mkdir ~/virtualenv```
* Create a virtual environment for the project - ```virtualenv --no-site-packages --distribute ~/virtualenv/samurai-example-python```
* Clone the repo if you haven't already
* ```cd samurai-example-python```
* Activate the virtual environment - ```source ~/virtualenv/samurai-example-python/bin/activate```
* Install dependencies - ```pip install -r deps.txt```
* ```cd sample```
* ```python manage.py syncdb```
* ```python manage.py runserver```
* go to 127.0.0.1:8000
