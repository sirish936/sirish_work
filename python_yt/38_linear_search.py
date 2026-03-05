pos = -1

def search(list, n):
    i=0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    return False

def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False

list = [1, 2, 3, 4, 5]
n = 4

if search(list, n):
    print("Element is present in array")
    print("Element found at index", pos)
else:
    print("Element is not present in array")