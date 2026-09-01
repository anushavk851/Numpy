a = np.array([10, 20, 30, 40, 50, 60, 70, 80])
#1 Print the first element.
print("1:",a[0])
#2 Print the last element.
print("2:",a[-1])
#3 Print the first 4 elements.
print("3:",a[0:4])
#4 Print elements from index 2 to 6.
print("4:",a[2:7])
#5 Print every second element.
print("5:",a[1:8:2])
#6 Print the array in reverse order.
print("6:",a[::-1])
#7 Print the last 3 elements.
print("7:",a[5:8])

b= np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
#1 Extract the first row.
print("1:",b[0])
#2 Extract the last row.
print("2:",b[-1])
#3 Extract the first column.
print("3:",b[:,0])
#4 Extract the last column.
print("4:",b[:,-1])
#5 Extract the first 2 rows.
print("5:",b[0:2])


b= np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

#6 Extract the last 2 columns.
print("6:",b[:,2:4])
#7 Extract:  6 7
 #          10 11
print("7:",b[1:3,1:3])
#8 Extract the middle 2 × 2 matrix.
print("8:",b[1:3,1:3])
#9 Reverse the rows.
print("9:",b[::-1,:])
#10 Reverse the columns.
print("9:",b[:,::-1])
