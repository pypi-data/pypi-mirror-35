import random

class E(object):
    MODES = [
        (0, 1),
        (0, 2),
        (1, 2)
    ]

    BASE_E = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    @classmethod
    def batch_generate(cls, rand, n):  
        ret = []
        for i in range(n * 2):
            ret.append(E.generate(rand))
        return ret

    @classmethod
    def generate(cls, rand):
        e = E.BASE_E

        def _g(e):
            for i in range(6):
                ind = random.randint(0, 2)
                swap_s, swap_t = E.MODES[ind]
                e[swap_s], e[swap_t] = e[swap_t], e[swap_s]
            return e

        ret_temp = [_g(e) for i in range(3)]
        ret = []
        zero = [0, 0, 0]
        for i in range(3):
            for j in range(3):
                # print i, j
                # print ret_temp[i][j]
                if i == 0:
                    ret.append(ret_temp[i][j] + [0, 0, 0, 0, 0, 0])
                elif i == 1:
                    ret.append([0, 0, 0] + ret_temp[i][j] + [0, 0, 0])
                else:
                    ret.append([0, 0, 0, 0, 0, 0] + ret_temp[i][j])
        return ret
    
    @classmethod
    def multiple(cls, A, B, n):
        ret = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    ret[i][j] = ret[i][j] + A[i][k] * B[k][j]

        return ret