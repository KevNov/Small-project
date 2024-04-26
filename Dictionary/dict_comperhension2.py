biodata = {
    "Name" : "Kevin Noufal R.S",
    "Is a succesful person" : "no",
    "Fav food" : "burger",
    "Going to commit seppuku" : "probably",
    "Fav Vtuber" : "usada pekora",
    "Dream cars" : "BMW M8"
}

newbio = {k.upper(): (v.upper() if v == 'usada pekora' else v) for k,v in biodata.items()}
print(newbio)

#newnum = {num: ("YAHOO" if num % 3 == 0 else "meh") for num in list(range(1,31))}
#print(newnum)