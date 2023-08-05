================================================================
Python Devtools
================================================================

**Pydevtools is full of tools i have found to be useful for python3 development**

This project is BIG fans of decorators. All tools in this project can be used by adding a decorator to a function

================
Getting started
================
**Import**

Importing is pretty straight forward simply add *import pydevtools*

**Timer**

Time any function in your code simply by adding the @pydevtools.optimize.timer(output_function) decorator
The output_function variable is designed to be a logging function such as logging.debug
Any function that accepts a single string as input can be used as an output_function


**Get_calls**

We have all been there. A complex piece of code where one function keeps breaking and you suspect it is because of something that calls it
get_calls helps you find exactly what is breaking it by giving you the function that calls it and the arguments that calls it
it can be applied to any function by using the @pydevtools.debug.get_calls(output_function) decorator 
The output_function argument can be any function that accepts a single string argument but is intented for a logging function or print