str1 = "ABC"
str2 = "123"

#combo = {str1[i]: str2[i] for i in range (0, len(str1))}
#print(combo)

#conditional logic with dictionaries
new_list = { num : ("odd" if num %2 != 0 else "even" ) for num in range(1,21)}
print(new_list)

# recap
#dict_comp = {val: val % 3 == 0 for val in range(1,26)}
#print(dict_comp)

