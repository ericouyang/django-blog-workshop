# Workshop: Building a simple blog platform using Django 

In this short workshop, we'll be using [Django](https://www.djangoproject.com), an open-source web framework written in Python, to develop a simple blogging platform. 

Note that below `$` denotes what should be entered into the command prompt. Enter what follows it into the macOS Terminal or Windows Command Prompt. 

## Installation 

### macOS 

1. If you don't have a recent version of Python installed, first install the [Brew package manager](http://brew.sh/), which helps you manage dependencies on macOS.

2. Install necessary dependencies: 
  
  `$ brew install python && brew install sqlite`

3. Install `virtualenv` globally via pip, the Python package manager. This tool allows to create virtual environments to help make development more manageable. 

  `$ pip install virtualenv`

4. Create a new virtualenv named `blog` in a convenient location on your machine:

  `$ virtualenv blog`

5. Navigate into the created `blog` folder using `cd blog` and activate the virtualenv:

  `$ source bin/activate`
  
  You'll now see that your shell reflects the change by indicating `(blog)` at the beginning of your prompt

6. Install Django via pip:

  `$ pip install Django`

7. Create a new Django project: 

  `$ django-admin startproject myblog`

8. Navigate into the created `myblog` project folder using `cd myblog`

9. Set up the database by running the migrate tool: 

  `$ ./manage.py migrate`

  In your project folder, you'll see a file `db.sqlite3` where your SQLite database is located

10. Run the development server on port 8000

  `$ ./manage.py runserver`

11. Navigate in your browser to `http://localhost:8000`

12. (Optional) Install Visual Studio Code: https://code.visualstudio.com/docs/setup/mac

### Windows

1. If you don't have a recent version of Python install, first install the [Chocolatey package manager](https://chocolatey.org), which helps you manage dependencies on Windows. 

2. Install necessary dependencies: 
  
  `$ choco install python sqlite`

3. Install `virtualenv` globally via pip, the Python package manager. This tool allows to create virtual environments to help make development more manageable. 

  `$ pip install virtualenv`

4. Create a new virtualenv named `blog` in a convenient location on your machine:

  `$ virtualenv blog`

5. Navigate into the created `blog` folder using `cd blog` and activate the virtualenv:

  `$ Scripts\activate`
  
  You'll now see that your shell reflects the change by indicating `(blog)` at the beginning of your prompt

6. Install Django via pip:

  `$ pip install Django`
  
7. Create a new Django project: 

  `$ django-admin startproject myblog`

8. Navigate into the created `myblog` project folder using `cd myblog`

9. Set up the database by running the migrate tool: 

  `$ python manage.py migrate`
  
  In your project folder, you'll see a file `db.sqlite3` where your SQLite database is located

10. Run the development server on port 8000

  `$ python manage.py runserver`

11. Navigate in your browser to `http://localhost:8000`

12. (Optional) Install Visual Studio Code: https://code.visualstudio.com/docs/setup/windows

## Hello World!

1. First, let's create a new app: 

  `$ python manage.py startapp posts`
  
2. In the newly created `posts/views.py` file, include the following code: 

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world!")
```

3. Create a new file at `posts/urls.py`, and include the following code: 

```python
from django.conf.urls import url

from views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]
```

4. Now, we need to link up the project and the application urls. Update your `myblog/urls.py` file with the following code: 

```python
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^posts/', include('posts.urls')),
    url(r'^admin/', admin.site.urls),
]
```

5. Now, we're going to create our `Posts` model. In `posts/models.py`, include the following code: 

```python
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    # timestamps
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
```

6. Our project needs to be aware of our new model. To do this, we add our application to `myblog/settings.py`. At the bottom of `INSTALLED_APPS`, include the new application's configuration, so it looks like this:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts.apps.PostsConfig'
]
```

7. Now, we create a new migration to reflect changes in our model: 

  `$ python manage.py makemigrations`

8. Apply the changes to our database: 

  `$ python manage.py migrate`
  
## Creating your first views 

1. Update `posts/views.py` with the following code:

```python 
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    template_name = 'posts/post_list.html'
    model = Post
```

2. Create a new template at `posts/templates/posts/post_list.html`:

```html
<h1>My blog</h1>
{% if post_list %}
    {% for post in post_list %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
        <p><small>Posted: {{ post.created }}</small></p>
        <hr/>
    {% endfor %}
{% else %}
    <p>No posts...yet!</p>
{% endif %}
```

3. Update `urlpatterns` in `posts/urls.py`, replacing the `index` method we had tested earlier to create "Hello World" 

```python
from django.conf.urls import url

from views import PostListView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post-list'),
]
```

## Leveraging the built-in admin system

1. First, we need to make the admin system aware of our new model so that we can make changes to it, such as adding, deleting, and editing posts. Add the following code to `posts/admin.py`:

```python
from django.contrib import admin

from .models import Post

admin.site.register(Post)
```

2. Create a new superuser to accesss the backend by following the prompts after running:

  `$ python manage.py createsuperuser`
  
3. Visit your new admin system at `http://localhost:8000/admin` to create new blog posts. 

## Next steps 

Now you have a basic functioning system! You may want to explore setting up a `DetailView` for displaying single posts (we've implemented this in this repository--see `posts/views.py`), customizing the admin system, and how you can better style your pages (e.g. using [Twitter Bootstrap](https://getbootstrap.com))

