import pprint

message = 'It was a sunny yet cold day in rainy Seattle, with the winter arriving and clock striking noon'
count = {}

for character in message:
    character = character.lower()
    count.setdefault(character,0)
    count[character] += 1

pprint.pprint(count)
print('\n')

words = message.split()
equal_word_count = {}

for word in words:
    word = word.lower()
    equal_word_count.setdefault(word,0)
    equal_word_count[word] += 1

pprint.pprint(equal_word_count)
    
