'''
A set of tools designed to help optimizing tools
'''
from functools import wraps
from datetime import datetime




def timer(output_function):
    '''
    Time any function in your code simply by adding the @pydevtools.optimize.timer(output_function) decorator
    The output_function variable is designed to be a logging function such as logging.debug
    Any function that accepts a single string as input can be used as an output_function
    '''
    def timer_dec(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            st = datetime.now()
            r = fn(*args, **kwargs)
            output_function(f"{fn.__name__} completed in {datetime.now() - st}")
            return(r)
        return(decorator)
    return(timer_dec)