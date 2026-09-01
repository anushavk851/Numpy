#IQR Method-(Inter Quartile Range)
#IQR=Q3-Q1 (Q3-75TH PERCENTILE AND Q1 25TH PERCENTILE)

#Q3=np.percentile(arr_name,75)
#Q1=np.percentile(arr_name,25)

# lower_bound=Q1-1.5*IQR
# upper_bound=Q3+1.5*IQR

#outliers=arr_name[(arr_name>upper_bound)|(arr_name<lower_bound)]

a=np.array([19,22,26,200,2,32,29])
Q1=np.percentile(a,25)
Q3=np.percentile(a,75)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
print("lower_bound:",lower_bound)
print("upper bound:",upper_bound)

outliers=a[(a>upper_bound) | (a<lower_bound)]
print("outliers:",outliers)
data=[int(x) for x in a if x not in outliers]
print("result:",data)

#capping method
 #replacing extreame value with boundary values
a=np.clip(a,5,45)
print(a)
