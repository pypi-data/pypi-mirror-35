=======
COOLFIG
=======

.. image:: https://img.shields.io/travis/GaretJax/coolfig.svg
   :target: https://travis-ci.org/GaretJax/coolfig

.. image:: https://img.shields.io/pypi/v/coolfig.svg
   :target: https://pypi.python.org/pypi/coolfig

.. image:: https://img.shields.io/pypi/dm/coolfig.svg
   :target: https://pypi.python.org/pypi/coolfig

.. image:: https://img.shields.io/coveralls/GaretJax/coolfig/master.svg
   :target: https://coveralls.io/r/GaretJax/coolfig?branch=master

.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg
   :target: http://coolfig.readthedocs.org/en/latest/

.. image:: https://img.shields.io/pypi/l/coolfig.svg
   :target: https://github.com/GaretJax/coolfig/blob/develop/LICENSE

.. image:: https://img.shields.io/requires/github/GaretJax/coolfig.svg
   :target: https://requires.io/github/GaretJax/coolfig/requirements/?branch=master

.. .. image:: https://img.shields.io/codeclimate/github/GaretJax/coolfig.svg
..   :target: https://codeclimate.com/github/GaretJax/coolfig

Coolfig is a library to easily write configuration specifications to be
fulfilled by various sources.

* Free software: MIT license
* Documentation: http://coolfig.rtfd.org


Installation
============

::

  pip install coolfig


Example
=======

Define your schema:

.. code:: python

   from coolfig import Settings, Value, types

   class DefaultSettings(Settings):
        SECRET_KEY = Value(str)
        DEBUG = Value(types.boolean, default=False)
        DB_URL = Value(types.sqlalchemy_url)
        LOCALES = Value(types.list(str))

Instantiate the configuration with a data provider:

.. code:: python

   from coolfig import EnvConfig

   settings = DefaultSettings(EnvConfig(prefix='MYAPP_'))

Profit:

.. code:: python

   if settings.DEBUG:
       print(settings.SECRET_KEY)
   else:
       print(settings.LOCALES)

   connect(settings.DB_URL)


Django integration
==================

In your ``settings.py`` file:

.. code:: python

   from coolfig import EnvConfig, load_django_settings

   INSTALLED_APPS = (
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',

      'testprj.my_custom_app',
   )

   MIDDLEWARE_CLASSES = (
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
      'django.middleware.security.SecurityMiddleware',
   )

   ROOT_URLCONF = 'testprj.urls'

   WSGI_APPLICATION = 'testprj.wsgi.application'

   TEMPLATES = [
      {
         'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [],
         'APP_DIRS': True,
         'OPTIONS': {
               'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
               ],
         },
      },
   ]

   load_django_settings(EnvConfig(), locals())

Then, in each ``settings`` submodule of each app, you can define additional
setting entries to be added to the main settings object. For example, in 
``testprj/my_custom_app/settings.py`` you can add the following:

.. code:: python

   from coolfig import Settings, Value

   class AppSettings(Settings):  # The class has to be named AppSettings
      MY_APP_SETTING = Value(str)

Usage is 100% compatible with Django's settings machinery:

.. code:: python

   from django.conf import settings

   settings.MY_APP_SETTING


=======
History
=======


3.1.0 - 2018-08-23
==================

* Make ``EnvDirConfig`` importable from ``coolfig``.


3.0.0 - 2018-08-23
==================

* Removed explicit support for secrets in favor of ``EnvDirConfig`` and
  a ``FallbackProvider``.
* Use `black` and `isort` for formatting.
* Improved tests coverage


2.0.0 - 2018-08-03
==================

* Support for Docker secrets.


1.0.2 - 2016-03-14
==================

* Additional bug-fixing.


1.0.1 - 2016-03-14
==================

* Fixed a bug in AppConfig checking.


1.0.0 - 2016-03-14
==================

* Added support for Django ``AppConfig`` (including custom settings path
  configured with a ``settings`` property on the config class.
* Officially supporting Django 1.4, 1.5, 1.6, 1.7, 1.8 and 1.9, running on
  Python 2.7, 3.4 (where Django supports itself supports it) and PyPy.


0.4.0 - 2015-10-05
==================

* Added support for the CACHES Django settings directive
* Added support for computed_values
* Added initial documentation stub


0.3.0 - 2015-07-20
==================

* Added first-class support for Django
* Added some more importing shortcuts (``EnvConfig``, ``DictConfig``,
  ``load_django_settings``)
* Added a ``DictValue`` value, able to load multiple keys with the same prefix
  into the same value
* Added an API to merge different settings schema into an existing object


0.2.0 - 2015-05-31
==================

* Added a ``EnvConfig`` provider
* Added a ``dottedpath`` value type


0.1.0 – 2015-05-30
==================

* Initial release


