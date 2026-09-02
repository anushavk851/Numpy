# find correlations and check if the relationship strong or weak
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 3, 4, 2, 6])
corr = np.corrcoef(x, y)[0, 1]
print("Correlation:", corr)
if abs(corr) < 0.3:
    print("Weak relationship")
elif abs(corr) < 0.7:
    print("Moderate relationship")
else:
    print("Strong relationship")
