import numpy as np

a = np.array([1,2,3,4])

print(a.size)
a.ndim
a.shape

a[0]
d=a[1:4]
print(d)

u=np.array([1,0])
v=np.array([0,1])
z=u+v

print(z)

for n, m in zip(u,v):
    z.append(n+m)
