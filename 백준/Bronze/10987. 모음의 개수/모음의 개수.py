word = str(input())
vowel = ['a', 'e', 'i', 'o', 'u']
count = 0

for letter in word :
    if letter in vowel :
        count += 1

print(count)
