# strings

## define string
my_string = "I'm an amazing string"
my_string2 = "So am I"
my_name = "Dilan Morar"

print(my_string)
print(type(my_string2))

# Concatenation - joining if two strings
print("Example of concatenation: "+my_string)
print("these are examples of strings", my_string2, my_string)

concatenate = my_name + ' ' + my_string
print(concatenate)

# interpolation
age = 21
name = "Julia"

# this is where we need to interpolate
print("Welcome <person>, you are <age> years old")
print("Welcome <person>, you were born in <birth_date>")

# this is interpolating
print(f"Welcome {name}, you are {age} years old")
print(f"Welcome {name}, you were born in {2019-age}")

# useful methods for string
example_string = " HeELlloO "
print(example_string)
# remove the blank spaces
print(example_string.strip())
# counts number of characters in a string
print(example_string.count('l'))
print(example_string.lower())
print(example_string.upper())
print(example_string.strip().capitalize())

# learning and using .split()
text_to_split = 'this is some example text in our file'
results_split = text_to_split.split(' ')
print (results_split)

# standard built-in function len()
print(len(example_string))

# casting and int
str_string = '1990'
print(type(str_string))

# str --> int
int_number = int(str_string)
print(type(int_number))

# int --> str
new_str = str(int_number)
print(type(new_str))