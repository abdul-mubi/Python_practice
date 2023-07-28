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