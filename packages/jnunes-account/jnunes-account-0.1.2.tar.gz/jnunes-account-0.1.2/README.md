# Commons Django Application

Commons User Accounts Application for registration, login, logout and reset password.

# Quick start

To use this project, install the last version available on
pypi [jnunes-accounts](https://pypi.org/project/jnunes-account/)
For package install, run ``pip install jnunes-account``. 

After install, configure your settings.py file, like this:

```python
INSTALLED_APPS = [
'account',
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles'
]
```

```python
After insta
from django.contrib.messages import constants
import environ
env = environ.Env()
environ.Env.read_env()
# Default URL settings
LOGIN_REDIRECT_URL = '/account/dummy'
LOGIN_URL = '/account/login/'
LOGOUT_REDIRECT_URL = '/account/login'
HOME_REDIRECT = '<<endereco da home page>>'
# SMTP Settings
EMAIL_HOST = env('DJGEMAIL_HOST')
EMAIL_PORT = env('DJGEMAIL_PORT')
EMAIL_HOST_USER = env('DJEMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('DJEMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
```
