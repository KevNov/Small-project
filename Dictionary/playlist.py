playlist = {
    'title' : 'trip to MSU',
    'owner' : 'kevnov',
    'songs' : [
        {'title' : 'waist down', 'artist' : ['Albert queque'], 'duration' : 3.3},
        {'title' : '7 years', 'artist' : ['Lucas graham'], 'duration' : 2.5},
        {'title' : 'make me', 'artist' : ['britney spear', 'G-easy'], 'duration' : 4.3},
        {'title' : 'we are young', 'artist' : ['Fun', 'Janelle Monae'], 'duration' : 3.5},
        {'title' : 'I cry', 'artist' : ['Florida'], 'duration' : 2.7}
    ]

}

for songs in playlist['songs']:
    print(songs['title'])

total_duration = 0
for songs in playlist['songs']:
    total_duration += songs['duration']
    print(total_duration)
