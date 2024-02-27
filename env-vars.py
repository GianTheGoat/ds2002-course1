#!/Users/gianbaez/anaconda3/bin/python3

import os

Fav_City = input("What is your favorite city?")
Fav_Drink = input("What is your favorite drink?")
Fav_Sport = input("What is your favorite sport?")

os.environ["Fav_City"] = Fav_City
os.environ["Fav_Drink"] = Fav_Drink
os.environ["Fav_Sport"] = Fav_Sport

print(os.getenv("Fav_City"))
print(os.getenv("Fav_Drink"))
print(os.getenv("Fav_Sport"))
