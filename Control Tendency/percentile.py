a=np.array([10,20,30,40,50])

#0th percentile (0th percentile is minimum value)
print("0th percentile:",np.percentile(a,0))

#25th percentile(Q1)(first quarter value)
print("25th percentile:",np.percentile(a,25))

#50th percentile(Q2)
print("50th percentile:",np.percentile(a,50))

#75th percentile(Q3)
print("75th percentile:",np.percentile(a,75))

#100th percentile-returns max value 
print("100th percentile:",np.percentile(a,100))

