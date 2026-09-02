# Find 25th,50th and 75th percentile
a = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print("25th percentile:",np.percentile(a,25))
print("50th percentile:",np.percentile(a,50))
print("75th percentile:",np.percentile(a,75))


# Find the middle 50% range
a = np.array([5, 8, 10, 12, 15, 18, 20, 25, 30])
Q1=np.percentile(a,25)
Q3=np.percentile(a,75)
print(f'the range lies between {Q1} and {Q3}')
