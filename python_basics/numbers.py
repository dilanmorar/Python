# numerical types
# numerical types are: integers, floats, composits, complex numbers etc...

# declaring an int
num1 = 20
print(type(num1))
num2 = 20.0
print(type(num2))

# mathematical operators + - / * % --- these tend to take priority over logical operators
result1 = 10+12
result2 = 10-2
result3 = 10*30
result4 = 20%3 # finds the remainder
result5 = 20/2

print(result1, result2, result3, result4, result5)

# logical operators <
# = means assignment
num_a = 10
num_b = 10
num_c = 13

# more than --> returns a boolean
print(num_b>num_c)
print(num_c>num_a)

# less than --> returns a boolean
print(num_b<num_c)
print(num_c<num_a)

# more/less than or equal to --> returns a boolean
print(num_b>=num_c)
print(num_c>=num_a)
print(num_a<=num_b)

# check if the same --- data type matters
print('10'==10)
print(num_b==num_a)
print(num_b==num_c)

# Boolean --- True or False
bool_true=True
bool_false=False
print(bool_true==bool_false)

# !
print(bool_true!=bool_false)

# logical AND & logical OR
# (<condition> and <condition>) --> boolean
print(True and True)
print(True and False)
# (<condition> or <condition>) --> boolean
print(True or False)
print(False or False)