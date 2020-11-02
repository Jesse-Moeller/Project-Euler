import numpy as np

def seq(i):
    k=np.ceil(i/2)
    if i%2==0:
        return 2*k+1
    else:
        return k

