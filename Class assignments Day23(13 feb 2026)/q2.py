import math
import time
from multiprocessing import Pool, cpu_count

numbers = [5000, 6000, 5500, 4500, 7000]


def compute_factorial(n):
    return math.factorial(n)


if __name__ == "__main__":



    starttime = time.perf_counter()

    seq_results = []
    for num in numbers:
        result = compute_factorial(num)
        seq_results.append(result)

    sequential_time = time.perf_counter() - starttime
    print("Sequential Time:", sequential_time)


    starttime2 = time.perf_counter()

    with Pool(cpu_count()) as pool:
        parallel_result = pool.map(compute_factorial, numbers)

    parallel_time = time.perf_counter() - starttime2
    print("Multiprocessing Time:", parallel_time)