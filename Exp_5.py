birthdays = {
    "Mohit": "15-01-1990",
    "Rohit": "10-07-1985",
    "Alexandar": "22-10-1992"
}


name = input("Enter a name: ")
if name in birthdays:
    birth_date = birthdays[name]
    birth_split = birth_date.split('-')
    print("Year:", birth_split[2], "Month:", birth_split[1], "Day:", birth_split[0])
    
    joined_date = "/".join(birth_split)
    print("Joined date:", joined_date)
else:
    print("No birthday found for", name)
