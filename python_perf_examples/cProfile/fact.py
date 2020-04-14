import cProfile, pstats, io
import time

def get_factorial(n):
    """Do factorial of n.
    Example:
    Factorial(3) == 3 * 2 * 1
    
    Args:
        n (integer): Do n factorial
    """

    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial


def timer(fn):
    """
    Decorator to determine running time
    """
    def inner(*args, **kwargs):
        t0 = time.time()
        retval = fn(*args, **kwargs)
        t1 = time.time()
        print('Total time for {}: {:.4}'.format(fn.__name__, t1-t0))
        return retval
    return inner

def profiler(fn):
    """
    Decorator for profiling
    """
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fn(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return inner
        