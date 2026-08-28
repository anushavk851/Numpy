#1. Create a 4 × 4 identity matrix and change all diagonal elements to 5.
arr=np.eye((4),dtype=int)
b=arr*5
print(b)

# 2. Create a 3 × 5 array filled with the value 7.
a=np.ones((3,5),dtype=int)
b=a*7
print(b)

# 3. Create an array containing numbers from 1 to 100, with a step of 10.
print(np.arange(1,101,10))

# 4. Create 6 equally spaced numbers between 10 and 50.
print(np.linspace(10,50,6))

# 5. Create a 5 × 5 matrix of zeros and change the middle element to 1.
a=np.zeros((5,5),dtype=int)
a[2,2]=1
print(a)

# 6. Create a 4 × 4 matrix of ones and change the first row to zeros.
a=np.ones((4,4),dtype=int)
a[0,:]=0
print(a)

# 7. Create an array of numbers from 1 to 30 and reshape it into a 5 × 6 matrix.
a=np.arange(1,31)
print(a.reshape((5,6)))

# 8. Create a 3 × 3 matrix containing numbers from 1 to 9 using NumPy special-array functions.
a=np.arange(1,10)
print(a.reshape((3,3)))
