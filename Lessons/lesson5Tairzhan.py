# string = "Python"
# for letter in string:
#     print (letter)


# sum = 0
# number = 1
# while number<=100:
#     sum += number
#     number +=2
# print ("сумма нечетных чисел:", sum)

# height = 5

# for i in range(1, height + 1):
#     stars = "*" * i
#     print(stars)

# n=5
# for i in range (1, n+1):
#     for j in range(1, n+1):
#         result = i * j
#         print (f"{i} * {j} = {result}\t", end =" ")


for number in range(2, 101):
    is_prime = True
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} - простое число")
