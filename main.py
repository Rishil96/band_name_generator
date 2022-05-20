# Project 1
# Band Name Generator

# greet user
print("Welcome to the Band Name Generator!")

# get city name input from user
city = input("What's the name of the city you grew up in?\n")

# get pet name input from user
pet = input("What's the name of your pet?\n")

# concatenate the city and pet name to print the final band name
print(f"Your Band name could be {city.title() + ' ' + pet.title()}")
