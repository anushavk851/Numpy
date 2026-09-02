#19 Find:Mean,Median,25th percentile,75th percentile,IQR,Outliers,Variance and Standard deviation
marks = np.array([45, 50, 52, 55, 60, 62, 65, 70, 72, 95])
print("mean:",np.mean(marks))
print("median:",np.median(marks))
print("25th percentile",np.percentile(marks,25))
print("75th percentile:",np.percentile(marks,75))
Q1=np.percentile(marks,25)
Q3=np.percentile(marks,75)
IQR=Q3-Q1
print("Inter Quartile Range:",IQR)
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
outliers=[]
for i in a:
    if i<lower_bound or i>upper_bound:
        outliers.append(int(i))
print("outliers:",outliers)
print("varience:",np.var(marks))
print("standard deviation:",np.std(marks))
