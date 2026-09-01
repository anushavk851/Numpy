b=np.array([[9,1,8,3],
            [4,5,6,5],
            [8,9,3,11],
            [13,7,15,16]])
print("max",np.max(b))
print("min",np.min(b))
print("max in each col",np.max(b,axis=0))
print("max in each row",np.max(b,axis=1))
print("min in each col",np.min(b,axis=0))
print("min in each row",np.min(b,axis=1))
#index
print("index of max",np.argmax(b))
print("index of min",np.min(b))
print("index of max in each col",np.argmax(b,axis=0))
print("index of max in each row",np.argmax(b,axis=1))
print("index of min in each col",np.argmin(b,axis=0))
print("index of min in each row",np.argmin(b,axis=1))
