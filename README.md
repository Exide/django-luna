# Luna
A game community web application using the Django framework.


## Quickstart

_Requires Python 2.7+. Does not support Python 3 yet._

### Install dependencies

These commands assume you're at the root of the repository.

```
$ pip2 install virtualenv
Collecting virtualenv
  Using cached virtualenv-15.0.2-py2.py3-none-any.whl
Installing collected packages: virtualenv
Successfully installed virtualenv-15.0.2
```

```
$ virtualenv --no-site-packages .venv
New python executable in .venv/bin/python2.7
Also creating executable in .venv/bin/python
Installing setuptools, pip, wheel...done.
```

```
$ .venv/bin/pip install -r requirements.txt
Collecting django==1.4.2 (from -r requirements.txt (line 1))
Collecting pillow==3.2.0 (from -r requirements.txt (line 2))
Collecting django-tagging==0.3.6 (from -r requirements.txt (line 3))
Collecting django-registration==0.7 (from -r requirements.txt (line 4))
Collecting django-pagination==1.0.7 (from -r requirements.txt (line 5))
Collecting markdown==2.1.0 (from -r requirements.txt (line 6))
Installing collected packages: django, pillow, django-tagging, django-registration, django-pagination, markdown
Successfully installed django-1.4.2 django-pagination-1.0.7 django-registration-0.7 django-tagging-0.3.6 markdown-2.1.0 pillow-3.2.0
```

Now you should have an isolated Python 2 environment ready to go at ```.venv/```.

### Configure the ```settings.py``` file

There are other settings, see [Django 1.4 Settings Overview](http://django.readthedocs.io/en/1.4.X/topics/settings.html), but these are the important ones to get started.

    SITE_NAME = 'Luna'
    ADMINS = ('Admin', 'admin@example.com')
    # GOOGLE_ANALYTICS_KEY = 'UA-12345678-9'
    ACCOUNT_ACTIVATION_DAYS = 7
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.example.com'
    EMAIL_HOST_USER = 'admin@example.com'
    EMAIL_HOST_PASSWORD = 'password'
    EMAIL_PORT = 587
    TIME_ZONE = 'America/Los_Angeles'
    LANGUAGE_CODE = 'en-us'


### Construct the backend

To get up and running you'll need to create the database and prime it with the necessary tables.

    $ .venv/bin/python manage.py syncdb
    Creating tables ...
    Creating table auth_permission
    Creating table auth_group_permissions
    Creating table auth_group
    Creating table auth_user_user_permissions
    Creating table auth_user_groups
    Creating table auth_user
    Creating table django_content_type
    Creating table django_session
    Creating table django_site
    Creating table django_admin_log
    Creating table account_profile
    Creating table forum_topic
    Creating table forum_post
    Creating table games_game
    Creating table registration_registrationprofile
    Creating table tagging_tag
    Creating table tagging_taggeditem

    You just installed Django's auth system, which means you don't have any superusers defined.
    Would you like to create one now? (yes/no): yes
    Username (leave blank to use 'exide'): admin
    E-mail address: admin@example.com
    Password:
    Password (again):
    Superuser created successfully.
    Installing custom SQL ...
    Installing indexes ...
    Installed 0 object(s) from 0 fixture(s)

### Startup the server


    $ .venv/bin/python manage.py runserver
    Validating models...

    0 errors found
    Django version 1.4.2, using settings 'Luna.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

### Configure the domain name for the site

_If you required to login, use the superuser account created in "Construct the backend"_

- Browse to: [http://localhost:8000/admin/sites/site/1/](http://localhost:8000/admin/sites/site/1/)
- Set the domain name and display name to the correct values for your site.
