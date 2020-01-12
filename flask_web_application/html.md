
## HTML in Flask

* static templates on the front-end using Flask framework

### Static templates

* render_template() function 
* File structure strategies for Flask

### Serve static files

* static file or assets are file are the files that server sends to the clients, without any intervention. e.g. css file and JavaScript

#### Steps to Static files
1. creat a `\static` directory

```
url_for('static', filename='borders.css')
```

* `url_for` generate the absolute path for the endpoint
