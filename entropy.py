import math
import string
def get_pool_size(password):
    N=0
    if any(char in string.ascii_lowercase for char in password):
        N=N+26
    if any(char in string.ascii_uppercase for char in password):
        N=N+26
    if any(char in string.digits for char in password):
        N=N+10
    if any(char in string.punctuation for char in password):
        N=N+32
    return N
def calculate_entropy(password):
    L=len(password)
    N=get_pool_size(password)
    if N==0:
        return 0
    else:
        E=L*(math.log2(N))
        return E