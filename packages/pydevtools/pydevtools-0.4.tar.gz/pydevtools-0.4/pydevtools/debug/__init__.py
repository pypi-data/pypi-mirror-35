'''
A helping hand to help you efficiently solve problems with your code
'''
from functools import wraps
import inspect




def get_calls(output_function):
    '''
    We have all been there. A complex piece of code where one function keeps breaking and you suspect it is because of something that calls it
    get_calls helps you find exactly what is breaking it by giving you the function that calls it and the arguments that calls it
    it can be applied to any function by using the @pydevtools.debug.get_calls(output_function) decorator 
    @param output_function : argument can be any function that accepts a single string argument but is intented for a logging function or print
    '''
    def get_call_dec(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            o = f"function: {inspect.stack()[1][3]} args: {args} kwargs: {kwargs}"
            output_function(o)
            r = fn(*args, **kwargs)
            return(r)
        return(decorator)
    return(get_call_dec)