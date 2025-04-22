import gmpy2

# 返回e的模逆元d
def euclidean_algorithm(e, phi_n):
    r_oldest, r = e, phi_n
    s_oldest, s = 1, 0
    t_oldest, t = 0, 1
    if phi_n == 0:
        # return s_oldest, t_oldest, e
        return s_oldest
    while r != 0:
        q = gmpy2.f_div(r_oldest, r)
        r_oldest, r = r, gmpy2.sub(r_oldest, gmpy2.mul(q, r))
        s_oldest, s = s, gmpy2.sub(s_oldest, gmpy2.mul(q, s))
        t_oldest, t = t, gmpy2.sub(t_oldest, gmpy2.mul(q, t))
    # return s_oldest, t_oldest, r_oldest
    return s_oldest