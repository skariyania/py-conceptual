"""implements throttle mechanism"""
import time
from functools import wraps

class ThrottleError(Exception):
    """Throttle error type"""


def throttle(delay, error_on_throttle=False):
    """
    Decorator function to throttle the execution of a function.

    Args:
    - delay (float): The minimum time (in seconds) between consecutive function calls.
    - error_on_throttle (bool): If True, raise ThrottleError on throttling. 
        If False, log and return None.

    Usage:
    @throttle(2.0, error_on_throttle=True)
    def my_function():
        print("Function called")

    my_function()  # Will be executed
    time.sleep(1)
    my_function()  # Will be throttled, either raising ThrottleError 
                        or logging the throttling message
    time.sleep(2)
    my_function()  # Will be executed
    """
    def decorator(func):
        last_executed_time = 0

        @wraps(func)
        def throttled_function(*args, **kwargs):
            nonlocal last_executed_time

            current_time = time.time()
            elapsed_time = current_time - last_executed_time

            if elapsed_time >= delay:
                result = func(*args, **kwargs)
                last_executed_time = current_time
                return result
            else:
                message = f"Throttling: Function '{func.__name__}' is being throttled."
                if error_on_throttle:
                    raise ThrottleError(message)
                else:
                    print(message)
                    return None
                    # we can modify this to return a specific value or implement a retry mechanism

        return throttled_function

    return decorator


@throttle(delay=2)
def hello():
    """prints hello"""
    print("hello")

# example usage
if __name__ == "__main__":
    hello()
    hello()
    time.sleep(2)
    hello()
    hello()
    hello()
    time.sleep(2)
    hello()
    time.sleep(2)
    hello()
    time.sleep(2)
    hello()
