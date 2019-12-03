
# mr Miyagi trainee ##projct

# Ask for user input and depending on the response, mr Miyagi will respond.
phrase = input('What would you like to say to Mr Miyagi?')

# Evaluate each input and print the appropriate responses
while phrase == 'Sensei, I am at peace':
    print('')
    phrase = input('What would you like to say to Mr Miyagi?')
if phrase == 'Sensei, I am at peace':
    print('Sometimes, what heart know, head forget')
    phrase = input('What would you like to say to Mr Miyagi?')
elif phrase[:-1] == '?':
    print('questions are wise, but for now. Wax on, and Wax off!')
    phrase = input('What would you like to say to Mr Miyagi?')
elif 'block' in phrase:
    print('Remember, best block, not to be there..')
    phrase = input('What would you like to say to Mr Miyagi?')
elif phrase[:6] == 'Sensei':
    print('You are smart, but not wise - address me as Sensei please')
    phrase = input('What would you like to say to Mr Miyagi?')
else:
    print('do not lose focus. Wax on. Wax off.')
    phrase = input('What would you like to say to Mr Miyagi?')

# Follow these rules:

# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'

# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'

# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remeber, best block, not to be there..'

# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.'

# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'

your_response = input('(MR.Miyagi)... -.-')