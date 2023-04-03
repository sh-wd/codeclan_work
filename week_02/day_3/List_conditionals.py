# # numbers = range(1, 11)
# # print(numbers)
# print(even_squared = [number * number for number in range(1, 11) if number % 2 == 0])

# # for number in numbers:
# #     if number %2 == 0:
# #         even_squared.append(number * number)

# # print(even_squared)

# # even_squared = [expression for item in list of conditional]

# ages = [5, 15, 64, 27, 84, 26]

# odd_ages = [age for age in ages if age % 2 != 0]

# print(odd_ages)

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]

found_over_10 = [name for name in chicken_names if len(name) > 10]
print(found_over_10)

found_h = [name for name in chicken_names if name[0] == "H"]
print(found_h)

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

letters = [word[0].lower() for word in words]
print(letters)