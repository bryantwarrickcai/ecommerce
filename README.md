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

## Answer to Questions for Assignment 4

---

**Question: What is the difference between `HttpResponseRedirect()` and `redirect()`?**

Answer: `HttpResponseRedirect` is a class, and it requires you to provide the URL to which you want to redirect the user. On the other hand, `redirect` is a function, and can be more flexible. With `redirect`, it can take a variety of arguments other than a URL, such as a view name or a model instance.

---

**Question: Explain how the `MoodEntry` model is linked with `User`!**

Answer: The `Product` model has a foreign key to connect to the username of the logged in user, stored in the built-in `User` model. With this way, each object also has a user associated to it, so that users can only see the items they have added to the database, not other users' items.

---

**Question: What is the difference between *authentication* and *authorization*, and what happens when a user logs in? Explain how Django implements these two concepts.**

Answer: Authentication is the process of verifying the identity of the user on a system. Authorization is the process of determining the actions that an authenticated user are allowed to perform. Authorization ensures that users can only have access to the actions that they are permitted to.

When a user logs in, they submit their credentials (username and password). The server then checks these credentials with their database. If the credentials are valid, the user is authenticated, and the system establishes a session for the user, which stores the user's identity. This session allows the user to remain logged in, so that users don't need to enter their details every time for every page they visit. The system then checks for the user's permissions (authorization) for the actions they are allowed to do, to ensure that they don't access restricted areas or perform restricted actions.

Django has a built-in `User` model which represents each user in the system. This model contains fields such as username and password. Django provides the built-in functions to handle user authentication (logging in and out). Authorization in Django is handled through their permission system. Permissions can be created through models, and can be checked using methods like `user.has_perm()`. Django also provides groups, which can contain a collection of permissions that can be assigned to users.

---

**Question: How does Django remember logged-in users? Explain other uses of *cookies* and whether all cookies are safe to use.**

Answer: Django remembers logged-in users by using session cookies. When a user logs in, Django generates a session key, which is associated with the user's information and settings. This session cookie is sent to the user's browser. On subsequent requests, the browser sends the cookie back to the server, which allows Django to recognize the logged-in user.

Cookies are used in many things other than remembering logged-in users. They can store user preferences (such as language settings or theme choices), using a "persistent login" (remember me) feature, to allow users to keep logged in across different sessions, and can also be used for tracking user behavior and analytics.

---

**Question: Explain how did you implement the checklist *step-by-step* (apart from following the tutorial).**

Answer:

1. First, one the `views.py` file on the `main` directory, I added the following imports:
```
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
2. I added a new `register` function on `views.py`. This function is used to create a user account when the form is submitted. The function is as follows:
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
3. In the `main/templates` directory, I created a new HTML file named `register.html`. I filled it with the following content:
```
{% extends 'base.html' %} {% block meta %}
<title>Register</title>
{% endblock meta %} {% block content %}

<div class="login">
    <h1>Register</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input type="submit" name="submit" value="Register" /></td>
            </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
</div>

{% endblock content %}
```
4. On the `urls.py` file inside the `main` directory, I imported the `register` function from `main.views`.
5. On the same file, I added a new path to `urlpatterns`: `path('register/', register, name='register')`.
6. On the `views.py` file inside the `main` directory, I imported `AuthenticationForm` from `django.contrib.auth.forms` and also imported `authenticate` and `login` from `django.contrib.auth`.
7. Still on `views.py`, I created a new function called `login_user`, which is used to authenticate users when they log in. Content is as follows:
```
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```
8. In the `main/templates` directory, I created a new HTML file named `login.html`. I filled it with:
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %} Don't have an account yet?
    <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
9. Inside the `urls.py` file inside the `main` directory, I imported the `login_user` function from `main.views`.
10. I added a new URL path to `urlpatterns` inside the `urls.py` file: `path('login/', login_user, name='login')`
11. On the `views.py` file in the `main` directory, I imported `logout` from `django.contrib.auth`.
12. I added a new function inside the `views.py` file called `logout_user`, which is used to log the user out.
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
13. On the `main.html` file in the `main/templates` directory, I added a new "Logout" button at the end of the file.
```
<a href="{% url 'main:logout' %}">
    <button>Logout</button>
</a>
```
14. On the `urls.py` file, I imported the `logout_user` function that I just created on `views.py`.
15. I added `logout` as a new URL path.
16. On the `views.py` file, I imported `login_required` from `django.contrib.auth.decorators`.
17. I added a decorator of `@login_required(login_url='/login')` above the `show_main` function.
18. On the `views.py` file, I imported `datetime`, `HttpResponseRedirect` from `django.http`, and `reverse` from `django.urls`.
19. I updated the `login_user` function in `views.py` to set a cookie of the last login date and time. The result is as follows:
```
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```
20. In the `show_main` function, I added a new key in the `context` variable named `last_login`, which has the value of `request.COOKIES["last_login"]`.
21. I modified the `logout_user` function to also delete the `last_login` cookie. Final result:
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
22. I added a new line inside the `main.html` file to show the last login data:
```
<h5>Last login session: {{ last_login }}</h5>
```
23. On the `models.py` file in the `main` directory, I added a new import: `from django.contrib.auth.models import User`
24. I added a new attribute to the `Product` entity, titled `user`, to identify the user in which each object belongs to. The new attribute is as follows:
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
25. I modified the `create_product` function inside `views.py` to be as follows:
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
```
26. In the `show_main` function, I modified the `products` variable to be `products = Product.objects.filter(user=request.user)` so that it only shows the products added by the logged-in user.
27. I also modified the `name` key in the `context` variable to be `request.user.username`.
28. I ran a model migration using `python manage.py makemigrations`.
29. I entered `1` twice during both prompts.
30. I ran `python manage.py migrate` to apply the migration in the previous step.
31. I ensured that my project is ready for a production environment. I added `import os` in the `settings.py` file on the `e_commerce` directory.
32. In the same file, I changed the variable `DEBUG` to this:
```
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```

---

## Answer to Questions for Assignment 5

---

**Question: If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!**

Answer: The order of priority for CSS selectors are as follows:

* Inline styles (using `style="..."` inside a tag)
* IDs
* Classes, attributes, and pseudo-classes
* Elements and pseudo-elements
* Source order

---

**Question: Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!**

Answer: Responsive design is an important concept because there is a huge diversity of devices that are used for accessing web applications, such as mobile phones, tablets, and desktops. Responsive design ensures that the webpage looks visually appealing and usable across all screen sizes and resolutions. With responsive design, it ensures a better viewing experience, reducing the need of zooming or scrolling. Most web applications nowadays do feature responsive design, such as Google, Microsoft, YouTube, Facebook, and so much more. However, some applications might not feature responsive design, such as older government websites, legacy e-commerce sites, or desktop-only applications.

---

**Question: Explain the differences between margin, border, and padding, and how to implement these three things!**

Answer: Padding is the space between the content of an element and the border. To implement padding in CSS, one uses the `padding` property to apply the margin on all four sides, or use `padding-top`, `padding-bottom`, `padding-left`, and `padding-right` for individual margins.

Border is a line that surrounds an element. The line can be styled and have different colors. The line can also be invisible. Borders can be applied to all sides or for each side individually. To implement a border, use the `border` property with the parameter being `<width> <style> <color>` as such:

```
border: 3px solid black
```

Individual borders can be applied using `border-top`, `border-bottom`, `border-left`, and `border-right`.

Margin is the space between the border of an element and other elements. The margin creates a distance between the element and adjacent elements.

To set a margin, use the `margin` property to apply the margin on all sides, or to apply different margins for individual sides, use the `margin-top`, `margin-bottom`, `margin-left`, and `margin-right` properties.

Here is an image demonstrating the differences:

![Margin, border, and padding order](margin_border_padding.png)

---

**Question: Explain the concepts of flex box and grid layout along with their uses!**

Answer: The flexbox (flexible box) layout is a one-dimensional layout, meaning that each item is aligned either horizontally or vertically (either rows or columns, but not both). Flex layouts are often used in navigation bars, card layouts (such as product listings), and form layouts. The grid layout is a two-dimensional layout, meaning that each item is aligned in a grid. This layout uses both rows and columns. The grid layout is often used for image galleries, multi-column layouts, list of results, and many more. In the grid layout, an item can take more than one grid space at once.

---

**Question: Explain how you implemented the checklist above step-by-step (not just following the tutorial)!**

Answer:

1. I created a new function titled `edit_product` inside the `views.py` file. This function is used to edit the details of a product. The function's content is as follows:
```
def edit_product(request, id):
    product = Product.objects.get(pk=id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```
2. I created a new file named `edit_product.html` in the `main/templates` directory. I filled it with the following:
```
{% extends 'base.html' %}
{% load static %}
{% block content %}
<h1>Edit Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Product"/>
            </td>
        </tr>
    </table>
</form>
{% endblock %}
```
3. On the `urls.py` file inside the `main` directory, I imported the `edit_product` function from `main.views` I just created.
4. I added `edit_product` as a new URL in the URL patterns: `path('edit-product/<uuid:id>', edit_product, name='edit_product')`
5. On the `main.html` page in the `main/templates` subdirectory, I added an "Edit" button on each table row. I added a new column with the following content:
```
<td>
    <a href="{% url 'main:edit_product' product.pk %}">
        <button>
            Edit
        </button>
    </a>
</td>
```
6. I created a new function titled `delete_product` inside the `views.py` file. This function is used to delete a product. The contents are as follows:
```
def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
7. On `urls.py`, I imported the `delete_product` function I just created.
8. I added a new URL pattern: `path('delete/<uuid:id>', delete_product, name='delete_product')`
9. On the `main.html` page, I added a "Delete" button on each table row. I added a new column:
```
<td>
    <a href="{% url 'main:delete_product' product.pk %}">
        <button>
            Delete
        </button>
    </a>
</td>
```
10. On the `base.html` page inside the `templates` folder on the root directory, I imported Tailwind using CDN. I modified the `<head>` part of the file to be like this:
```
<head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% endblock meta %}
    <script src="https://cdn.tailwindcss.com"></script>
</head>
```
11. In the `templates` folder of the root directory, I created a new file named `navbar.html`. This file is used for the navigation bar used in every webpage of the application.
12. I added a link to the navbar in `main.html`, `create_product.html`, `login.html`, `register.html`, and `edit_product.html`, by adding `{% include 'navbar.html' %}` in each of these files.
13. I created a new folder in the root directory titled `static`.
14. I created a new folder inside the `static` directory titled `css`.
15. Inside the `css` folder, I created a new file titled `global.css`. I filled it with:
```
.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
}
.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #3b82f6;
    box-shadow: 0 0 0 3px #3b82f6;
}
@keyframes shine {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}
.animate-shine {
    background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
    background-size: 200% 100%;
    animation: shine 3s infinite;
}
```
16. I added `global.css` to `base.html`.
17. I added some styling to the `login.html` and `register.html` pages.
18. I added a new file called `card_info.html` inside `main/templates`. This is used to display a card for the NPM, name, and class.
19. I added a new file called `card_product.html` so that it uses a card to display information for each product.
20. I modified the `main.html` page to use CSS styling.
21. I modified the `create_product.html` and `edit_product.html` pages to add CSS styling.
22. I configured the `STATIC_URL`, `STATICFILES_DIRS`, and `STATIC_ROOT` variables inside `settings.py`.

---

## Answer to Questions for Assignment 6

---

**Question: Explain the benefits of using JavaScript in developing web applications!**

Answer: JavaScript plays a crucial role in developing modern web applications today. One of the primary advantages of JavaScript is the ability to create interactive and dynamic user interfaces. JavaScript allows websites to update content and apply animations without requiring a refresh of the page. JavaScript was originally a client-side language, but the invention of Node.js allows using JavaScript for server-side development as well, allowing developers to use a single language for both the frontend and backend. JavaScript is supported by all modern browsers without needing to install additional plugins or tools. JavaScript also supports asynchronous programming, which allows running multiple tasks simultaneously without needing one task to finish first.

---

**Explain why we need to use `await` when we call `fetch()`! What would happen if we don't use `await`?**

Answer: The `fetch` function is an asynchronous function, meaning that it returns a promise, which will be resolved with the response data when it's available. Using `await` allows you to write asynchronous code that looks and behaves like synchronous code. When you need to perform multiple asynchronous operations in a specific order, using `await` will ensure that each operation is completed before moving on to the next one. If you don't use `await`, the rest of the code will keep executiing even when the promise is unresolved. Since the code execution doesn't wait for the fetch to complete, the code might be trying to access data that hasn't been fetched yet, leading to unexpected behaviors or errors.

---

**Why do we need to use the `csrf_exempt` decorator on the view used for AJAX `POST`?**

Answer: Django usees CSRF tokens to ensure that the request originated from the user's browser and is not from a malicious site. Every time a form is rendered, a unique CSRF token is generated and sent to the client. This token must be included in the AJAX request when submitting forms. Our AJAX request is not including a CSRF token, so we need to add the `@csrf_exempt` decorator to bypass the CSRF validation. However, using this introduces potential security risks, so it's better to include the CSRF token with each request.

---

**On this week's tutorial, the user input sanitization is done in the back-end as well. Why can't the sanitization be done just in the front-end?**

Answer: If the sanitization is done only in the front-end, attackers may be able to bypass the front-end validation by making direct API calls to the server (such as using Postman). Users can also disable JavaScript in their browsers, which would render front-end validation ineffective. In summary, the back-end validation provides a backup check in case the data managed to somehow bypass through the front-end check.

---

**Explain how you implemented the checklist above step-by-step (not just following the tutorial)!**

Answer:

1. I added the following two imports to the `views.py` file in the `main` directory:
```
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
```
2. I created a new function inside the `views.py` file titled `add_product_ajax`. This function allows creating a new product using AJAX.
3. Inside the `urls.py` file, I imported the `add_product_ajax` function that I created before.
4. I added a new URL path inside `urls.py`: `path('create-ajax', add_product_ajax, name='add_product_ajax')`
5. In the `views.py` file, I removed two lines: `products = Product.objects.filter(user=request.user)` and `"products": products,`.
6. In the `views.py` file, on the `show_xml` and `show_json` functions, I changed the first line to: `data = Product.objects.filter(user=request.user)`, so that it only displays data by the logged in user rather than all users.
7. I removed this code snippet in the `main.html` file (the code used to display the cards):
```
{% if not products %}
<div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
    <img src="{% static 'image/very-sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
    <p class="text-center text-gray-600 mt-4">There are no products in BryShop.</p>
</div>
{% else %}
<div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
    {% for product in products %}
        {% include 'card_product.html' with product=product %}
    {% endfor %}
</div>
{% endif %}
```
8. I replaced that code snippet I removed with:
```
<div id="product_cards"></div>
```
9. I added a new `<script>` block at the very bottom of the file (before the `{% endblock content %}`). It goes as follows:
```
<script>
    async function getProducts() {
        return fetch("{% url 'main:show_json' %}").then((res) => res.json());
    }
</script>
```
10. I added a new async function called `refreshProducts` inside the `main.html` file. The function goes as follows:
```
async function refreshProducts() {
    document.getElementById("product_cards").innerHTML = "";
    document.getElementById("product_cards").className = "";
    const products = await getProducts();
    let htmlString = "";
    let classNameString = "";

    if (products.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/very-sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">There are no products in BryShop.</p>
            </div>
        `;
    }
    else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
        products.forEach((product) => {
            htmlString += `
                <div class="relative break-inside-avoid">
                    <div class="relative top-5 bg-sky-100 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-sky-300">
                        <div class="bg-sky-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-sky-300">
                            <h3 class="font-bold text-black text-xl mb-2">${product.fields.name}</h3>
                        </div>
                        <div class="p-4">
                            <h5 class="text-black mb-2 text-xl">Price: ${product.fields.price}</h5>
                            <p class="text-gray-600 mb-2">${product.fields.description}</p>
                        </div>
                    </div>
                    <div class="absolute top-0 -right-4 flex space-x-1">
                        <a href="/edit-product/${product.pk}" class="bg-green-400 hover:bg-green-500 text-white rounded-full p-2 shadow-md">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                                <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                            </svg>
                        </a>
                        <a href="/delete/${product.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 shadow-md">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                            </svg>
                        </a>
                    </div>
                </div>
            `;
        });
    }
    document.getElementById("product_cards").className = classNameString;
    document.getElementById("product_cards").innerHTML = htmlString;
}

refreshProducts();
```
11. I added a new crud modal ID below the `product_cards` div inside the `main.html` file:
```
<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
    <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
        <!-- Modal header -->
        <div class="flex items-center justify-between p-4 border-b rounded-t">
            <h3 class="text-xl font-semibold text-gray-900">
                Add New Product
            </h3>
            <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                </svg>
                <span class="sr-only">Close modal</span>
            </button>
        </div>
        <!-- Modal body -->
        <div class="px-6 py-4 space-y-6 form-style">
            <form id="productForm">
                <div class="mb-4">
                    <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                    <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-sky-500" required>
                </div>
                <div class="mb-4">
                    <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
                    <input type="number" id="price" name="price" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-sky-500" required>
                </div>
                <div class="mb-4">
                    <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                    <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-sky-500" required></textarea>
                </div>
            </form>
        </div>
        <!-- Modal footer -->
        <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
            <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
            <button type="submit" id="submitProduct" form="productForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
        </div>
    </div>
</div>
```
12. I added a new this code at the very bottom inside the `<script>` tag:
```
const modal = document.getElementById('crudModal');
const modalContent = document.getElementById('crudModalContent');

function showModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modal.classList.remove('hidden'); 
    setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
    }, 50);
}

function hideModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modalContent.classList.remove('opacity-100', 'scale-100');
    modalContent.classList.add('opacity-0', 'scale-95');

    setTimeout(() => {
        modal.classList.add('hidden');
    }, 150);
}

document.getElementById("cancelButton").addEventListener("click", hideModal);
document.getElementById("closeModalBtn").addEventListener("click", hideModal);
```
13. I added a new button in the HTML page to add a new product by AJAX.
14. I added a function called `addProduct` at the beginning of the `<script>` tag. Content is as follows:
```
function addProduct() {
    fetch("{% url 'main:add_product_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#productForm')),
    })
    .then(response => refreshProducts())

    document.getElementById("productForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
}
```
15. I added the following at the end of the code:
```
document.getElementById("productForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addProduct();
    hideModal();
});
```
16. The next steps help prevent XSS (cross-site scripting). First I imported `strip_tags` from `django.utils.html` in both `views.py` and `forms.py`.
17. In the `views.py` file, inside the `add_product_ajax` function, I used `strip_tags` for the `name` and `description` variables. The code is modified to this:
```
@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    user = request.user

    new_product = Product(name=name, price=price, description=description, user=user)
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
```
18. In the `forms.py` file, I added new methods in the `ProductForm` class to strip HTML tags from the fields.
19. In the `main.html` file, in the `meta` block, I added the following script: `<script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>`
20. In the `main.html` file in the `refreshProducts` function I created earlier, I added `DOMPurify.sanitize` for `name` and `description`.

---
