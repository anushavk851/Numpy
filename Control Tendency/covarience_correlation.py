#COVARIANCE
a=np.array([10,56,4,78,23,8,100])
b=np.array([11,45,78,3,8,44,9])
print("Covarience",np.cov(a,b))     #([cov(a,a) cov(a,b)][cov(y,x) cov(y,y)]) so we get matrix with 2x2
print("single value",np.cov(a,b)[0,1]) #to get single value

#CORRELATION
a=np.array([10,56,4,78,23,8,100])
b=np.array([11,45,78,3,8,44,9])
print("Correlation",np.corrcoef(a,b)) #to get correlation
print("single value",np.corrcoef(a,b)[0,1]) #to get single value
