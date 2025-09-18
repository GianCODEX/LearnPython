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
