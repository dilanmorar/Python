# lists in python
# lists are ordered by index
# aka --> arrays or objects in java script

# syntax
# declare lists using ()
# seperate objects using

landlords = ['Julio', 'Jane', 'Alfred', 'Marksons']
print(landlords)
print(type(landlords))

# access the landlords in the list
print(landlords[2])
print(landlords[-1])
print(landlords[0])

# places to live
places_to_live = ['California', 'Rio de Janeiro', 'Melbourne', 'Manchester', 'Singapore']
print(places_to_live[3])

# reassigning a index
places_to_live[3]="Hawaii"
print(places_to_live[3])

# method .append(object)
print(len(places_to_live))
places_to_live.append('LA')
print(len(places_to_live))

# insert into a specific position .insert(object)
places_to_live.insert(0,'Lisbon')
print(places_to_live)

# .pop(object) removes specific from list
places_to_live.pop(3)
print(places_to_live)

# list slicing used to manage lists
print(places_to_live[3:])
print(places_to_live[:3])

# print from specified index to second specified index
print(places_to_live[2:4])

# skip slicing
print(places_to_live[0::2])

# tuples immutable lists
# syntax defined using (object, object)
enemies = ('Mario', 'Sailorman' 'Moon Cake', 'Jerry', 'Berry')
print(type(enemies))

# if you try to re-assign it will break