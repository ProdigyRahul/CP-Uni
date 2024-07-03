row = int(input())
for i in range(0, row):
    for j in range(0, i+1):
        print("*", end='')
    print('')

print("")
for i in range(0, row):
    for j in range(0, i+1):
        print(j+1, end='')
    print("")

# a to z print pattern
