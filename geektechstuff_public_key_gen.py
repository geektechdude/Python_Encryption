# Public Key Generation Algorithm
# GeekTechStuff

# Choose 2 prime numbers (larger is better)
p = 7
q = 13

# Calculate RSA modulus
r = p * q
print(r)

# Computer Euler's totient function (ETF)
x = (p-1)*(q-1)
print("Euler's totient function is:",x)

# e will be the public key
e = input("Pick a number that is greater than 1, is a prime number and that cannot divide Euler's totient function: ")
e = int(e)

d = 0
while d < 1000000000:
    if (e * d) % x == 1:
        break
    d = d+1

print("RSA modulus: ",r)
print("Euler's toient function: ",x)
print("Public Key: ",e)
print("Private Key: ",d)
print(" ")

# Encrypt / Decrypt

# Encrypting a letter
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter = input("Enter a letter: ")
print("Encrypting:")
letter = letter.upper()
letter_position =alphabet.find(letter) 
cipher_position_enc = (letter_position ^ e) % r
encrypted_letter = alphabet[cipher_position_enc]
print(letter,"changes from", letter_position,"to",cipher_position_enc,"and becomes",encrypted_letter)

# Decrypting a letter
print("Decrypting:")
cipher_position_dec = (cipher_position_enc ^ d) % r
try:
    decrypted_letter = alphabet[cipher_position_dec]
    print(encrypted_letter,"at", cipher_position_enc,"becomes", decrypted_letter,"at",cipher_position_dec)
except:
    print("Error: The decrypted letter position is: ",cipher_position_dec," which is bigger than the 26 letter alphabet")
   
