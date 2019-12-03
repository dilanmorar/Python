# continuation on for loops

dict_data = {
    1: {
        'name': 'Bronson',
        'money': 0.50
    },
    2: {
        'name': 'Janet',
        'money': 3.50
    },
    3: {
        'name': 'Bartolumeu',
        'money': 1.50
    },
    4: {
        'name': 'Vanessa',
        'money': 0.23
    }
}

# for key in dict_data:
#     print(key)
#     print(dict_data[key])

for key in dict_data:
    print(dict_data[key]['name'], 'owes', dict_data[key]['money']*4000/12+dict_data[key]['money'])