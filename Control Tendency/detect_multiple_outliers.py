#8 Detect multiple outliers
a = np.array([5, 7, 8, 10, 11, 12, 13, 15, 50, 60])
Q1=np.percentile(a,25)
Q3=np.percentile(a,75)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
outliers=[]
for i in a:
    if i<lower_bound or i>upper_bound:
        outliers.append(int(i))
print("outliers:",outliers)
