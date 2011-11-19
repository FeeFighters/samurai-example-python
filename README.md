This is a sample app which showcases the use of python library for the [Samurai API](http://feefighters.com/samurai) from [Fee
Fighters](http://feefighters.com).

Here are the steps to run this app in a python virtualenv. Using virtualenv instead of installing everything on your
machine is always a good idea

Steps:

1. Install python-setuptools - ```sudo apt-get install python-setuptools```

2. Install pip - ```sudo easy_install pip```

3. Install virtualenv - ```sudo pip install virtualenv```

4. Make a virtual env directory - ```mkdir ~/virtualenv```

5. Create a virtual environment for the project - ```virtualenv --no-site-packages --distribute ~/virtualenv/samurai-example-python```

6. Clone the repo if you haven't already

7. ```cd samurai-example-python```

8. Activate the virtual environment - ```source ~/virtualenv/samurai-example-python/bin/activate```

9. Install dependencies - ```pip install -r deps.txt```

10. ```cd sample```

11. ```python manage.py syncdb```

12. ```python manage.py runserver```

13. go to 127.0.0.1:8000
