numbers = [1,2,3,4,5]
names = ["Ben","Jane","Phoebe"]
chickens = [
    {"name": "Margaret", "age": 2, "eggs": 0},
    {"name": "Hetty", "age": 1, "eggs": 2},
    {"name": "Henrietta", "age": 3, "eggs": 3},
]

for number in numbers:
    print(number*2)

for name in names:
    print(name)

total_eggs = 0

for chicken in chickens:
    print(f"{chicken['name']} is {chicken['age']}")
    total_eggs += chicken['eggs']
                    
print(f"Total eggs: {total_eggs}")