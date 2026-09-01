#all values except diagonal values are zero,diagonal value will be one
#gives default float values
arr4=np.eye(3)   #in case of sqaure matrix
print(arr4)
arr=np.eye(4,3)
print(arr)

# 1. Create a 4 × 4 identity matrix and change all diagonal elements to 5.
arr=np.eye((4),dtype=int)
b=arr*5
print(b)
