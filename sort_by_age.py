def sort_by_age(persons):
    return sorted(persons, key=lambda person: person[1])
    
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people = sort_by_age(people)
print(sorted_people)
