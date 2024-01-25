# [0x02: AirBnB Clone-v2](#airbnb-clone)
# [....](#v2)

# [0x03: Deploy Static](#deploy-static)
# [0x04: Web framework](https://github.com/TheeKingZa/AirBnB_clone_v2/tree/master/web_flask/README.md)
# [Authors](https://github.com/TheeKingZa/AirBnB_clone_v2/tree/master/AUTHORS) 

# Description

    This project is an implementation of a simplified version of AirBnB's backend system.
    It includes a command-line interpreter
    a storage engine for managing data related to AirBnB-like objects.

## Resources
Read or watch:

* [cmd module](https://docs.python.org/3.8/library/cmd.html)
* [cmd module in depth](http://pymotw.com/2/cmd/)
* [packages concept page](https://docs.python.org/3.4/tutorial/modules.html#packages)
* [uuid module](https://docs.python.org/3.8/library/uuid.html)
* [datetime](https://docs.python.org/3.8/library/datetime.html)
* [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
* [cmd module](https://wiki.python.org/moin/CmdModule)
* [python unittest](https://realpython.com/python-testing/)

# For this project fork:
  * [Codebase](https://github.com/justinmajetich/AirBnB_clone.git)

# [Models](https://github.com/TheeKingZa/AirBnB_clone_v2/blob/master/models/README.md)

# [Unit Test](https://github.com/TheeKingZa/AirBnB_clone_v2/blob/master/tests/README.md)

# [Web Static](https://github.com/TheeKingZa/AirBnB_clone_v2/blob/master/web_static/README.md)

# NEED TO KNOW?
* [Background Context](#background-context)
* [Comments in SQL](comments-for-your-sql-file)
* [What is Unit testing and how to implement it in a large project](#unit-testing)
* [What is args and how to use it](#args)
* [What is kwargs and how to use it](#kwargs)
* [How to handle named arguments in a function](#named-arguments)
* [How to create a MySQL database](#create-mysql-database)
* [How to create a MySQL user and grant it privileges](#create-mysql-user-and-grant-privileges)
* [What ORM means](#orm)
* [How to map a Python Class to a MySQL table](#map-class-to-mysql-table)
* [How to handle 2 different storage engines with the same codebase](#handle-multiple-storage-engines)
* [How to use environment variables](#use-environment-variables)
---
# AirBnB Clone
# v2
# **Background Context**
	# Environment variables will be your best friend for this project!
 	|	* HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
   	|	* HBNB_MYSQL_USER: the username of your MySQL
	|	* HBNB_MYSQL_PWD: the password of your MySQL
	|	* HBNB_MYSQL_HOST: the hostname of your MySQL
	|	* HBNB_MYSQL_DB: the database name of your MySQL
	|	* HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)
	|
	# Environment Variables in Python
	* In Python, the os module is commonly used to access environment variables. Here's a brief explanation of the environment variables mentioned in your context:
 		* HBNB_ENV: Indicates the running environment, such as "dev" or "test."
		* HBNB_MYSQL_USER: Specifies the MySQL username.
		* HBNB_MYSQL_PWD: Stores the MySQL password.
		* HBNB_MYSQL_HOST: Contains the hostname of the MySQL server.
		* HBNB_MYSQL_DB: Represents the database name for MySQL.
		* HBNB_TYPE_STORAGE: Determines the type of storage used, such as "file" or "db."

# Comments for your SQL file:
	..$ cat my_script.sql
		-- first 3 students in the Batch ID=3
		-- because Batch 3 is the best!
		SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
	..$

[^](#need-to-know)

## Unit Testing
	Unit testing is a software testing method in which individual units or components of a program are tested in isolation to ensure that they function correctly.
 	The primary goal of unit testing is to validate that each unit of the software performs as designed.
  	In a large project, unit testing becomes crucial for maintaining code quality, catching bugs early in the development process and facilitating code refactoring.

	* Why Unit Testing?
		1. Early Detection of Bugs:
  			Unit tests help identify and fix bugs at an early stage,
     			preventing them from escalating into larger issues.
		2. Code Refactoring:
  			Unit tests provide a safety net for making changes to the codebase.
     			Developers can confidently refactor code knowing that existing functionality won't break.
		3. Documentation:
  			Unit tests serve as living documentation,
     			showcasing how each component of the system is intended to work.
		4. Continuous Integration:
  			Automated unit tests are integral to continuous integration pipelines,
     			ensuring that new code changes do not introduce regressions.

	* How to Implement Unit Testing in a Large Project
		1. Choose a Testing Framework:
			Select a testing framework that fits your project and programming language.
   			Popular choices include unittest for Python, JUnit for Java, and JUnit for JavaScript.

		2. Organize Your Project Structure:
			Arrange your project in a way that facilitates easy testing.
   			Place your unit tests in a separate directory,
      			and structure your code to be modular and testable.

		3. Write Testable Code:
			Design your code with testability in mind. Break down complex functions into smaller,
   			testable units. Use dependency injection to make it easier to isolate and test components.

		4. Write Unit Tests:
			Create individual test cases for each unit or component. 
   			Test a unit's inputs, outputs, and edge cases.
      			Ensure that the tests cover a broad spectrum of scenarios.

		Example (using Python's unittest):

			pyCode:
				import unittest
				from your_module import your_function

				class TestYourFunction(unittest.TestCase):
				    def test_positive_input(self):
				        self.assertEqual(your_function(2, 3), 5)

				    def test_negative_input(self):
				        self.assertEqual(your_function(-2, 3), 1)

				    # Add more test cases as needed
	* Automate Testing:
		Integrate your unit tests into your continuous integration pipeline.
  		This ensures that tests are run automatically whenever there's a code change, providing rapid feedback.

	* Maintain and Update Tests:
		Regularly review and update your unit tests as the codebase evolves.
  		Ensure that new features and changes are accompanied by corresponding test cases.

By incorporating unit testing into your development workflow, you can enhance the reliability, maintainability, and scalability of your large projects

[^](#need-to-know)

# Args
	*args in Python
 	
  		In Python, *args is a special syntax that allows a function to accept a variable number of positional arguments.
    		The term "args" is a convention, and the asterisk (*) before it indicates that it can accept multiple arguments.

		# Purpose of *args
			When defining a function,
	  		you may not always know in advance how many arguments it will receive.
    			*args provides a flexible way to handle variable numbers of arguments without explicitly naming them.

		# How to Use *args
			Here's a simple example to illustrate the use of *args:

			pyCode:
				def print_args(*args):
				    for arg in args:
				        print(arg)

				# Using *args to accept and print multiple arguments
				print_args(1, 2, 3, "four", 5.0)

		In this example, the print_args function can accept any number of arguments,
 		and it will print each argument.
  		The *args syntax allows the function to handle a variable-length argument list.

		# Unpacking with *args
			You can also use *args when calling a function to unpack the elements from an 
	  		iterable (e.g., a list or tuple) and pass them as separate arguments:

			pyCode:
				def add_numbers(*args):
				    return sum(args)

				# Using *args to pass a list of numbers to the function
				numbers = [1, 2, 3, 4, 5]
				result = add_numbers(*numbers)
				print(result)  # Output: 15
		In this example, *numbers unpacks the elements of the list, and the add_numbers function receives them as separate arguments.

		* When to Use *args
			Use *args when you want to create functions that can accept a variable number of positional arguments.
	  		This is particularly useful in scenarios where the number of inputs may vary,
    			and you want your function to be versatile.

		Keep in mind that *args is a convention,
	 	and you could use any other name preceded by an asterisk,
  		but sticking to this convention makes
	   	your code more readable and consistent with the Python community.

			pyCode:
				def example_function(*custom_name):
				    # Function logic here
				    pass
		In summary, *args allows you to work with an arbitrary number of positional arguments, making your functions more adaptable and versatile.

[^](#need-to-know)

## Kwargs
	# **kwargs in Python
		In Python, **kwargs is a special syntax that allows a function to accept a variable number of keyword arguments. 
  		The term "kwargs" is short for "keyword arguments," and the double asterisk (**) before it indicates 
    		that it can accept multiple keyword arguments.

	# Purpose of **kwargs
		While *args is used to pass a variable number of positional arguments, 
  		**kwargs is used to pass a variable number of keyword arguments. 
    		This is especially useful when you want to create functions that are flexible and
      		can accept additional named parameters without explicitly defining them in the function signature.

	# How to Use **kwargs
		Here's a simple example to illustrate the use of **kwargs:

			pyCode:
				def print_kwargs(**kwargs):
				    for key, value in kwargs.items():
				        print(f"{key}: {value}")

				# Using **kwargs to accept and print multiple keyword arguments
				print_kwargs(name="John", age=25, city="New York")
	
 	In this example, the print_kwargs function can accept any number of keyword arguments, 
 	and it will print each key-value pair. 
  	The **kwargs syntax allows the function to handle a variable-length list of keyword arguments.

	# Using **kwargs with Functions
		You can use **kwargs when defining a function to indicate that it should accept any number of keyword arguments:

   			pyCode:
      				def example_function(**custom_kwargs):
				    # Function logic here
				    pass
	# Passing **kwargs to Another Function
		You can also use **kwargs to pass a dictionary of keyword arguments to another function:

			pyCode:
				def process_data(**kwargs):
				    # Process data using keyword arguments
				    pass

				def main_function(**kwargs):
				    # Do some logic
				    process_data(**kwargs)  # Pass keyword arguments to another function
				    # Continue with other logic
		
  		In this example, the process_data function receives the keyword arguments passed to main_function.

# When to Use **kwargs
	Use **kwargs when you want to create functions that can accept a variable number of keyword arguments. 
 	This is particularly useful in scenarios where additional parameters may be needed, 
  	and you want your function to be adaptable to different situations.

	Keep in mind that **kwargs is a convention, 
 	and you could use any other name preceded by a double asterisk, 
  	but sticking to this convention makes your code more readable and consistent with the Python community.

In summary, **kwargs allows you to work with an arbitrary number of keyword arguments, making your functions more versatile and flexible

[^](#need-to-know)

## Named Arguments
Guide on how to handle named arguments in a Python function.

[^](#need-to-know)

## Create MySQL Database
Step-by-step instructions on how to create a MySQL database.

[^](#need-to-know)

## Create MySQL User and Grant Privileges
Instructions on creating a MySQL user and granting the necessary privileges.

[^](#need-to-know)

## ORM
Definition and explanation of what ORM (Object-Relational Mapping) means.

[^](#need-to-know)

## Map Class to MySQL Table
Guide on how to map a Python Class to a MySQL table using ORM.

[^](#need-to-know)

## Handle Multiple Storage Engines
Explanation of how to handle 2 different storage engines with the same codebase.


[^](#need-to-know)

## Use Environment Variables
Instructions on how to use environment variables in Python projects.

---

# Deploy static


Concepts
For this project, we expect you to look at these concepts:

* [CI/CD](https://digital.ai/catalyst-blog/walk-before-you-run-understanding-ci-in-cd/)
* [AirBnB clone](#airbnb-clone)


# More To Know !


CI/CD
The lean/agile methodology (See: [Twelve Principles of Agile Software](http://agilemanifesto.org/principles.html)) is now widely used by the industry and one of its key principles is to iterate as fast as possible. If you apply this to software engineering, it means that you should:

code
ship your code
measure the impact
learn from it
fix or improve it
start over
As fast as possible and with small iterations in days or even hours (whereas it used to be weeks or even months). One big advantage is that if product development is going the wrong direction, fast iteration will allow to quickly detect this, and avoid wasting time.

From a technical point of view, quicker iterations mean fewer lines of code being pushed at every deploy, which allows easy performance impact measurement and easy troubleshooting if something goes wrong (better to debug a small code change than weeks of new code).



Applied to software engineering, CI/CD (Continuous Integration/Continuous Deployment) is a principle that allows individuals or teams to have a lean/agile way of working.

This translates to a “shipping pipeline” which is often built with multiple tools such as:

Shipping the code:
Capistrano, Fabric
Encapsulating the code
Docker, Packer
Testing the code
Jenkins, CircleCi, Travis
Measuring the code
Datadog, Newrelic, Wavefront
[^](#airbnb-clone-v2)

