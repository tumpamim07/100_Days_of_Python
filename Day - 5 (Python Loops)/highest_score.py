student_scores = [180, 124, 165, 142, 185, 150, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]


#1st Option
print(sum(student_scores))


#2nd Option
sum = 0
for score in student_scores:
    sum += score
print("Total Score:",sum)

#1st option
print(max(student_scores))


#2nd Option
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f"Max Score: {max_score}")