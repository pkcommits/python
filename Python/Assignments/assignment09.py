import string
from collections import Counter

# Step 1: Take input from the user
text = input("Enter a paragraph: ")

# Step 2: Remove punctuation and convert to lowercase
cleaned_text = ''
for char in text:
    if char not in string.punctuation:
        cleaned_text += char.lower()

# Step 3: Split into words
words = cleaned_text.split()

# Step 4: Count frequency using Counter
word_counts = Counter(words)

# Step 5: Get the top 5 most common words
top_5 = word_counts.most_common(5)

# Step 6: Display the result
for word, count in top_5:
    print(f"{word}: {count}")
