input = [1,2,3,5]
output = [i for i in input]
print(output)

input1 = ['a','b','aad','abc','sss']
output = [i for i in input1 if 'a' in i]
print(output)

input2 = ['a','b','aad','abc','sss']
output = [i if 'a' in i else 'no' for i in input1]
print(output)

sentence = 'The rocket, who was named Ted, came back \
... from Mars because he missed his friends.'
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
consonants = [i for i in sentence if is_consonant(i)]
print(consonants)

# ChatGPT
# can elif be used inside list comprehensive ?

# No, you cannot use elif directly within a list comprehension. 
# List comprehensions are concise ways to create lists in Python, and they are designed to be simple and compact. 
# They are meant for cases where you are performing a single operation on each element of an iterable.

# If you need to handle multiple conditions using if, elif, and else, it's better to use a regular for loop or 
# a more advanced approach like using a generator expression along with the itertools module's chain function. 