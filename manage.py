import settings
from django.core.management import execute_manager

if __name__ == "__main__":
    try:
        execute_manager(settings)
    except ImportError:
        import sys

        sys.stderr.write(
            '''
Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.
You'll have to run django-admin.py, passing it your settings module.
(If the file settings.py does indeed exist, it's causing an ImportError somehow.)
''' % __file__)
        sys.exit(1)
