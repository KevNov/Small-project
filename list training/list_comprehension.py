#create the list where there's only E,T,M
answer = [person[0].upper() for person in ["Elie", "Tim", "Matt"]]
print(answer)

#list for even value
answer2 = [num for num in [1,2,3,4,5,6] if num % 2 == 0]
print(answer2)

#list where output should be [3,4]
answer3 = [num for num in [1,2,3,4] if num in [3,4,5,6]]
print(answer3)

#reverse the word and using lower case
answer4 = [person[::-1].lower() for person in ["Elie", "Tim", "Matt"]]
print(answer4)

#create a list of number where it can be divided by 12\
answer5 = [num for num in range(1,101) if num % 12 == 0]
print(answer5)

#create the list of word "amazing" without the vowels word (aiueo)
answer6 = [char.lower() for char in "amazing" if char not in "aiueo"]
print(answer6)

#nested list comprehension
answer7 =[[num for num in range(0,10)]for num in range(0,10)]
print(answer7)