import time
from functools import wraps

def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # in milliseconds
        print(f"Function '{func.__name__}' executed in {execution_time:.2f} ms")
        return result
    return wrapper

# Example usage:
@execution_time
def example_function():
    time.sleep(1)  # Simulate some work
    print("Function executed")

example_function()