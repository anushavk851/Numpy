#1 Find the mean
a = np.array([10, 20, 30, 40, 50])
print("mean:",np.mean(a))
#2 Find the median
a = np.array([12, 5, 8, 20, 15])
print("median:",np.median(a))
#3 Find the mode
a = np.array([2, 4, 4, 5, 6,4, 7, 8])
b=np.unique(a,return_counts=True)
print("mode is:",b[0][np.argmax(b[1])])

#3 Find both mean and median. Which one is more affected by the value 100?
a = np.array([10, 20, 30, 40, 100])
mean_a=np.mean(a)
median_a=np.median(a)
b=np.array([10, 20, 30, 40])
mean_b=np.mean(b)
median_b=np.median(b)
diff_mean=mean_a-mean_b
print(diff_mean)
diff_median=median_a-median_b
print(diff_median)
if diff_mean>diff_median:
    print("mean is more affected")
else:
    print("median is more affected")
