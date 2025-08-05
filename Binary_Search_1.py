def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
n_data = list(map(int, input().split()))
n_data.sort() # 이진 탐색을 위해 정렬

m = int(input())
m_data = list(map(int, input().split()))

for i in m_data:
    result = binary_search(n_data, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
                  
    


