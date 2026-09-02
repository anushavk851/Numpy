#9 remove outliers
a = np.array([10, 12, 14, 15, 16, 18, 20, 100])
Q1=np.percentile(a,25)
Q3=np.percentile(a,75)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
outliers_removed=[]
for i in a:
    if i<lower_bound or i>upper_bound:
        pass
    else:
        outliers_removed.append(int(i))
print(outliers_removed)
