import numpy as np
import math
def levy(n, m, beta):
    num = math.gamma(1 + beta) * math.sin(math.pi * beta / 2)
    den = math.gamma((1 + beta) / 2) * beta * (2 ** ((beta - 1) / 2))
    sigma_u = (num / den) ** (1 / beta)
    u = np.random.normal(scale=sigma_u, size=(n, m))
    v = np.random.normal(size=(n, m))
    z = u / (np.abs(v) ** (1 / beta))
    return z

