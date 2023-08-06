=====
Rudra
=====

Rudra is a Django app for models. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "rudra" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'rudra',
    ]

2. Include the rudra URLconf in your project urls.py like this::

    path('rudra/', include('rudra.urls')),

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

4. Visit http://127.0.0.1:8000/rudra/ to participate in the poll.