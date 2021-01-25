num=[0,1,2,3,4]
binary=["0","1","10","11","100"]

z=zip(num,binary)
ans={num:binary for num,binary in z}
print(ans)