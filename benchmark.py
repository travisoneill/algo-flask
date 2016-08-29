import sort_library
from math import log10
from statistics import stdev, mean
from collections import deque, defaultdict
from time import time
from random import randint, randrange

def handle_request(int_array, request_data):
    """Takes code string and converts to function object to be passed into
    'run_test.' Called from server."""
    code = request_data['method']
    # print(code)
    exec(code)
    test_function = locals()[request_data['name']]
    # print(test_function)
    test_results = run_test(int_array, test_function)
    print(test_results)
    return test_results

def run_test(int_array, test_function, iterations=1):
    """runs benchmark test on arrays of length equal to ints in int_array.
    called from 'handle_request'"""
    results = []
    for n in int_array:
        # print(n)
        # print(results)
        data = benchmark(test_function, n, iterations)
        results.append({"x": n, "y": data['avg']})
    return results

def random_array(length, min=0, max=10):
    """random_array(n, min=-1000000, max=1000000)
         returns ARRAY of random INTS"""
    randarr = []
    for x in range(length):
        randarr.append(randint(min, max))
    return randarr

def benchmark(test_function, array_length=100000, iterations=10, analytics=False):
    """benchmark(algo, length=100000, iterations=10):
         returns INT total run time in ms"""
    random = random_array(array_length)
    elapsed_time = 0
    results = []
    for n in range(iterations):
        arr = random.copy()
        t0 = time()
        test_function(arr)
        t1 = time()
        elapsed_time += float(t1-t0)
        results.append(float(t1-t0) * 1000)

    ms = int(elapsed_time * 1000)
    avg = ms // iterations
    benchmark_results = {'total': ms, 'avg': avg}
    if analytics:
        analysis = analyze(results)
        benchmark_results['std'] = analysis['std']
        benchmark_results['adj_avg'] = analysis['adj_avg']
    return benchmark_results

def analyze(bm_result):
    """drops outliers and calculates adjusted avg and stdev"""
    bm_result.sort()
    if len(bm_result) > 20:
        drop = len(bm_result) // 20
        bm_result = bm_result[drop:-drop]
    avg, std = mean(bm_result), stdev(bm_result)
    return {'std': std, 'adj_avg': avg}

def python_sort(arr):
    """python library sort"""
    arr.sort()

def bubble_sort(arr, done=False):
    """bubble_sort(arr, done=False)
         Sorts array. Iterative. Time: O(N^2), space: O(1)"""
    while done == False:
        done = True
        for idx, num in enumerate(arr[0:-1]):
            if num > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
                done = False
    return arr

def merge_sort(arr):
    """Sorts array. Recursive. O(NlogN) time, O(N) space"""
    def merge(arr1, arr2):
        arr1, arr2 = deque(arr1), deque(arr2)
        merged = []
        while len(arr1) > 0 and len(arr2) > 0:
            if(arr1[0] < arr2[0]):
                merged.append(arr1.popleft())
            else:
                merged.append(arr2.popleft())
        return merged + list(arr1) + list(arr2)
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge_sort_iter(arr):
    def merge(arr1, arr2):
        arr1, arr2 = deque(arr1), deque(arr2)
        merged = []
        while len(arr1) > 0 and len(arr2) > 0:
            if(arr1[0] < arr2[0]):
                merged.append(arr1.popleft())
            else:
                merged.append(arr2.popleft())
        return merged + list(arr1) + list(arr2)
    for i in range(len(arr)):
        arr[i] = [arr[i]]
    while len(arr) > 1:
        merged = []
        for i in range(0, len(arr) - 1, 2):
            merged.append(merge(arr[i], arr[i+1]))
        arr = merged

def counting_sort(arr):
    '''Sorts array. O(m+n) time. O(m) space.'''
    min, max = arr[0], arr[0]
    map = defaultdict(lambda: 0)
    sorted = []
    for n in arr:
        map[n] += 1
        if n > max: max = n
        if n < min: min = n
    for n in range(min, max + 1):
        for _ in range(map[n]):
            sorted.append(n)
    return sorted

def dig(n, num):
    digit = (abs(num) // 10**n) % 10
    digit = digit * -1 if num < 0 else digit
    return digit

def radix_sort(arr):
    '''Sorts array. O(log10(m)*n) time. O(n) space'''
    def dig(n, num):
        digit = (abs(num) // 10**n) % 10
        digit = digit * -1 if num < 0 else digit
        return digit
    iterations = 1
    iter = 0
    while iter < iterations:
        idx = [-1] + [0] * 18
        max = abs(arr[0])
        for n in arr:
            if abs(n) > max: max = abs(n)
            d = dig(iter, n)
            idx[d + 9] += 1
        iterations = int(log10(max)) + 1
        for i in range(18):
            idx[i + 1] += idx[i]
        for n in reversed(arr[:]):
            i = dig(iter, n) + 9
            j = idx[i]
            arr[j] = n
            idx[i] -= 1
        iter += 1





def run():
    pass

#TESTING FUNCTION ALIASES
ra = random_array
bm = benchmark

#SORT FUNCTION ALIASES
ps = python_sort
bs = bubble_sort
ms = merge_sort
msi = merge_sort_iter
cs = counting_sort
rs = radix_sort


if __name__ == "__main__":
    print('PYTHON BENCHMARK CLI', '\n')
    print('SORTS, (ALIAS => METHOD):')
    print('ps() => ', ps.__doc__)
    print('ms() => ', ms.__doc__)
    print('cs() => ', cs.__doc__)
    print('bs() => ', bs.__doc__, '\n')
    print('METHODS, (ALIAS => METHOD):')
    print('ra() => ', ra.__doc__)
    print('bm() => ', bm.__doc__)
