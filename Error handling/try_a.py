# solving error using try

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None
    
d = {"name": "kevnov", "age": 25}
print(get(d, "color"))
