
## Jinja Template engine

* Delimiters

1. `{% ... %}` use for statements
2. `{{ ... }}` use for variables
3. `{# ... #}` use for comments
4. `# .. ##` use for line statements

```
return render_template("index.html", my_object=object)
```
The value of this object is then fetched inside the template using `{{}}` syntax.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Jinja2 Demo</title>
</head>
<body>
    <h3>Username:</h3>
    <p>
        {{username}}
    </p>
</body>
</html>
```

```
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    Users = {
        "Archie": "Amsterdam",
        "Veronic": "London",
        "Betty": "San Francisco",
        "Jughead": "Los Angeles"
    }
    return render_template("index.html", users=Users)
```
```
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title> Jinja2 Demo </title>
</head>
<body>
    <h3>Betty lives in:</h3>
    <p>
        {{users["Betty"]}}
    </p>
</body>
</html>
```

## Control flow

the syntax of `for` loops in Jinja is very similar to pythonic syntax

### Loops
```
{% for elements in array %}
    ...
{% endfor %}
```

```
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Jinja2 Demo</title>
</head>
<body>
    <table style="width:100%; text-align:center">
    <tr>
        <th>Index</th>
        <th>Username</th>
        <th>Location</th>
    </tr>
    {% for username, location in users.items() %}
    <tr>
        <td>{{loop.index}}</td>
        <td>{{username}}</td>
        <td>{{location}}</td>
    </tr>
    {% endfor %}
</table>
</body>
</html>
```

### Conditionals
```
{% if true %}
{% endif %}

{% if ... %}
{% elif ...%}
{% else %}
{% endif %}
```

### Template inheritance
* Jinja provides us a way to avoid rewriting .css file




