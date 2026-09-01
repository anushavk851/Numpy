array=np.array([[0,1,2,3],
                [4,5,6,7],
                [8,9,10,11],
                [13,14,15,16]])
#for slicing we will use subscript operator
#array[start:end:step]

#row selection-in 2D array
print(array[1])    #[4,5,6,7]
print(array[3])    #[13,14,15,16]
print(array[-1])   #[13,14,15,16]
print(array[0:2])  #[[0 1 2 3][4 5 6 7]]
print(array[2:])   #[[ 8  9 10 11][13 14 15 16]]
print(array[0:4:2])#[[ 0  1  2  3][ 8  9 10 11]]
print(array[::2])  #[[ 0  1  2  3][ 8  9 10 11]]
print(array[::-1]) #[[13 14 15 16][ 8  9 10 11][ 4  5  6  7][ 0  1  2  3]]
print(array[::-2]) #[[13 14 15 16][ 4  5  6  7]]

array=np.array([[0,1,2,3],
                [4,5,6,7],
                [8,9,10,11],
                [13,14,15,16]])

#column selection-multidimension slicing in 2D array
print(array[:,0])      #[ 0  4  8 13] every rows 0th column
print(array[:,-1])     #[ 3  7 11 16] every rows last column
print(array[1,3])      #7 first row ,3rd column value
print(array[:,0:3])    #[[ 0  1  2][ 4  5  6][ 8  9 10][13 14 15]] print all rows and  column from 0 to 2 index
print(array[:,::-1])   #[[ 3  2  1  0][ 7  6  5  4][11 10  9  8][16 15 14 13]] rows are in correct order but columns are reversed
print(array[:,2:4])    #[[ 2  3][ 6  7][10 11][15 16]] all rows 2nd and 3rd column is printed
print(array[1:3,2:4])  #[[ 6  7][10 11]] print rows from 1 and 2 nd index and column of 2nd and 3rd index
print(array[0,1:])     #[1 2 3] 1st index row and colum from index 1 to last
print(array[0:2,0:2])  #[[0 1][4 5]] 1st 2 rows and first 2 column
