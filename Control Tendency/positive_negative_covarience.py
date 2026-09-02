# Find cov(x, y) and cov(x, z).which relation is positive and which is negative
x = np.array([10, 20, 30, 40, 50])
y = np.array([15, 25, 35, 45, 55])
z = np.array([50, 40, 30, 20, 10])

covar_xy=np.cov(x,y)
print("Covarience of x and y:",covar_xy)
if covar_xy[0,1]<0:
    print("cov(x,y) is negative covarience")
else:
    print("cov(x,y) is positive covarience")

covar_xz=np.cov(x,z)
print("Covarience of x and z:",covar_xz)
if covar_xz[0,1]<0:
    print("cov(x,z) is negative covarience")
else:
    print("cov(x,z) is positive covarience")
