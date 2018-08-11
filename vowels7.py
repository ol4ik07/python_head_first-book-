vowels=set('aeiou')
word=input("Provide a word to search for vowels:")
word=word.lower()
found=vowels.intersection(set(word))
for vowel in found:
    print (vowel)
