a = [1,2,3,4,5]
b = [4,4,3,2,1]

c = [x+y for x,y in zip(a,b)]
print(c)

d = [a[i] + b[i] for i in range(len(a))]
print(d)