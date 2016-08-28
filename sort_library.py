def python_sort():
    return '''def python_sort(arr):
    arr.sort()'''


def bubble_sort():
    return '''def bubble_sort(arr, done=False):
    while done == False:
        done = True
        for idx, num in enumerate(arr[0:-1]):
            if num > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
                done = False
    return arr'''

def merge_sort():
    return '''def merge_sort(arr):
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
    return merge(merge_sort(left), merge_sort(right))'''

# def counting_sort(arr):
#     min, max = arr[0]
#     map = {}
#     for n in arr:
#         count = map.get(n, default=0)
#         count += 1
#         if n > max:
#             max = n
#         in n < min:
#             min = n 
