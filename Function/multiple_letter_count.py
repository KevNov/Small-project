# using general dict comperhencsion

#char_count = {char: char.count(char) for char in "iamasurgeon"}
#print(char_count)
#char_count2 = {char: char.count(char) for char in "summer"}
#print(char_count2)

# using function

def multiple_count(letter):
    return {char: letter.count(char) for char in letter}

print(multiple_count("masturbate"))
print(multiple_count("trojan horse"))
print(multiple_count("latter sucker"))
