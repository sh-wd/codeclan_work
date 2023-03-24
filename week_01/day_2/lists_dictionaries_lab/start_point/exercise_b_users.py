users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
Jonathons_twitter = users["Jonathan"]["twitter"]
print(Jonathons_twitter)

# 2. Get Erik's hometown
eriks_hometown = users["Erik"]["home_town"]
print(eriks_hometown)

# 3. Get the list of Erik's lottery numbers
eriks_lottery_numbers = users["Erik"]["lottery_numbers"]
print(eriks_lottery_numbers)

# 4. Get the species of Avril's pet Monty
montys_species = users["Avril"]["pets"][0]["species"]
print(montys_species)

# 5. Get the smallest of Erik's lottery numbers
ordered_list = sorted(users["Erik"]["lottery_numbers"])
print(ordered_list)
lowest_number = ordered_list[0]
print(lowest_number)

# 6. Return an list of Avril's lottery numbers that are even
avrils_numbers = users["Avril"]["lottery_numbers"]

even_numbers = []

for number in avrils_numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({"name":"fluffy","species":"dog"})
print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary
users["Scott"] = ""
print(users)