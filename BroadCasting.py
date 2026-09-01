#BROADCASTING
 #broadcasting allows numpy to perform operations on array. with different between 2 or more arrays,numpy will virtually expands
 #its dimension so that the smaller array matches the larger arrays in shape
#RULES
 #2 arrays are compatible when matching each dimensions either the dimensions need the same size or one of the dimension have size of one

array1=np.array([[1,2,3,4]])
array2=np.array([[1],[2],[3],[4]])
print(array1.shape)#(1,4)
print(array2.shape) #(4, 1) both are not equal but atleast one is 1(atleast one row is 1 and 1 col is 1)
print(array1*array2)
# array3=np.array([[1,2,3,4],[5,6,7,8]]) #(2,4)
# array4=np.array([[1],[2],[3],[4]])     #(4,1) 
# #operands could not be broadcast together with shapes(2,4),(4,1)
# print(array3*array4) #shows error
array3=np.array([[1,2,3,4],[5,6,7,8],[5,4,3,2],[2,6,9,4]]) #(4,4)
array4=np.array([[1],[2],[3],[4]]) # (4,1)
#here at least one is a match(4) and one is 1
print(array3*array4)


#exercise
array1=np.array([[1,2,3,4,5,6,7,8,9,10]])                    #(1,10)
array2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])  #(10,1)
print(array1*array2) 
