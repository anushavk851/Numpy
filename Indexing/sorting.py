#SORTING in 1D
x=np.array([7,2,8,3])
#ascending
print("asc",np.sort(x))
#decending
print("desc",np.sort(x)[::-1])


#SORTING 2D
b=np.array([[9,1,8,3],
            [4,5,6,5],
            [8,9,3,11],
            [13,7,15,16]])
print("asc-row",np.sort(b,axis=1)) #sorting by row
print("asc-col",np.sort(b,axis=0)) #sorting by column
print("desc-col",np.sort(b,axis=0)[::-1]) #sorting column in descending order
print("asc-row",np.sort(b,axis=1)[::-1])#sorting row in descending order
