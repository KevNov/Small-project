# create biodata

personal_data = {
    "Name" : "Kevin Noufal R.S",
    "Age" : 24,
    "Is a succesful person" : False,
    "Fav food" : "burger",
    "Going to commit suicide" : True,
    "Fav Vtuber" : "Usada pekora",
    "Dream cars" : "BMW M8"
}

#print(personal_data["Fav Vtuber"])
#print(personal_data["Going to commit suicide"])
#print(personal_data.get("phone"))
#print(personal_data.items())

for data in personal_data.values():
    print(data)

for k,v in personal_data.items():
    print(f"key is {k} and the result is {v}")

#lisst = dict.fromkeys(["name","age","gender"], 'unknown')
#print(lisst)
#print("phone" in personal_data)
#print("Dream cars" in personal_data)


