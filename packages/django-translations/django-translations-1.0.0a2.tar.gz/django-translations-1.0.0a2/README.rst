Translations
============

.. image:: https://travis-ci.com/perplexionist/django-translations.svg?branch=master
    :target: https://travis-ci.com/perplexionist/django-translations

Translations app provides an *easy*, *efficient* and *modular* way of
translating django models.

Requirements
------------

* Python (>=3.5)
* Django (1.11, >=2.0)

Installation
------------

1. Install Translations using PIP (use ``--pre``, still in development):

   .. code:: bash

      $ pip install --pre django-translations

2. Add ``'translations'`` to ``INSTALLED_APPS`` in the settings of your Django
   project:

   .. code:: python

      INSTALLED_APPS += [
          'translations',
      ]

3. Run ``migrate``:

   .. code:: bash

      $ python manage.py migrate

4. Make sure django internationalization settings are set correctly:

   .. code:: python

      USE_I18N = True          # use internationalization
      USE_L10N = True          # use localization

      MIDDLEWARE += [          # locale middleware
          'django.middleware.locale.LocaleMiddleware',
      ]

      LANGUAGE_CODE = 'en-us'  # fallback language
      LANGUAGES = (            # supported languages
          ('en', 'English'), 
          ('de', 'German'),
      )

Basic Usage
-----------

Model
~~~~~

Inherit ``Translatable`` in any model you want translated:

.. code:: python

   from translations.models import Translatable

   class Continent(Translatable):
       ...

   class Country(Translatable):
       ...

   class City(Translatable):
       ...

**No Migrations** needed afterwards!

Query
~~~~~

Use the queryset extensions:

.. code:: python

   >>> continents = Continent.objects.prefetch_related(
   ...     'countries',
   ...     'countries__cities',
   ... ).apply_translations(
   ...     'countries',
   ...     'countries__cities',
   ...     lang='de'
   ... )
   >>> continents[0].name
   Europa
   >>> continents[0].countries.all()[0].name
   Deutschland

This does **Only One Query** for the queryset and relations translations!

Admin
~~~~~

Use the admin extensions:

.. code:: python

   from django.contrib import admin
   from translations.admin import TranslatableAdmin, TranslationInline

   from .models import Continent

   class ContinentAdmin(TranslatableAdmin):
       inlines = [TranslationInline,]

   admin.site.register(Continent, ContinentAdmin)

This provides admin inlines for the translations of the model.

Documentation
-------------

For more interesting capabilities browse through the `documentation`_.

.. _documentation: http://perplexionist.github.io/django-translations
