from random import choice

cars = choice(["toyota","daihatsu","mercedes-benz","wuling","honda","mitsubishi"])

#price in dolars ($)
wang_cars = {
    "BMW" : 75000,
    "Mazda" : 40000,
    "peugeot" : 65000,
    "honda" : 30000,
    "mercedes-benz" : 80000
}

price = wang_cars.get(cars)
if price:
    print(f"{price} in USD")
else:
    print("we dont sell this type of car here")
