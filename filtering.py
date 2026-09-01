#FILTERING
 #refers to process of selecting elements from an array that matching given conditions

ages=np.array([[21,17,19,20,16,30,18,65],
               [39,22,15,99,18,19,20,21]])
teenagers=ages[ages<18]
adults=ages[(ages>=18)&(ages<65)]
seniorcz=ages[ages>65]
even=ages[ages%2==0]
odd=ages[ages%2!=0]
print("teenagers:",teenagers)
print("adults:",adults)
print("senior citizen:",seniorcz)
print("even:",even)
print("odd:",odd)

#WHERE
 #we use where to preserve the orginal shape of data
ages=np.array([[21,17,19,20,16,30,18,65],
               [39,22,15,99,18,19,20,21]])
adults=np.where(ages>=18,ages,0) #here 0 is a default value given when condition is wrong,we can use any default value
print(adults)
