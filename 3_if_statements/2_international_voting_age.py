
voting_ages = {
    "Pakistan": 18,
    "America": 21,
    "Turkey": 26,
    "India":  30,
}

age = int(input("Please enter your age: "))

for country, voting_age in voting_ages.items():
    if age >= voting_age:
        print(f"You can vote in , {country} !!")
    else:
        print(f"You can't vote in , {country}..")
