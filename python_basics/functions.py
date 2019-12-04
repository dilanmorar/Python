# functions

# a function is like a machine
# it needs to be turned on (called)
#it does things (block of code)

# good practices
# they should be small and only do one job
    # avoid stringy code
    # testable code
    # maintainable code
    # readable

# Do Not Print inside a function
# call the function inside a print(function_name)
# DRY - Don't Repeat Yourself
# seperation of concerns
    # define functions in one file
    # call them in another
    # there is more to this

# functions work this way
    # 1) define a function
    # 2) call a function

# syntax
# def <name>(arg1, arg2 ,arg3):
    # block of code
    # return something if you wish

def say_hello():
    return 'hello'
# print(say_hello())

def say_hello_user(firstname, lastname):
    return 'Hello ' + firstname.capitalize() + ' ' + lastname.capitalize()
# print(say_hello_user('dilan', 'morar'))