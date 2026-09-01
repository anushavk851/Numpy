import numpy as np

#1 Generate 5 random numbers between 0 and 1.
print(np.random.rand())

#2 Generate a 3 × 3 matrix of random numbers between 0 and 1.
print(np.random.random((3,3)))

#3 Generate 10 random integers between 1 and 50.
print(np.random.randint(1,51,10))

#4 Generate a 4 × 5 matrix containing random integers between 10 and 100.
print(np.random.randint(10,101,size=(4,5)))

#5 Generate 5 random integers between 1 and 20 without repetition.
a=np.arange(1,21)
print(np.random.choice(a,5,replace=False))

#6 Generate a random number between 1 and 100 and check whether it is even or odd.
a=np.random.randint(1,100)
print(a)
if a%2==0:
    print("Even")
else:
    print("ODD")

#7 Generate a 3 × 3 random matrix and find its maximum value.
a=np.random.randint(1,100,size=(3,3))
print(a)
print(np.max(a))

#8 Generate a 5 × 5 random matrix and find the sum of each row.
a=np.random.randint(1,20,size=(5,5))
print(a)
print(np.sum(a))

#9 Generate 20 random integers between 1 and 100 and find:maximum,minimum,mean and standard deviation
a=np.random.randint(1,101,20)
print(a)
print("Maximum:",np.max(a))
print("Minimum:",np.min(a))
print("Mean:",np.mean(a))
print("Standard Deviation:",np.std(a))
  
