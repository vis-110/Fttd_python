student_mark = [87, 42, 67, 41, 35, 89, 77]

for s in range(len(student_mark)):
    for r in range(len(student_mark)):
        if student_mark[s] < student_mark[r]:
            temp = student_mark[s]
            student_mark[s] = student_mark[r]
            student_mark[r] = temp

print(student_mark)