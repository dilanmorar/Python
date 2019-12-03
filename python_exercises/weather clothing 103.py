# Make a weather/clothing game
# IF statements
# Ask for user input and depending on the response advise on their attire.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# when sunny >> respond with 'take your shorts!'
# stormy >> respond with 'take rain coat'
# rainy >> respond with 'Take your umbrella'
# rainy and stormy >> 'stay home'
# anything else respond with 'sorry, i didn't quite catch that'

print("These are the weather conditions: 'sunny', 'stormy', 'rainy' and 'rainy and stormy'")
weather = input('Please enter a weather condition: ')

if weather == 'sunny':
    print('take your shorts!')
elif weather == 'stormy':
    print('take rain coat')
elif weather == 'rainy':
    print('take your umbrella')
elif weather == 'rainy and stormy':
    print('stay home')
else:
    print("sorry, i didn't quite catch that")