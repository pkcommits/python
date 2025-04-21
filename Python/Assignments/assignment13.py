from collections import defaultdict

def group_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        # Sort the word to get the key
        key = ''.join(sorted(word))
        anagram_dict[key].append(word)
    return list(anagram_dict.values())

# Input from user
user_input = input("Enter words separated by spaces: ")
words = user_input.strip().split()

# Grouping anagrams
result = group_anagrams(words)

# Output the result
print("Grouped Anagrams:")
for group in result:
    print(group)
