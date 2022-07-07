# 4.Generating 0/1 Vectors

def vectorRecursion(index, vector):
    if index >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[index] = num
        vectorRecursion(index + 1, vector)


n = int(input())
vector = [0] * n

vectorRecursion(0, vector)
