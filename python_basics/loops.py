# loops
# loops will iterate over an iterable and run a block of code

# syntax
# for <placeholder> in <iteratable>:
    # identation
    # includes the code
# code stops when identation stops

#iterables are: list, ranges and dictionaries ... also strings

import time

wishlist = ['rc car', 'molten cheese', 'cheerleaders', 'attention', 'white shirts', 'sugar laces', 'reeses pieces',
'pastel de nata']

# counter = 1
# for item in wishlist:
#     print(counter, '-', item)
#     time.sleep(1)
#     counter += 1


listdata = [['rc car','cheerleaders','white shirts','audi r8'],['sugar laces','cheese','pastel de nata','baklava']]

counter = 1
for data in listdata:
    print(data)
    counter = 1
    for number in data:
        print(counter, '-', number)
        counter += 1