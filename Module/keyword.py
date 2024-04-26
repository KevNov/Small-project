import keyword

def contains_keyword(*words):
    for item in words:
        if keyword.iskeyword(item):
            return True
    return False

print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))
print(contains_keyword("four", "for", "if"))
print(contains_keyword("blah", "doggo", "crab", "anchor"))
    