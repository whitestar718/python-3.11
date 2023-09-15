import time

def timer(function):
    def tictoc(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        print(f"Elapsed time: {(time.time() - start) * 1000} ms.")
    return tictoc


@timer
def append_list(n_iter):
    temp_list = []
    for i in range(n_iter):
        temp_list.append(i)

append_list(2500000)