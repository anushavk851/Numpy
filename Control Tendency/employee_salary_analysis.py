#20 Find:Mean,Median,Q1,Q3,IQR,Outlier,Mean after removing the outlier and Median after removing the outlier
salary = np.array([20000, 22000, 25000, 27000, 30000, 32000, 35000, 100000])
print("mean:",np.mean(salary))
print("median:",np.median(salary))
Q1=np.percentile(salary,25)
print("Q1:",Q1)
Q3=np.percentile(salary,75)
print("Q3:",Q3)
IQR=Q3-Q1
print("Inter quartile range(IQR):",IQR)
lower_bound=Q1-1.5* IQR
upper_bound=Q3+1.5*IQR
outliers=[]
for i in salary:
    if i<lower_bound or i>upper_bound:
        outliers.append(int(i))
print("outliers =",outliers)

removing_outliers=[]
for i in salary:
    if i<lower_bound or i>upper_bound:
        pass
    else:
        removing_outliers.append(int(i))
print("list after removing outliers:",removing_outliers)
print("mean after removing outliers:",np.mean(removing_outliers))
print("median after removing outliers:",np.median(removing_outliers))
