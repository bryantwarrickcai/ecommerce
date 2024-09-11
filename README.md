# E-Commerce Application (BryShop) - PBP Assignment 2

[Link to PWS application](http://bryant-warrick-ecommerce.pbp.cs.ui.ac.id/)

## Answer to Questions

---

**Question: Explain how you implemented the checklist above step-by-step (not just following the tutorial).**

Answer:

1. I created a virtual environment using the command `python -m venv env`.
2. I activate the virtual environment using the command `env\Scripts\activate`.
3. I created a `requirements.txt` file with the following content:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
4. Inside the virtual environment, I ran the command `pip install -r requirements.txt`.
5. I created the Django project using the command `django-admin startproject e_commerce .`.
6. I added `"localhost"` and `"127.0.0.1"` in the `ALLOWED_HOSTS` on `settings.py`.
7. I added a `".gitignore"` file.
8. I created the `main` application by running `python manage.py startapp main` while the virtual environment is active.
9. Inside the `settings.py` in the `e_commerce` directory, I added `'main'` to the `INSTALLED_APPS` variable.
10. For routing for the `main` application, I created a new file named `urls.py` in the `main` directory.
11. Inside `urls.py`, I pasted the following content:
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

---

**Question: Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between `urls.py`, `views.py`, `models.py`, and the `html` file.**

Answer:

---

**Explain the use of git in software development!**

Answer: Git is a version control system that can be used to track changes in code and files over time. Git is very heavily used in software development, as it stores a complete history of all the changes in the project, allowing developers to review and revert the codebase. Git allows collaboration on projects, and provides detailed logs for who made the specific changes, when, and why.

Git also enables developers to create branches, for separate lines of development. This allows testing and working on new features and bug fixes without affecting the main codebase. Once work on a branch is complete, the code can be merged back into the main branch. Code in Git can be stored in a remote repository (such as GitHub), where other collaborators can pull these changes to their local devices.

---

**In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?**

Answer: Django provides a comprehensive framework that simplifies many aspects of building web applications. Django already provides everything needed to build a web application out of the box, such as database management, user authentication, form handling, and URL routing. By learning Django, beginners can learn about both the frontend and backend aspects of web development. Django is also built in Python, which is usually considered a great programming language for beginners.

---

**Why is the Django model called an ORM?**

Answer: ORM stands for Object-Relational Mapper. A Django model is called an ORM because it provides a way to interact with relational databases using object-oriented programming. ORM allows mapping Python objects (like Django models) to database tables.

---
