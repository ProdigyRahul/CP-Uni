string = input("Enter a string: ")
new_array = string.split(' ')

max_length = 0

for i in range(len(new_array)):
    if len(new_array[i]) > max_length:
        max_length = len(new_array[i])
        
print(max_length)
