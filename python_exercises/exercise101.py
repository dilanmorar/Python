# Define the following variables

# name, last_name, age, eye_color, hair_color

first_name = 'Dilan'
last_name = 'Morar'
eye_color = 'dark brown'
hair_color = 'black'
age = '22'

# Prompt user for input and Re-assign these

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
eye_color = input('What is your eye color? ')
hair_color = input('What is your hair color? ')
age = input('What is your age? ')

# Print them back to the user as conversation

# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize() + '! Welcome, your age is ' + age + ', your eyes '
    'are '+ eye_color + ' and your hair color is ' + hair_color + '.')

#Section 2 - Calculate in what year was the person born? and responde back.

# print something like: 'You said you we're 28 hence you were born in 1991!'