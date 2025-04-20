# Step 1: Create a list of scores from user input
scores_input = input("Enter the scores separated by space: ")
scores = list(map(int, scores_input.split()))

print("Original scores:", scores)

# Step 2: Append a new score
new_score = int(input("Enter a new score to append: "))
scores.append(new_score)
print("After appending {}: {}".format(new_score, scores))

# Step 3: Remove a specific score
remove_score = int(input("Enter a score to remove: "))
if remove_score in scores:
    scores.remove(remove_score)
    print("After removing {}: {}".format(remove_score, scores))
else:
    print("Score {} not found in the list.".format(remove_score))

# Step 4: Sort the list
scores.sort()
print("Sorted list:", scores)

# Step 5: Find max, min, average
maximum = max(scores)
minimum = min(scores)
average = sum(scores) / len(scores)
print("Maximum: {}, Minimum: {}, Average: {:.2f}".format(maximum, minimum, average))

# Step 6: Reverse the list
scores.reverse()
print("Reversed:", scores)
