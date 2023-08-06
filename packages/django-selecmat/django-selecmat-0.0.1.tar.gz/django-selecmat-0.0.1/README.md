# Selecmat
MaterializeCSS + Selectize.js for Django Form

A simple Django template tag to work with [Materializecss](http://materializecss.com/) and [Selectize.js](https://selectize.github.io/selectize.js/)





## Install


```
pip install  django-selecmat

```



[on pypi](https://pypi.python.org/pypi/django-selecmat)
[on GitHub](https://github.com/dwjorgeb/django-selecmat)

Add to INSTALLED_APPS:

```
INSTALLED_APPS = (
     'selecmat',
     ...
     )
```

Add MaterializeCSS and Selectize to your project:

In your base.html:

```
<head>

{% block css %}
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css">

  <link type="text/css" rel="stylesheet" href="{% static 'css/selectize.css' %}" media="screen,projection"/>

{% endblock css %}

</head>
```

```

  <body >

  {% block javascript %}
  <script
    src="https://code.jquery.com/jquery-3.3.1.min.js"
    integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
    crossorigin="anonymous"></script>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/js/materialize.min.js"></script>
  <script type="text/javascript" src="{% static 'js/selectize.min.js' %}"></script>

  <script>
  $(document).ready(function(){

    // Initialize materialize data picker
    $('.datepicker').datepicker({'format': 'yyyy-mm-dd'});
    $('select').selectize();

  });

  </script>

  {% endblock javascript %}



  ...

  </body>
```

## Usage

Use it like this, simple.

{% load selecmat %}

### All the form

{{ form|selecmat }}

### Individual field

{{ form.<<field name>> | selecmat }}


### Custom size (default is 's12')

{{ form|selecmat:'m6' }}


### Icons support
This is most useful for adding a descriptive icon when you are creating a custom layout by building the form one field at a time. Substitue FIELD_NAME below with one of the field names from your form.
```html
{{ form.FIELD_NAME|selecmat:'s12 m6, icon=person' }}
{{ form.FIELD_NAME|selecmat:'custom_size=s12 m6, icon=person' }}
```

## Demo

![Basic form](https://cloud.githubusercontent.com/assets/3958123/6165004/a1984f52-b2a4-11e4-8ae2-078505991b0d.png)

![DatePicker](https://cloud.githubusercontent.com/assets/3958123/6165005/a19bf044-b2a4-11e4-9989-6a64f9c97087.png)


## Help

### Widget

- TextInput
- Textarea
- CheckboxInput
- RadioSelect
- Select
- SelectMultiple
- CheckboxSelectMultiple
- Filefield
- DateField
- DateTimeField (doesn't show time yet)



## Inspired by

[django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form)

## Originally Built By

Florent CLAPIÉ

[https://pypi.org/user/florent1933/](https://pypi.org/user/florent1933/)

## Adapted from 

[django-materialize-form](https://github.com/kalwalkden/django-materializecss-form)