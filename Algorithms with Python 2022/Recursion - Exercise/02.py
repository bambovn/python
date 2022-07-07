# 02. Nested Loops

def nested_loops(index, arr):

    if index >= len(arr):
        print(*arr, sep=' ')
        return

    for num in range(1, len(arr) + 1):
        arr[index] = num
        nested_loops(index+1, arr)


n = int(input())
arr = [None] * n

nested_loops(0, arr)
