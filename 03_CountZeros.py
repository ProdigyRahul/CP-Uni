# num = int(input())

# def fact(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return x * fact(x-1)

# # count traililng zeros

# temp = fact(num)
# print("Factorial of" + num + " is" + temp)
# cnt = 0
# while temp % 10 == 0:
#     temp = temp // 10
#     cnt += 1
# print(cnt)


def countZero(num):
    count = 0
    power_of_5 = 5
    while num >= power_of_5:
        count += num // power_of_5
        power_of_5 *= 5
    return count

num = int(input("Enter a number: "))

zeros_count = countZero(num)

print(f"Number of zeros in {num}! is {zeros_count}")

