#21 Find: Mean of hours,Mean of marks,Variance of hours,Variance of marks,Covariance and Correlation
hours = np.array([1, 2, 3, 4, 5, 6])
marks = np.array([40, 45, 55, 60, 70, 80])
print("mean of hours:",np.mean(hours))
print("mean of marks:",np.mean(marks))
print("varience of hours:",np.var(hours))
print("varience of marks:",np.var(marks))
print("covarience:",np.cov(hours,marks))
print("correlation:",np.corrcoef(hours,marks))
