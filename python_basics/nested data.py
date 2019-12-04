# # nested data in lists and dictionaries
# mix_list = ['strings', 98, ['more string', [1,2,3]]]
# print(type(mix_list[2]))
# internal_list = mix_list[2]
# print(mix_list[2][1][2])
# print(internal_list[1][2])

embeded_dict = {
    'status': 'operational',
    'key1': ['car keys', 'boat keys', 'mansion keys', 'dog house keys'],
    'staff': {
        'Julio Cesar':{
            'firstname': 'Julio',
            'lastname': 'Cesar',
            'birthdate': 1979,
            'football club': 'Flamengo'
        },
        'Julia Venus':{
            'firstname': 'Julia',
            'lastname': 'Venus',
            'birthdate': 1969,
            'football club': 'Cuba FC'
        },
    }
}

print(embeded_dict['key1'][1])
print(embeded_dict['key1'][3])

print(embeded_dict['staff']['Julio Cesar'])

print(embeded_dict['staff']['Julia Venus']['lastname'])
print(embeded_dict['staff']['Julia Venus']['birthdate'])
print(embeded_dict['staff']['Julia Venus']['football club'])
