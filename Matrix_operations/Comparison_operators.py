#using comparison operators we can create boolean array,filter data and use element wise comparisons
scores=np.array([91,55,100,73,82,64])
print(scores==100)
print(scores!=100)
print(scores>=60)
print(scores<60)

scores[scores<60]=0  #any score less than 60 will be assigned as 0
print(scores)
