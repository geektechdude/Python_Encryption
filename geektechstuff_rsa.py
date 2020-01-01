# RSA
# GeekTechStuff

from sympy import randprime, isprime

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
print("RSA(r) = ",r)
# Euler's totient
e = (p-1)*(q-1)
print("Euler = ",e)
# Public key - relative prime, greater than 1 and less than Euler's totient
pub_key = randprime(2,e)
print("Public Key: ",pub_key)
# Private key generation
d = 0
while d < 1000000000:
    if (pub_key * d) % e == 1:
        break
    d = d+1
priv_key = d
print("Private Key: ",priv_key)
   

# Trying above to encrypt ASCII A
print("Converting A to its ASCII value")
ascii = ord("A")
print("ASCII value of A is: ",ascii)
print("Attempting to encrypt A")
m = ascii

cipher_text = (m**pub_key)%r
print("(",m,"**",pub_key,") %",r )
print("Ciphered letter becomes ASCII:",cipher_text)
  
c = cipher_text
decrypt_text = (c**priv_key)%r
print("(",c,"**",priv_key,") %",r)
print("Decrypted letter becomes ASCII:",decrypt_text)
    
if m == decrypt_text:
    print("Success!!")

def cipher_message(message):
    encrypt_text = []
    for letter in message:
        m = ord(letter)
        cipher_text = (m**pub_key)%r
        encrypt_text.append(cipher_text)
    print(encrypt_text)
    return(encrypt_text)

def decrypt_message(message):
    decrypt_text = ""
    for letter in message:
        c = letter
        decrypt_letter = (c**priv_key)%r
        ascii_convert = chr(decrypt_letter)
        decrypt_text = decrypt_text + ascii_convert
    print(decrypt_text)
    return(decrypt_text)

# Testing
test = cipher_message("geektechstuff is an awesome website")
decrypt_message(test)
