import string

def clean_text(text):
    # Convert to lowercase and remove punctuation
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))

def plagiarism_checker(doc1, doc2):
    # Clean the texts
    doc1_clean = clean_text(doc1)
    doc2_clean = clean_text(doc2)

    # Convert to sets of words
    set1 = set(doc1_clean.split())
    set2 = set(doc2_clean.split())

    # Find common words
    common_words = set1.intersection(set2)

    # Calculate Jaccard similarity (intersection over union)
    union_words = set1.union(set2)
    similarity = (len(common_words) / len(union_words)) * 100

    # Display results
    print(f"Common Words: {common_words}")
    print(f"Similarity: {similarity:.2f}%")

# Example usage
doc1 = input("Enter first sentence: ")
doc2 = input("Enter second sentence: ")
plagiarism_checker(doc1, doc2)
