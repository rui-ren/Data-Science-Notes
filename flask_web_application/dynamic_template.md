
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


```
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

@app.route("/")
def homepage():
    "view function for Home Page"
    return render_template("home.html", pets = pets)

@app.route("/about")
def about():
    "view function for About Page"
    return render_template("about.html")
    
@app.route("/")
def homepage():
    "view function for home page"
    return render_template("home.html", pets = pets)
    
@app.route("/about")
def about():
    "view function for About Page"
    return render_template("about.html")

# dynamic template for the cats
@app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    """view function for showing details of each pet"""
    pet = next((pet for pet in pets if pet["id"] == pet_id), None)
    if pet is None:
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet = pet)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", post=3000)
```

