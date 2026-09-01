#to change shape or dimension of array without changing its data
arr7=np.arange(1,13)
arr7.reshape(4,3)

#1 Convert it into a 3 × 4 matrix.
print("1",a.reshape((3,4)))
#2 Convert it into a 4 × 3 matrix.
print("2",a.reshape((4,3)))
#3 Convert it into a 2 × 6 matrix.
print("3",a.reshape((2,6)))
#4 Convert it into a 6 × 2 matrix.
print("4",a.reshape((6,2)))
#5 Convert it into a 3-dimensional array with shape (2, 2, 3).
print("5",a.reshape((2,2,3)))
#6 Create numbers from 1 to 20 and reshape them into 4 × 5.
a=np.arange(1,21)
print("6",a.reshape((4,5)))
#7 Create numbers from 1 to 24 and reshape them into 2 × 3 × 4.
b=np.arange(1,25)
print("7",b.reshape((2,3,4)))
#8 Create a 3 × 4 matrix from below array using and then flatten it.
c=np.arange(1,13)
d=c.reshape((3,4))
print("8",d.flatten())
