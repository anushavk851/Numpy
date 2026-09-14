#measure of control tendencey
print(np.mean(b))
print(np.median(b))
print(np.std(b))        #standard deviation
print(np.var(b))        #variance-deviation of data points from mean values(average),variants=std^2

a=np.array([[2,5,3],[6,3,4]])
print("mean:",np.mean(a))
print("row-wise mean:",np.mean(a,axis=1)) #mean of each row
print("col-wise mean:",np.mean(a,axis=1)) #each col
print("median:",np.median(a))
print("row-wise median:",np.median(a,axis=1)) #median of each row
print("col-wise median:",np.median(a,axis=0)) #median of each col
