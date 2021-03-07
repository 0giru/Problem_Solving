def BinarySearch(par_array, target, start, end):
    while start <= end:
        mid = (start + end)//2

        if par_array[mid] == target:
            return mid

        elif par_array[mid] > target:
            end = mid - 1

        elif par_array[mid] < target:
            start = mid + 1
    
    return None

n, target = map(int, input().split())

array = list(map(int, input().split()))

result = BinarySearch(array, target, 0, n-1)

if result == None:
    print("there is no target in array")
else:
    print("index of target in array is", result)