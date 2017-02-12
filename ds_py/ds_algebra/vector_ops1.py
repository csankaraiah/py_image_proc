import numpy as np

def add_vector(a,b):
    return(a + b)

def sub_vector(a,b):
    return(a - b)

def scl_mul(a,b):
    return(a * b)


a = np.array([8.218,-9.341])
b = np.array([-1.129,2.111])
c = add_vector(a,b)

print c


a = np.array([7.119,8.215])
b = np.array([-8.223,0.878])
c = sub_vector(a,b)

print c

a = np.array([1.671,-1.012,-0.318])
b = 7.41

c = scl_mul(a,b)

print c

