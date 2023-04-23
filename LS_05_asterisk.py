# 1. Последовательностью Фибоначчи называется последовательность чисел 
# a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def FibN(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return FibN(n-1)+FibN(n-2)
    
print(FibN(12))