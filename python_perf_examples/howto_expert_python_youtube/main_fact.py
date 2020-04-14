import multiprocessing as mp
from fact import get_factorial, timer, profiler

NUMBERS = []
_ = [NUMBERS.append(x) for x in range(500, 1000)]


@profiler
@timer
def loop_single_proc(nums):
    """Loop over single processing of tuple
    Args:
        nums (list of ints): list of ints
    """
    result_list = []
    return [result_list.append(get_factorial(x)) for x in nums]

@profiler
@timer
def map_single_proc(nums):
    """Use map in a single process to determine fact
    
    Args:
        nums (list of ints): list of ints
    """
    return list(map(get_factorial, nums))

@profiler
@timer
def multi_proc_map(nums):
    """Use multiprocesses to determine fact
    
    Args:
        nums (list of ints): list of )) 
    """

    with mp.Pool(processes=4) as pool:
        result = (pool.map(get_factorial, nums))
    return result

if __name__ == '__main__':
    loop_single_proc(NUMBERS)
    map_single_proc(NUMBERS)
    multi_proc_map(NUMBERS)
