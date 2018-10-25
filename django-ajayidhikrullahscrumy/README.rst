=====
myscrumy
=====

Myblog is a simple demo of Django's basic usage.

Quick start
-----------

1. Add "ajayidhikrullahscrumy" to INSTALLED_APPS:
  INSTALLED_APPS = {
    ...
    'ajayidhikrullahscrumy'
  }

2. Include the ajayidhikrullahscrumy URLconf in urls.py:
  url(r'^ajayidhikrullah/', include('ajayidhikrullahscrumy.urls'))

3. Run `python manage.py syncdb` to create myblog's models.

4. Run the development server and access http://127.0.0.1:8000/admin/ to
    manage blog posts.

5. Access http://127.0.0.1:8000/ajayidhikrullahscrumy/ to view a list of most recent posts.