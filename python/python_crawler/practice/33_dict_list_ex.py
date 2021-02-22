# pet list 애완동물
pets = [
        {'name' : 'nabi', 'age' : 25, 'kind' : 'cat'},
        {'name' : 'guma', 'age' : 25, 'kind' : 'dog'},
]
pet3 = {'name' : 'dragon', 'age' : 1, 'kind' : 'lizard'}
print(pets)
print(len(pets))
pets.append(pet3)
print(pets)
print(len(pets))

# 종(kind)이 알고 싶을 때
print(pet3['kind'])
pet1 = pets[0]
pet2 = pets[1]
print(pet1['kind'])
print(pet2['kind'])