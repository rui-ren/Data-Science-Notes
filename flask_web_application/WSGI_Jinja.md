
## WSGI and JinJa2

### Web Server Gataway Interface (WSGI)

* Flexibility
* Interoperability
* Scalability
* Efficiency

### Jinja template language


## Procedure for flask

1. Import modules
```
from flask import Flask
```

2. Creating a Flask object
```
app = Flask(__name__)
```
3. Run the application in main
```
if __name__ == "__main__":
    app.run()
```
4. Create view function
```
def hello():
    return "hello world";
```
5. Assign a URL route
```
@app.route("/")
def hello():
    return "Hello World";
```

### Routes
* static routing, the `rule` parameter of `route` decorator is simple string
* dynamic routing, the `rule` parameter is instead a `variable`.

```
@app.route('/square/<float:number>')
def show_square(number):
    return "Square of " + str(number) + "is:" + str(number * number)
```

* converter: String default, int, float, path, uuid

