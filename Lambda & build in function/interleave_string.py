# a function that accept 2 string and return that string in a new form of string

def interleave(*str):
    return ''.join(''.join(word) for word in zip(str))
    
print(interleave('hi','ha'))
print(interleave('aaa', 'zzz'))
print(interleave('lzr','iad'))

# still didn't get this thing
