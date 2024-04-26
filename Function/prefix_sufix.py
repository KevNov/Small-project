# combine a word using function

def combine_word(word,**kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    return word

print(combine_word("horse"))
print(combine_word("under", suffix= "wear" ))
print(combine_word("thing", prefix= "man"))
print(combine_word("onee", suffix= "-chan"))
print(combine_word("ordinate", prefix= "sub"))