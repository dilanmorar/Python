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
## useful methods for string