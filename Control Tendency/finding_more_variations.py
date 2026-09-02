#Find which dataset have more variations
a = np.array([10, 10, 10, 10, 10])
b = np.array([5, 10, 15, 20, 25])
a_var=np.var(a)
b_var=np.var(b)
if a_var>b_var:
    print(f'dataset {a} have more variations with varience of {a_var}')
else:
    print(f'dataset {b} have more variations with varience of {b_var}')
