a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 1. Find the sum of all elements.
print(np.sum(a))

# 2. Find the maximum value in the entire array.
print(np.max(a))

# 3. Find the minimum value in the entire array.
print(np.min(a))

# 4. Find the mean of the entire array.
print(np.mean(a))

# 5. Find the sum of each row.
print(np.sum(a,axis=1))

# 6. Find the sum of each column.
print(np.sum(a,axis=0))

# 7. Find the maximum value from each row.
print(np.max(a,axis=1))

# 8. Find the minimum value from each column.
print(np.min(a,axis=0))

# 9. Find the mean of each row.
print(np.mean(a,axis=1))

# 10. Find the mean of each column.
print(np.mean(a,axis=0))

# 11. Find the index of the maximum value in the entire array.
print(np.argmax(a))

# 12. Find the index of the minimum value in the entire array.
print(np.argmin(a))
