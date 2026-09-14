import numpy as np
marks = np.array([
    [78, 85, 90, 67],
    [88, 76, 95, 82],
    [65, 70, 72, 80],
    [92, 89, 85, 94]
])

# 1. Find the average marks of all students.
print(np.average(marks,axis=1))
# 2. Find the highest mark in the entire array.
print(np.max(marks))
# 3. Find the lowest mark in the entire array.
print(np.min(marks))
# 4. Find the average marks of each student.
print(np.average(marks,axis=1))
# 5. Find the highest mark of each student.
print(np.max(marks,axis=1))
# 6. Find the lowest mark of each student.
print(np.min(marks,axis=1))
# 7. Find the average mark for each subject.
print(np.average(marks,axis=0))
# 8. Find the highest mark in each subject.
print(np.max(marks,axis=0))
# 9. Find the lowest mark in each subject.
print(np.min(marks,axis=0))
# 10. Find the student with the highest average marks.
average=np.average(marks,axis=1)
print(max(average))
# 11. Find the subject with the highest average marks.
average=np.average(marks,axis=0)
print(max(average))
# 12. Find the standard deviation of each student's marks.
print(np.std(marks,axis=1))
# 13. Find the variance of each subject.
print(np.var(marks,axis=0))
# 14. Find the position/index of the highest mark in the entire array.
print(np.argmax(marks))
# 15. Find the position/index of the lowest mark in the entire array.
print(np.argmin(marks))
# 16. Find the total marks of all students.
print(np.sum(marks))








