# return the longest and the shortest name in a list

def min_max_name(names):
    return (min(names ,key=lambda n: len(n)), max(names, key=lambda n: len(n)))

print(min_max_name(["tono","roy","elizabeth","daisuke","ilham"]))
print(min_max_name(["lavi","faiz","david","vergil","kevin"]))