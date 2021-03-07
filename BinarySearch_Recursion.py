# 이진탐색 함수

# 이진 탐색은 정렬된 자료에서만 사용할 수 있고 O(logN)의 시간복잡도를 가진다.

# 정렬된 배열인 par_array이 필요
# 찾고자 하는 값인 target 필요
# 탐색이 진행되며 시작점인 start 필요
# 탐색이 진행되며 끝점인 end 필요
def BinarySearch(par_array, target, start, end):
    if start > end:
        return None
    
    # 이진탐색을 위한 인덱스 쪼개기
    # 정수부만을 이요하므로 //연산자 사용
    mid = (start + end)//2

    if par_array[mid] == target:
        return mid
    elif par_array[mid] > target:
        return BinarySearch(par_array, target, start, mid-1)
    elif par_array[mid] < target:
        return BinarySearch(par_array, target, mid+1, end)

n, target = map(int, input().split())

array = list(map(int, input().split()))

result = BinarySearch(array, target, 0, n-1)

if result == None:
    print("there is no target in array")
else:
    print("index of target in array is", result)