arr = list(map(int, input().split()))
if len(arr) % 2 != 0:
    print("Invalid Input")
else:
    k = int(input())

    first = 0
    second = 1
    unique = set()

    while(second <= len(arr) and first <= len(arr)):
        sum = arr[first] + arr[second]
        if sum % k == 0:
            unique.add((arr[first], arr[second]))
            first += 1
            second += 1
        first += 1
        second += 1
        

    print(unique)