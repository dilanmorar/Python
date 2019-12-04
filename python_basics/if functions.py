# if functions
# control flow
# while loops also part of the control flow

# syntax
# if <condition>:
    # block of code
# elif <condition>:
    # block of code
# else:
    # block of code

age = int(input('what is your age? '))

if age < 21 and age >= 18:
    print('you can drive, vote, but not drink in the US')
elif age > 18:
    print('you can drive, vote and drink in the US')
elif age >= 16:
    print('you can drive, but not vote or drink in the US')
else:
    print("you can't do anything in the US")

# most specific has to be on top
# conditions are built with operators and logical operators
# once something is true, the block runs and the program exits the fuction