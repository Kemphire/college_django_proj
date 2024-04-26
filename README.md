# Steps to setup on your local machine
- First clone the repo
- navigate to the project folder then run the following command to create virtual enviroment and subsequently run the default debug server
```python
python -m venv .venv
pip install -r requirements.txt
cd main_wrapper
python manage.py runserver
```
- if you followed the above steps then congratulation you have successfully ran my project locally and you have directory structure such like below

## Tree after cloning repo
```
.
├── main_wrapper
│   ├── blog
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── admin.cpython-310.pyc
│   │   │   ├── admin.cpython-311.pyc
│   │   │   ├── apps.cpython-310.pyc
│   │   │   ├── apps.cpython-311.pyc
│   │   │   ├── desktop.ini
│   │   │   ├── forms.cpython-310.pyc
│   │   │   ├── models.cpython-310.pyc
│   │   │   ├── models.cpython-311.pyc
│   │   │   ├── url.cpython-310.pyc
│   │   │   ├── url.cpython-311.pyc
│   │   │   ├── views.cpython-310.pyc
│   │   │   └── views.cpython-311.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── desktop.ini
│   │   ├── forms.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_post_contents.py
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── 0001_initial.cpython-310.pyc
│   │   │   │   ├── 0001_initial.cpython-311.pyc
│   │   │   │   ├── 0002_post_contents.cpython-310.pyc
│   │   │   │   ├── 0002_post_contents.cpython-311.pyc
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── __init__.cpython-311.pyc
│   │   │   │   └── desktop.ini
│   │   │   └── desktop.ini
│   │   ├── models.py
│   │   ├── static
│   │   │   ├── blog
│   │   │   │   ├── desktop.ini
│   │   │   │   └── main.css
│   │   │   └── desktop.ini
│   │   ├── templates
│   │   │   ├── blog
│   │   │   │   ├── about.html
│   │   │   │   ├── base.html
│   │   │   │   ├── desktop.ini
│   │   │   │   ├── home.html
│   │   │   │   ├── post_creation_form.html
│   │   │   │   ├── post_detail.html
│   │   │   │   ├── post_edit_form.html
│   │   │   │   └── profile_view.html
│   │   │   └── desktop.ini
│   │   ├── tests.py
│   │   ├── url.py
│   │   └── views.py
│   ├── corey_proj
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── desktop.ini
│   │   │   ├── settings.cpython-310.pyc
│   │   │   ├── settings.cpython-311.pyc
│   │   │   ├── urls.cpython-310.pyc
│   │   │   ├── urls.cpython-311.pyc
│   │   │   ├── wsgi.cpython-310.pyc
│   │   │   └── wsgi.cpython-311.pyc
│   │   ├── asgi.py
│   │   ├── desktop.ini
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── desktop.ini
│   ├── manage.py
│   ├── media
│   │   ├── default.jpg
│   │   ├── default.jpg:Zone.Identifier
│   │   └── profile_pics
│   │       ├── Kartikey_shahi_passport_photo-min.jpg
│   │       ├── Raj_photo.jpg
│   │       ├── ascii_htimonlee.jpg
│   │       ├── ascii_htimonlee.png
│   │       ├── ascii_htimonlee_I1PLldX.jpg
│   │       ├── ascii_htimonlee_JG2El4P.png
│   │       ├── ascii_htimonlee_NWteIwV.png
│   │       ├── ascii_htimonlee_T7G6bAt.png
│   │       ├── hadjf.jpg
│   │       ├── hitmonlee.jpg
│   │       ├── image-removebg-preview_3.png
│   │       └── images-removebg-preview.png
│   └── user_authentication
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-310.pyc
│       │   ├── __init__.cpython-311.pyc
│       │   ├── admin.cpython-310.pyc
│       │   ├── admin.cpython-311.pyc
│       │   ├── apps.cpython-310.pyc
│       │   ├── apps.cpython-311.pyc
│       │   ├── desktop.ini
│       │   ├── forms.cpython-310.pyc
│       │   ├── forms.cpython-311.pyc
│       │   ├── models.cpython-310.pyc
│       │   ├── models.cpython-311.pyc
│       │   ├── signals.cpython-310.pyc
│       │   ├── views.cpython-310.pyc
│       │   └── views.cpython-311.pyc
│       ├── admin.py
│       ├── apps.py
│       ├── desktop.ini
│       ├── forms.py
│       ├── migrations
│       │   ├── 0001_initial.py
│       │   ├── 0002_alter_profile_image.py
│       │   ├── 0003_alter_profile_image.py
│       │   ├── 0004_alter_profile_image.py
│       │   ├── 0005_alter_profile_bio.py
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   │   ├── 0001_initial.cpython-310.pyc
│       │   │   ├── 0002_alter_profile_image.cpython-310.pyc
│       │   │   ├── 0003_alter_profile_image.cpython-310.pyc
│       │   │   ├── 0004_alter_profile_image.cpython-310.pyc
│       │   │   ├── 0005_alter_profile_bio.cpython-310.pyc
│       │   │   ├── __init__.cpython-310.pyc
│       │   │   ├── __init__.cpython-311.pyc
│       │   │   └── desktop.ini
│       │   └── desktop.ini
│       ├── models.py
│       ├── signals.py
│       ├── templates
│       │   ├── desktop.ini
│       │   └── user_authentication
│       │       ├── desktop.ini
│       │       ├── login.html
│       │       ├── logout.html
│       │       ├── profile.html
│       │       └── register.html
│       ├── tests.py
│       └── views.py
└── requirements.txt
```
