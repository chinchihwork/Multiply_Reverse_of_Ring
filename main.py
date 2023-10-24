import numpy as np

class FIND_REVERSE():
    def __init__ (self , module : int):
        self.q = np.int64(module)

    def extended_gcd(self , a , b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.extended_gcd(b % a, a)
            return (g, y - (b // a) * x, x)

    def mod_inverse(self , m):
        g, x, y = self.extended_gcd(self.q, m)
        if g != 1:
            raise ValueError("Modular inverse does not exist")
        else:
            return x % m
    

if __name__ == "__main__":
    module = 3034699991
    delta = int(module / 257003)
    test = FIND_REVERSE(module)
    ans = test.mod_inverse(delta)
    print(ans)