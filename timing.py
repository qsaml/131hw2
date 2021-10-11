'''
Calculates the time taken to run a function.

Params:
  None
Returns:
  None
'''

import time
import functools


def calculate_time(do_this):
    @functools.wraps(do_this)
    def time_this():
        start_time = time.time()
        thing = do_this()
        end_time = time.time()
        print(f'Total time {end_time - start_time}')
        return thing
    return time_this


@calculate_time
def do_this():
    time.sleep(2)


calculate_time(do_this())
