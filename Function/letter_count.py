#define single_letter_count below:
def single_letter_count(word, letter):
    return word.lower().count(letter.lower())

print(single_letter_count("hello world", "l"))
print(single_letter_count("fuck you", "z"))