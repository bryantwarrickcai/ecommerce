# E-Commerce Application (BryShop) - PBP Assignment 2 and 3

[Link to PWS application](http://bryant-warrick-ecommerce.pbp.cs.ui.ac.id/)

## Answer to Questions for Assignment 2

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
6. I added `"localhost"`, `"127.0.0.1"`, and `"bryant-warrick-ecommerce.pbp.cs.ui.ac.id"` in the `ALLOWED_HOSTS` on `settings.py`.
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
12. Inside the `urls.py` of the `e_commerce` directory (not the `main` directory), I imported using `from django.urls import path, include`. After that, I added the following URL route in the `urlpatterns` variable: `path('', include('main.urls'))`
13. Creating the model: In the `models.py` file in the `main` directory, I filled it with the following code:
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
```
14. I performed a model migration by running `python manage.py makemigrations` and `python manage.py migrate`.
15. In the `views.py` file inside the `main` directory, I filled it with the following code:
```
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        "appname": "BryShop",
        "name": "Bryant Warrick Cai",
        "npm": "2306256255",
        "class": "KKI"
    }

    return render(request, "main.html", context)
```
16. I created a new file named `main.html` in the `templates` directory of the `main` directory. I filled it with:
```
<!DOCTYPE html>
<head>
    <title>BryShop</title>
</head>
<body>
    <h1>Welcome to {{ appname }}!</h1>
    <h3>Name:</h3>
    <p>{{ name }}</p>
    <h3>NPM:</h3>
    <p>{{ npm }}</p>
    <h3>Class:</h3>
    <p>{{ class }}</p>
</body>
```
17. I performed a deployment to PWS by creating a new project in PWS named `ecommerce`.
18. I pushed my project to PWS using `git push pws main:master`.

---

**Question: Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between `urls.py`, `views.py`, `models.py`, and the `html` file.**

Answer:

<img src="diagram.png" alt="Diagram" width="800">

In Django, `urls.py` maps the URLS to functions or class-based views. When a user access a specific URL, Django checks to determine which view should process the request. `views.py` provides logic that handles the request. It can process requests, retrieve data from models, and renders the response using HTML (template) files. `models.py` defines the structure of the database using Django's ORM. The HTML template is used to define the structure and design that the end-users see. Templates can be inserted in HTML files, which uses `views.py` to fill in the templates.

---

**Question: Explain the use of git in software development!**

Answer: Git is a version control system that can be used to track changes in code and files over time. Git is very heavily used in software development, as it stores a complete history of all the changes in the project, allowing developers to review and revert the codebase. Git allows collaboration on projects, and provides detailed logs for who made the specific changes, when, and why.

Git also enables developers to create branches, for separate lines of development. This allows testing and working on new features and bug fixes without affecting the main codebase. Once work on a branch is complete, the code can be merged back into the main branch. Code in Git can be stored in a remote repository (such as GitHub), where other collaborators can pull these changes to their local devices.

---

**Question: In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?**

Answer: Django provides a comprehensive framework that simplifies many aspects of building web applications. Django already provides everything needed to build a web application out of the box, such as database management, user authentication, form handling, and URL routing. By learning Django, beginners can learn about both the frontend and backend aspects of web development. Django is also built in Python, which is usually considered a great programming language for beginners.

---

**Question: Why is the Django model called an ORM?**

Answer: ORM stands for Object-Relational Mapper. A Django model is called an ORM because it provides a way to interact with relational databases using object-oriented programming. ORM allows mapping Python objects (like Django models) to database tables.

---

## Answer to Questions for Assignment 3

---

**Question: Explain why we need data delivery in implementing a platform.**

Answer: Data delivery ensures that users can interact and receive content and information from the system. Data delivery enables dynamic content, maintains data consistency, and ensures secure transmission of the data. It also allows integration with external services to provide users with feedback and error handling, making the platform reliable and user-friendly.

---

**Question: In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?**

Answer: In my opinion, I think JSON is better. JSON has a simpler and more human-readable structure than XML. JSON uses key-value pairs, whereas XML uses opening and closing tags with the data inside the tags. JSON format is more compact which leads to smaller file sizes. Parsing JSON is also faster due to its simple structure. JSON is also natively supported by JavaScript and many other programming languages.

---

**Question: Explain the functional usage of `is_valid()` method in Django forms. Also explain why we need the method in forms.**

Answer: In Django, the `is_valid()` method is used to check if the data submitted to the form adheres to the rules and constraints implemented by the form, such as field types, field length, and custom validation logic. In other words, `is_valid()` validates the data entered into the form. `is_valid()` is crucial because without it, there can be invalid or malicious data entered that bypasses these constraints, which may lead to errors or security vulnerabilities.

---

**Question: Why do we need `csrf_token` when creating a form in Django? What could happen if we did not use `csrf_token` on a Django form? How could this be leveraged by an attacker?**

Answer: The `csrf_token` in Django forms is an essential security feature to prevent CSRF (Cross-Site Request Forgery) attacks. This token is included in every form submission to ensure that a form submission is coming from a legitimate user, rather than by an attacker. Without this token, malicious websites can trick legitimate users to unknowingly submit requests to the legitimate website. (The malicious website has a script to submit a request to the legitimate website.)

---

**Question: Explain how you implemented the *checklist* above step-by-step (not just following the tutorial).**

Answer:

1. First I created a new directory named `templates` inside the root directory. Inside the `templates` folder, I created a new file named `base.html`. I filled it with the following content:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {% block meta %} {% endblock meta %}
    </head>

    <body>
        {% block content %} {% endblock content %}
    </body>
</html>
```
2. Inside the `settings.py` file in the `e_commerce` directory, in the `TEMPLATES` variable, I modified the `dirs` to be `[BASE_DIR / 'templates']`.
3. I also made sure that the value of `APP_DIRS` is `True`.
4. I modified the `models.py` file in the `main` directory to import `uuid` and use a new UUID field, named `id` as the primary key of the object.
5. I did a model migration by running `python manage.py makemigrations` and `python manage.py migrate`.
6. I created a new file named `forms.py` in the `main` directory. I filled it with the following:
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```
7. I changed the contents of the `views.py` file in the `main` directory to:
```
from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    context = {
        "appname": "BryShop",
        "name": "Bryant Warrick Cai",
        "npm": "2306256255",
        "class": "KKI",
        "products": products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
```
8. Inside the `urls.py` file in the `main` directory, I changed the contents to:
```
from django.urls import path
from main.views import show_main, create_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
]
```
9. I created a new HTML file named `create_product.html` in the `main/templates` directory. I filled the file with:
```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product" />
        </td>
        </tr>
    </table>
</form>

{% endblock %}
```
10. I changed the contents of the `main.html` file inside the `templates` folder of the `main` directory to:
```
{% extends 'base.html' %}
{% block content %}
<!DOCTYPE html>
<head>
    <title>BryShop</title>
</head>
<body>
    <h1>Welcome to {{ appname }}!</h1>
    <h3>Name:</h3>
    <p>{{ name }}</p>
    <h3>NPM:</h3>
    <p>{{ npm }}</p>
    <h3>Class:</h3>
    <p>{{ class }}</p>

    {% if not products %}
    <p>There are no products in BryShop.</p>
    {% else %}
    <table>
        <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Description</th>
        </tr>

        {% comment %} This is how to display product data
        {% endcomment %} 
        {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}

    <br />

    <a href="{% url 'main:create_product' %}">
        <button>Add New Product</button>
    </a>
</body>
{% endblock content %}
```
11. On the `views.py` file inside the `main` directory, I added the following imports:
```
from django.http import HttpResponse
from django.core import serializers
```
12. I created a new function called `show_xml` in the `views.py` file, with the following content:
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
This allows viewing the data in XML.
13. I created a new function called `show_json` in the `views.py` file, with the following content:
```
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
This allows viewing the data in JSON.
14. On `urls.py`, I imported `show_xml` and `show_json` inside from `main.views`, and created two new URL paths: `path('xml/', show_xml, name='show_xml')` for XML and `path('json/', show_json, name='show_json')` for JSON.
15. I then created a new function called `show_xml_by_id` in `views.py` for showing XML data only for a specific UUID.
```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
16. I then created a new function called `show_json_by_id` in `views.py` for showing JSON data only for a specific UUID.
```
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
17. On `urls.py`, I imported `show_xml_by_id` and `show_json_by_id` inside from `main.views`, and created two new URL paths: `path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id')` for XML and `path('json/<str:id>/', show_json_by_id, name='show_json_by_id')` for JSON.

### Screenshots of Postman

![XML request](postman_xml.png)

![JSON request](postman_json.png)

![XML by ID request](postman_xml_id.png)

![JSON by ID request](postman_json_id.png)

---
