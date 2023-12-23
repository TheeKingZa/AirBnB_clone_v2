# AirBnB clone - Web framework
[#](https://github.com/TheeKingZa/AirBnB_clone_v2/tree/master/README.md) 0x04
---

# NEED TO KNOW?
* [What is a Web Framework](#what-is-a-web-framework)
* [How to build a web framework with Flask](#how-to-build-a-web-framework-with-flask)
* [How to define routes in Flask](#how-to-define-routes-in-flask)
* [What is a route](#what-is-a-route)
* [How to handle variables in a route](#how-to-handle-variables-in-a-route)
* [What is a template](#what-is-a-template)
* [How to create a HTML response in Flask by using a template](#create-an-html-response-in-flask-using-a-template)
* [How to create a dynamic template](#create-a-dynamic-template-loops-conditions) (loops, conditions…)
* [How to display in HTML data from a MySQL database](#display-data-from-a-mysql-database-in-html)
* [W3C Compliance And Validation](#overview)
* [W3C Validation](#w3c-validation)
* [What is W3C Validation](#what-is-w3c-validation)
* [How to Validate](#how-to-validate)
* [Badge](#badge)
* [Additional tips](#additional-tips)

---

# Web Framework Basics

Welcome to the Web Framework Basics project! This README.md provides an overview of essential concepts and steps to build a web framework using Flask.

## What is a Web Framework

**Web frameworks provide a structure and tools to facilitate web development. They offer predefined functions, libraries, and utilities to streamline the creation of web applications.**

## How to Build a Web Framework with Flask
**To build a web framework using Flask, follow these steps:**
```
1. Install Flask using pip: `pip install Flask`
2. Create a Python file for your application.
3. Import Flask and define your app: 

    python

    ```
    from flask import Flask
    app = Flask(__name__)
    ```
4. Define routes using the `@app.route` decorator and corresponding functions to handle them.
5. Run the app: `if __name__ == "__main__": app.run()`
6. Expand functionality by adding templates, handling routes, and integrating databases.
```

[^](#need-to-know)
---

## How to Define Routes in Flask

**Routes in Flask are defined using the `@app.route` decorator followed by the URL path.** For example:

    
    python
    ```
    @app.route('/')
    def index():
      return 'Welcome to the homepage!'
    ```

This associates the specified URL path ('/') with the index() function, which returns 'Welcome to the homepage!'

[^](#need-to-know)
---

# What is a Route
**In web development, a route refers to the mapping of a URL path to a specific function or resource in a web application. Routes define the endpoints that clients can request.**

# How to Handle Variables in a Route
**Variables can be handled within routes by specifying a variable section in the URL using <variable_name>.** 
---

For example:
---
    python
---
      @app.route('/user/<username>')
      def show_user_profile(username):
        return f'User: {username}'
    
Here, the show_user_profile() function takes the username variable from the URL and displays it in the response.

[^](#need-to-know)
---

# What is a Template
**A template in web development refers to a pre-designed layout or structure used to generate dynamic content. In Flask, templates are HTML files that can include placeholders for dynamic data.**

# Create an HTML Response in Flask Using a Template
**To create an HTML response using a template in Flask:**

  Create an HTML template file, e.g., template.html.
  Use Flask's render_template function to render the HTML template and pass dynamic data.
  Return the rendered template as a response. 
  
  For example:
      python
      
        from flask import render_template

        @app.route('/hello/<name>')
        def hello(name=None):
          return render_template('template.html', name=name)
      
This passes the name variable to the template.html file, which can display it dynamically.

[^](#need-to-know)
---

# Create a Dynamic Template (Loops, Conditions...)
**Dynamic templates in Flask allow for incorporating loops, conditions, and dynamic data. Use template syntax (Jinja2) to include logic in your HTML templates.**

For instance:
      
      html
      
        <ul>
          {% for item in items %}
            <li>{{ item }}</li>
          {% endfor %}
        </ul>
      
Here, the {% for ... %} block loops through items and displays each item within an <li> tag.

[^](#need-to-know)

# Display Data from a MySQL Database in HTML
**To display data from a MySQL database in HTML using Flask**:
    
    1.Connect Flask to the MySQL database using a library like flask-mysql.
    2.Query the database to retrieve the desired data.
    3.Pass the fetched data to an HTML template using Flask's render_template function.
    4.Display the data in the HTML template dynamically using template syntax (Jinja2).

---

[^](#need-to-know)

---

# W3C Compliance and Validation

# Overview
This project adheres to W3C (World Wide Web Consortium) standards to ensure compatibility, accessibility, and proper rendering across different browsers and devices. W3C compliance is essential for creating web content that follows best practices and promotes a seamless user experience.

[^](#need-to-know)

# W3C Validation
# What is W3C Validation?
W3C validation is the process of checking your web documents against the official standards set by the W3C. This ensures that your HTML, CSS, and other web-related technologies meet the specifications, reducing the likelihood of errors and improving overall web quality.

# How to Validate
To validate this project, you can use the W3C Markup Validation Service for HTML and W3C CSS Validation Service for CSS. Follow these steps:

1. HTML Validation:

Open the W3C Markup Validation Service.
Enter the URL of your web page or upload the HTML file.
Review and address any issues reported by the validator.

2. CSS Validation:
    * Open the W3C CSS Validation Service.
    * Enter the URL of your CSS file or upload the file.
    * Address any warnings or errors reported by the validator.
---

[^](#need-to-know)

---
# Badge
Include a badge in your README to proudly display W3C compliance status. You can use the following Markdown:

markdown
Copy code
[![W3C Compliant](https://img.shields.io/w3c-validation/html?url=your-website-url)](https://validator.w3.org/)

Replace your-website-url with the actual URL of your deployed website.

# Additional Tips
   * Regularly validate your code during
     development to catch and fix issues early.
   * Use semantic HTML and proper CSS techniques
     to enhance accessibility and maintainability.
   * Update your validation status badge whenever
     significant changes are made to your web content.

```
  Feel free to replace the placeholder content
  with your detailed explanations,
  code snippets,
  and additional instructions as needed.
```

[^](#need-to-know)
