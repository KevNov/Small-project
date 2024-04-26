names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# finds the minimum length of a name in names
min_names = min(names, key=lambda n:len(n)) # Tim
print(min_names)

# find the longest name itself
max_names = max(names, key=lambda n:len(n)) #Ollivander
print(max_names)

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
min(songs, key=lambda s: s['playcount']) #{"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title'] #YMCA