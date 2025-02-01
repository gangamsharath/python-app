import time

def profiler(fun):
    """print the runtime of the decorated furnction"""
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = fun(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"finished {fun.__name__} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@profiler
def algorithm(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(1000)]) #throw away variable

algorithm(1)
algorithm(9999)