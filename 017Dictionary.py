sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry":22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

print(sensors)
print(num_cameras)

# Create a new dictionary and adding new values.
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0

print(animals_in_zoo)

# Adding more than one values at a time
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids)

# Overwrite the value 
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"


# Zip method to unify two different list in to Dictionary
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks =zip(drinks, caffeine)

print(zipped_drinks)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

drinks_to_caffeine2 = {key:value for key, value in zip(drinks, caffeine)}
print(drinks_to_caffeine2)

# Playlist Example
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key, value in zip(songs,playcounts)}

print(plays)
plays["Purple Haze"] = 1
plays["Respect"] = 94
library = {"The Best Songs":plays, "Sunday Feelings":{}}
print(library)

