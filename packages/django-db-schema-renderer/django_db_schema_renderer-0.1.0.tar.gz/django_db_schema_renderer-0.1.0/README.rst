=============================
django-db-schema-renderer app
=============================

App to draw db-schema of selected apps, models.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django-db-schema-renderer" to your INSTALLED_APPS setting like this::
    INSTALLED_APPS = [
        'django_db-schema_renderer',
        'django.contrib.admin',

    ]


2. Add app related urls to your root `urls.py`
    from django_db_schema_renderer.urls import schema_urls
    
    urlpatterns = [
    ...
    path("db-schema/", include((schema_urls, "db-schema"))),
    ...

    ]

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to render db-schema.

