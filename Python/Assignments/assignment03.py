n = 5
student_data = {}

for i in range(n):
    name= input("Enter student name: ")
    score = int(input("Enter student score: "))
    student_data[name] = score

#Calculating average score

total = sum(student_data.values())
avg_score = total/5
print(f'Average score is: {avg_score}')

# Find Highest Scorer
highest_scorer = max(student_data, key=student_data.get)
print(f'Highest scorer: {highest_scorer}')

# Find Lowest Scorer
lowest_scorer = min(student_data, key=student_data.get)
print(f'Lowest scorer: {lowest_scorer}')
