n = 5
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
    
print("The sum of numbers from 1 to", n, "is:", sum)

x = 0

while x < 11:
    print(x)
    if x == 10:
        break
    x += 1 
    # Will count to 10
print("Loop finished")

# number loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
    
print("Loop finished")

# Python loop

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("Loop finished")

# Char loop

text = "Hello, Gian!"

for char in text:
    print(char)
print("Loop finished")    
    
# range() function

for c in range(1, 8, 2):
    print(c)
print("Loop finished")

# range function (cont'd)

for v in range(6):
    print(v)
print("Loop finished")
