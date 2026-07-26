import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    print(type(A))
    A_arr=np.array(A)
    print(type(A_arr))
    return A_arr.T
    # pass
