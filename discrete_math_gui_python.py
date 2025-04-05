import math

ALPHA = {'A': '01', 'B': '02', 'C': '03', 'D': '04', 'E': '05', 'F': '06', 'G': '07', 'H': '08', 'I': '09',
              'J': '10', 'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18',
              'S': '19', 'T': '20', 'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25', 'Z': '26', ' ': '27'}



print("""Let’s build a public key (n,e)! 
Enter two distinct prime numbers for A's key: p and q""")


def prime_test(val):
    prime_num = [2, 3, 5, 7]

    if val < 2:
        return "NOT PRIME"

    if val in prime_num:
        return "PRIME"

    for i in prime_num:
        if val % i == 0:
            return "NOT PRIME"
        else:
            continue

    n = math.sqrt(val)
    n = math.floor(n)

    for i in range(11, n + 1, 2):
        if val % i == 0:
            return "NOT PRIME"
    return "PRIME"


def check_p_q_e(enter):
    while True:
        try:
            num = int(input(enter))
            prime_test_result = prime_test(num)
            if prime_test_result == "PRIME":
                if enter == "Enter an e value: ":
                    print("e and φ(n) are coprime.")
                    return int(num)
                else:
                    print(f"{num} is a prime number.")
                    return int(num)
            else:
                if enter == "Enter an e value: ":
                    print("e and φ(n) are not coprime.")
                else:
                    print(f"{num} is not a prime number.")
        except ValueError:
            print("Enter valid integer value.")


def compute_keys(user, e, d, n):
    e = int(e)
    n = int(n)
    d = int(d)
    print(f"""{user}'s key generation is complete! 
{user}'s public key is ({n}, {e}) and the private key is ({n}, {d}).""")
    user_keys = [(n,e),(n,d)]
    return user_keys


def translate(m):
    translation = ""
    for char in m:
        for key, value in ALPHA.items():
            if char == key:
                translation += ALPHA[char]
    return str(translation)


def signature(t, a_priv_key):
    while len(t) % 2 != 0:
        t = "0" + t

    n, d = a_priv_key[1]
    n = int(n)
    d = int(d)

    sign_block = ""
    for i in range(0, len(t), 2):
        block = t[i:i + 2]
        block = int(block)
        encrypt_t = pow(block, d, n)
        sign_block += str(encrypt_t) + " "

    sign_block = str(sign_block.rstrip(" "))
    return sign_block


def encryption(t,signed_m, b_pub_key):
    s = signed_m.split(" ")

    n, e = b_pub_key[0]
    n = int(n)
    e = int(e)

    while len(t) % 2 != 0:
        t = "0" + t

    t_block = ""
    for i in range(0, len(t), 2):
        block = t[i:i + 2]
        block = int(block)
        encrypt_t = pow(block, e, n)
        t_block += str(encrypt_t) + " "

    t_block = t_block.rstrip(" ")

    s_block = ""
    for block in s:
        block = int(block)
        encrypt_s = pow(block, e, n)
        s_block += str(encrypt_s) + " "

    s_block = s_block.rstrip(" ")

    encrypted = f"""{t_block}, {s_block}"""

    return str(encrypted)


def decrypt_num(ciphertext, b_priv_key):
    cipher = ciphertext.split(", ")
    c = cipher[0].split(" ")

    s = cipher[1].split(" ")

    n, d = b_priv_key[1]
    n = int(n)
    d = int(d)

    decrypt_numtext = ""
    for i in c:
        i = int(i)
        num = pow(i, d, n)
        num = str(num)
        if len(num) % 2 != 0:
            num = "0" + num
        decrypt_numtext += num

    decrypt_numtext = str(decrypt_numtext.rstrip(" "))

    decrypt_sig = ""
    for i in s:
        i = int(i)
        num = pow(i, d, n)
        num = str(num)
        if len(num) % 2 != 0:
            num = "0" + num
        decrypt_sig += num + " "

    decrypt_sig = str(decrypt_sig.rstrip(" "))

    decrypt = f"{decrypt_numtext}, {decrypt_sig}"

    return decrypt


def decrypt_plaintext(c, b_priv_key):
    c = c.split(",")
    c = c[0].split(" ")

    n, d = b_priv_key[1]
    n = int(n)
    d = int(d)

    decrypt_numtext = ""
    for i in c:
        i = int(i)
        num = pow(i, d, n)
        num = str(num)
        if len(num) % 2 != 0:
            num = "0" + num
        decrypt_numtext += num

    plaintext = ""
    for j in range(0, len(decrypt_numtext), 2):
        val = decrypt_numtext[j:j + 2]
        for key, value in ALPHA.items():
            if ALPHA[key] == val:
                plaintext += key
                break

    return str(plaintext)


def verification(decrypt, a_pub_key):
    decrypt = decrypt.split(", ")
    t = decrypt[0]
    s = decrypt[1].split(" ")  # decrypted signature

    n, e = a_pub_key[0]
    n = int(n)
    e = int(e)

    check_sig = ""
    for i in s:
        i = int(i)
        num = pow(i, e, n)
        num = str(num)
        if len(num) % 2 != 0:
            num = "0" + num
        check_sig += num

    check_sig = str(check_sig.rstrip(" "))

    print("Checking for Authentication...")
    if check_sig == t:
        print(f"Decrypted Signature: {check_sig}")
        print(f"Translated Plaintext: {t}")
        return "Signature Valid"
    else:
        print(f"Decrypted Signature: {check_sig}")
        print(f"Translated Plaintext: {t}")
        return "Signature Not Valid"


a_p = check_p_q_e("Enter a p value: ")
a_q = check_p_q_e("Enter a q value: ")

print()
a_n = a_p * a_q
print(f"Calculate n : {a_p} * {a_q} = {a_n}")

print()
a_tot = (a_p-1) * (a_q-1)
print(f"""Calculate Euler's Totient Function: 
tot(n) = φ(n) = ({a_p} - 1) * ({a_q} - 1) = {a_tot}""")

print()
print(f"""Enter any number for e where 1 < e < tot(n) and e is coprime to tot(n). 
Possible Choices: 17, 29, 41, 53""")
a_e = check_p_q_e("Enter a e value: ")

print()
while True:
    try:
        a_d = pow(a_e, -1, a_tot)
        break
    except ValueError:
        print("Base is not invertible for the given modulus. Try again")

print(f"""Calculate d:
Modular multiplicative inverse of e (mod tot(n)) = {a_d}""")

a_keys = compute_keys("A",a_e, a_d, a_n)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

b_p = check_p_q_e("Enter a p value: ")
b_q = check_p_q_e("Enter a q value: ")

print()
b_n = b_p * b_q
print(f"Calculate n : {b_p} * {b_q} = {b_n}")

print()
b_tot = (b_p-1) * (b_q-1)
print(f"""Calculate Euler's Totient Function: 
tot(n) = φ(n) = ({b_p} - 1) * ({b_q} - 1) = {b_tot}""")

print()
print(f"""Enter any number for e where 1 < e < tot(n) and e is coprime to tot(n). 
Possible Choices: 17, 29, 41, 53""")
b_e = check_p_q_e("Enter an e value: ")

print()
b_d = pow(b_e, -1, b_tot)
print(f"""Calculate d:
Modular multiplicative inverse of e (mod tot(n)) = {b_d}""")

b_keys = compute_keys("B",b_e, b_d, b_n)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

print("ENCRYPTION AND DECRYPTION")
print("""Encryption is done with c(m) = m^e mod n where c is the ciphertext and m is the message. 
Note that both of these values must be integers 1 < m < n and 1 < c < n
Decryption is done with m(c) = c^d mod n
KEY USED FOR TRANSLATING AND DECRYPTING:
A: 01, B: 02, C: 03, D: 04, E: 05, F: 06, G: 07, H: 08, I: 09,
J: 10, K: 11, L: 12, M: 13, N: 14, O: 15, P: 16, Q: 17, R: 18,
S: 19, T: 20, U: 21, V: 22, W: 23, X: 24, Y: 25, Z: 26, \' \': 27""")

while True:
    try:
        plaintext = input("Enter plaintext (m): ").upper()
        break
    except ValueError:
        print("Enter alphabetical characters only.")

print()
translated_m = translate(plaintext)
print(f"Translated plaintext : {translated_m}")

print()
sign_mssg = signature(translated_m, a_keys)
print(f"Signed Message : {sign_mssg}")

print()
ciphertext = encryption(translated_m, sign_mssg, b_keys)
print(f"""Encrypted Message (encrypted translated plaintext, encrypted signature) : 
{ciphertext}""")

print()
decrypt_num = decrypt_num(ciphertext, b_keys)
print(f"""Decrypt to Numerical Value (decrypt translated plaintext, decrypted signature) : 
{decrypt_num}""")

print()
decrypt_m = decrypt_plaintext(ciphertext, b_keys)
print(f"Decrypt to Numerical Value : {decrypt_m}")

authentication = verification(decrypt_num, a_keys)
print(authentication)
