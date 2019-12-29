# RSA
# GeekTechStuff

from sympy import randprime, isprime

def create_rsa_r_8():
    # Generates an 8-bit key
    p = 0
    q = 0
    r = 257
    while r > 256:
        # 1st prime (p)
        p = randprime(2,250)
        # 2nd prime (q)
        q = randprime(2,250)
        if p == q:
            # 1st prime (p)
            p = randprime(2,250)
            # 2nd prime (q)
            q = randprime(2,250)
        # RSA modulus (R) of both primes (p * q)
        r = p * q
    # Euler's totient
    e = (p-1)*(q-1)
    print("Euler = ",e)
    return(r)

rsa = create_rsa_r_8()
print("RSA modulus (r) = ",rsa)