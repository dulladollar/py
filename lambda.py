people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slyterin"}
]
def f(peron):
    return peron["name"]
# other whay of doing this is by replacing fuction f (def f(person):) and aply the next line. with lambda methode
# people.sort(key=lambda person: person["name"])

people.sort(key = f)

print(people)
