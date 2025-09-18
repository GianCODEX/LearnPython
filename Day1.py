octal_num = 0o20
print(octal_num)
print(type(octal_num))

hexadecimal_num = 0x10
print(hexadecimal_num)
print(type(hexadecimal_num))

binary_num = 0b10000
print(binary_num)
print(type(binary_num))


======================================
platform = "PYnative"
platform2 = "PYnation"
print(type(platform))
print(type(platform2))

print(platform)
print(platform2)

print(platform[0:3])
print(platform2[0:5])


======================================
x = 9 + 8j
y = 10 + 4.5j
z = 11.2 + 1.2j
print(type(x))

print(x)
print(y)
print(z)


======================================
# creat a tuple
my_tuple = (11, 24, 56, 88, 78)
print(my_tuple) # (11, 24, 56, 88, 78)
print(type(my_tuple)) # class 'tuple'

# Accessing 3rd element of a tuple
print(my_tuple[2]) # 56

# Slice a tuple
print(my_tuple[2:7]) # (56, 88, 78) 

# create a tuple using a tuple() class
my_tuple2 = tuple((10, 20, 30, 40)) # (10, 20, 30, 40)
print(my_tuple2)


=====================================
my_list = [1,2,3,3,3,4] # listing
my_set = {1,2,3,3,3,4} # arrange the list and removes duplicate

print("List: ", my_list)
print("Set: ", my_set)


=====================================
my_list = [1,2,3,3,3,4]
my_set = {1,2,3,3,3,4}

my_set.add(400) # .add is a function to add items within the key-value
my_set.add(300) 

my_set.remove(1) # .remove is a function remove items within the key-value

print("List: ", my_list)
print("Set: ", my_set)


=====================================
my_set = {11,44,75,89,56}
print(type(my_set))

f_set = frozenset(my_set)
print(type(my_set))

print(f_set)


===================================== 
# CONDITIONS
x = 25
y = 20

z = x > y
print(z)
print(type(z))

num = int(input("Enter a number: "))

if num == 0:
    print("The number is 0")
elif num < 0:
    print("Enter a positive number")
elif num % 2:
    print("The number is odd")
else:
    print("The number is even")


=====================================
a = [9,14,17,11,78]
b = bytes(a)
print(type(b))
print(b[0])
print(b[-1])


=====================================
