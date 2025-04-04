import tkinter as tk
import math

alpha_code = {'A': '01', 'B': '02', 'C': '03', 'D': '04', 'E': '05', 'F': '06', 'G': '07', 'H': '08', 'I': '09',
              'J': '10', 'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18',
              'S': '19', 'T': '20', 'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25', 'Z': '26', ' ': '27'}


def primality_test_p():
    try:
        num = int(entry_p.get())

        prime_num = [2, 3, 5, 7]

        if num < 2:
            result = f"{num} is a not a prime number."
            result_label_p.config(text=result)
            return

        if num in prime_num:
            result = f"{num} is prime number."
            result_label_p.config(text=result)
            return

        for i in prime_num:
            if num % i == 0:
                result = f"{num} is a not prime number."
                result_label_p.config(text=result)
                return
            else:
                continue

        n = math.sqrt(num)
        n = math.floor(n)

        for i in range(11, n + 1, 2):
            if num % i == 0:
                result = f"{num} is a not prime number."
                result_label_p.config(text=result)
                return
        result = f"{num} is a prime number."
        result_label_p.config(text=result)
        return

    except ValueError:
        result_error = """Error
        Please enter a valid prime integer."""
        result_label_p.config(text=result_error,
                              anchor="w")
        return


def primality_test_q():
    try:
        num = int(entry_q.get())

        prime_num = [2, 3, 5, 7]
        if num < 2:
            result = f"{num} is a not a prime number."
            result_label_q.config(text=result)
            return

        if num in prime_num:
            result = f"{num} is a prime number."
            result_label_q.config(text=result)
            return

        for i in prime_num:
            if num % i == 0:
                result = f"{num} is a not prime number."
                result_label_q.config(text=result)
                return
            else:
                continue

        n = math.sqrt(num)
        n = math.floor(n)

        for i in range(11, n + 1, 2):
            if num % i == 0:
                result = f"{num} is a not prime number."
                result_label_q.config(text=result)
                return
        result = f"{num} is a prime number."
        result_label_q.config(text=result)
        return

    except ValueError:
        result_error = """Error
        Please enter a valid prime integer."""
        result_label_q.config(text=result_error,
                              anchor="w")


def primality_test_p_b():
    try:
        num = int(entry_p_b.get())

        prime_num = [2, 3, 5, 7]

        if num < 2:
            result = f"{num} is a not a prime number."
            result_label_p_b.config(text=result)
            return

        if num in prime_num:
            result = f"{num} is prime number."
            result_label_p_b.config(text=result)
            return

        for i in prime_num:
            if num % i == 0:
                result = f"{num} is a not prime number."
                result_label_p_b.config(text=result)
                return
            else:
                continue

        n = math.sqrt(num)
        n = math.floor(n)

        for i in range(11, n + 1, 2):
            if num % i == 0:
                result = f"{num} is a not prime number."
                result_label_p_b.config(text=result)
                return
        result = f"{num} is a prime number."
        result_label_p_b.config(text=result)
        return

    except ValueError:
        result_error = """Error
        Please enter a valid prime integer."""
        result_label_p_b.config(text=result_error,
                                anchor="w")
        return


def primality_test_q_b():
    try:
        num = int(entry_q_b.get())

        prime_num = [2, 3, 5, 7]
        if num < 2:
            result = f"{num} is a not a prime number."
            result_label_q_b.config(text=result)
            return

        if num in prime_num:
            result = f"{num} is a prime number."
            result_label_q_b.config(text=result)
            return

        for i in prime_num:
            if num % i == 0:
                result = f"{num} is a not prime number."
                result_label_q_b.config(text=result)
                return
            else:
                continue

        n = math.sqrt(num)
        n = math.floor(n)

        for i in range(11, n + 1, 2):
            if num % i == 0:
                result = f"{num} is a not prime number."
                result_label_q_b.config(text=result)
                return
        result = f"{num} is a prime number."
        result_label_q_b.config(text=result)
        return

    except ValueError:
        result_error = """Error
        Please enter a valid prime integer."""
        result_label_q_b.config(text=result_error,
                                anchor="w")
        return


def calculate_n(p, q):
    if p == "" or "not prime" in result_label_p.cget("text"):
        result_label_n.config(text="Enter a prime p value.",
                              anchor="w")
        return
    elif q == "" or "not prime" in result_label_q.cget("text"):
        result_label_n.config(text="Enter a prime q value.",
                              anchor="w")
        return

    if "Error" in result_label_q.cget("text") or "Error" in result_label_p.cget("text"):
        result_label_n.config(text="Enter a valid prime integer.",
                              anchor="w")
        return

    p = int(p)
    q = int(q)
    n = p * q
    result_label_n.config(text=n,
                          anchor="w")
    return


def calculate_n_b(p, q):
    if p == "" or "not prime" in result_label_p_b.cget("text"):
        result_label_n.config(text="Enter a prime p value.",
                              anchor="w")
        return
    elif q == "" or "not prime" in result_label_q_b.cget("text"):
        result_label_n_b.config(text="Enter a prime q value.",
                                anchor="w")
        return

    if "Error" in result_label_q_b.cget("text") or "Error" in result_label_p_b.cget("text"):
        result_label_n_b.config(text="Enter a valid prime integer.",
                                anchor="w")
        return

    p = int(p)
    q = int(q)
    n = p * q
    result_label_n_b.config(text=n,
                            anchor="w")
    return



def euler_totient(p, q):
    p_prime = "is a prime" in result_label_p.cget("text")
    q_prime = "is a prime" in result_label_q.cget("text")
    if p_prime and q_prime:
        p = int(p)
        q = int(q)
        f = (p - 1) * (q - 1)
        result_label_f.config(text=f,
                              anchor="w")
        return
    else:
        #print(result_label_p.cget("text"))
        #print(result_label_q.cget("text"))
        result_label_f.config(text="Enter valid input to continue.",
                              anchor="w")
        return


def euler_totient_b(p, q):
    p_prime = "is a prime" in result_label_p_b.cget("text")
    q_prime = "is a prime" in result_label_q_b.cget("text")
    if p_prime and q_prime:
        p = int(p)
        q = int(q)
        f = (p - 1) * (q - 1)
        result_label_f_b.config(text=f,
                                anchor="w")
        return
    else:
        result_label_f_b.config(text="Enter valid input to continue.",
                                anchor="w")
        return


def coprime_e(e="", f=""):
    try:
        if e == "" or f == "":
            result_label_e.config(text="Insufficient data. Enter correct values to continue.",
                                  anchor="w")
            return

        num = int(entry_e.get())

        e = int(e)
        f = int(f)

        prime_num = [2, 3, 5, 7]
        if num < 2:
            result_label_e.config(text="e and φ(n) are not coprime. Try again.",
                                  anchor="w")
            return

        if num in prime_num:
            result = True
            if 1 < e < f and result is True:
                result_label_e.config(text="e and φ(n) are coprime! Continue.",
                                      anchor="w")
                return
            else:
                result_label_e.config(text="e and φ(n) are not coprime. Try again.",
                                      anchor="w")
                return

        for i in prime_num:
            if num % i == 0:
                result_label_e.config(text="e and φ(n) are not coprime. Try again.",
                                      anchor="w")
                return
            else:
                continue

        n = math.sqrt(num)
        n = math.floor(n)

        for i in range(11, n + 1, 2):
            if num % i == 0:
                result_label_e.config(text="e and φ(n) are not coprime. Try again.",
                                      anchor="w")
                return
        result = True
        if 1 < e < f and result is True:
            result_label_e.config(text="e and φ(n) are coprime! Continue.",
                                  anchor="w")
            return
        else:
            result_label_e.config(text="e and φ(n) are not coprime. Try again.",
                                  anchor="w")
            return

    except ValueError:
        result_error = """Error
        Please enter a valid prime integer."""
        result_label_e.config(text=result_error,
                              anchor="w")


def coprime_e_b(e="", f=""):
    try:
        if e == "" or f == "":
            result_label_e_b.config(text="Insufficient data. Enter correct values to continue.",
                                    anchor="w")
            return

        num = int(entry_e_b.get())

        e = int(e)
        f = int(f)

        prime_num = [2, 3, 5, 7]
        if num < 2:
            result_label_e_b.config(text="e and φ(n) are not coprime. Try again.",
                                    anchor="w")
            return

        if num in prime_num:
            result = True
            if 1 < e < f and result is True:
                result_label_e_b.config(text="e and φ(n) are coprime! Continue.",
                                        anchor="w")
                return
            else:
                result_label_e_b.config(text="e and φ(n) are not coprime. Try again.",
                                        anchor="w")
                return

        for i in prime_num:
            if num % i == 0:
                result_label_e_b.config(text="e and φ(n) are not coprime. Try again.",
                                        anchor="w")
                return
            else:
                continue

        n = math.sqrt(num)
        n = math.floor(n)

        for i in range(11, n + 1, 2):
            if num % i == 0:
                result_label_e_b.config(text="e and φ(n) are not coprime. Try again.",
                                        anchor="w")
                return
        result = True
        if 1 < e < f and result is True:
            result_label_e_b.config(text="e and φ(n) are coprime! Continue.",
                                    anchor="w")
            return
        else:
            result_label_e_b.config(text="e and φ(n) are not coprime. Try again.",
                                    anchor="w")
            return

    except ValueError:
        result_error = """Error
        Please enter a valid prime integer."""
        result_label_e_b.config(text=result_error,
                                anchor="w")


def compute_d(e, f):
    if "coprime" in str(result_label_e.cget("text")):
        if "valid" not in str(result_label_f.cget("text")):
            e = int(e)
            f = int(f)

            d = pow(e, -1, f)
            result_label_d.config(text=d,
                                  anchor="w")
            return
        else:
            result_label_d.config(text="Insufficient data. Enter correct values to continue.",
                                  anchor="w")
            return
    else:
        result_label_d.config(text="Insufficient data. Enter correct values to continue.",
                              anchor="w")
        return


def compute_d_b(e, f):
    if "coprime" in str(result_label_e_b.cget("text")):
        if "valid" not in str(result_label_f_b.cget("text")):
            e = int(e)
            f = int(f)

            d = pow(e, -1, f)
            result_label_d_b.config(text=d,
                                    anchor="w")
            return
        else:
            result_label_d_b.config(text="Insufficient data. Enter correct values to continue.",
                                    anchor="w")
            return
    else:
        result_label_d_b.config(text="Insufficient data. Enter correct values to continue.",
                                anchor="w")
        return


def compute_keys(e, d, n):
    e = int(e)
    n = int(n)
    d = int(d)
    key_generation_text = f"""A's key generation is complete! 
    A's public key is ({n}, {e}) and the private key is ({n}, {d})."""

    result_label_keys.config(text=key_generation_text,
                             anchor="w")
    return


def compute_keys_b(e, d, n):
    e = int(e)
    n = int(n)
    d = int(d)
    key_generation_text = f"""B's key generation is complete! 
    B's public key is ({n}, {e}) and the private key is ({n}, {d})."""

    result_label_keys_b.config(text=key_generation_text,
                               anchor="w")
    return


def translate(m):
    try:
        translation = ""
        m = str(m)
        m = m.upper()

        for char in m:
            for key, value in alpha_code.items():
                if char == key:
                    translation += alpha_code[char]

        result_label_m.config(text=translation,
                              anchor="w")
        return

    except ValueError:
        result_error = """Error
        Please enter a valid plaintext (alphabetical letters)."""
        result_label_m.config(text=result_error,
                              anchor="w")
        return


def signature(m, a_priv_key):
    try:
        m = str(m)
        while len(m) % 2 != 0:
            m = "0" + m

        d, n = a_priv_key
        n = int(n)
        d = int(d)

        sign_block = ""
        for i in range(0, len(m), 2):
            block = m[i:i + 2]
            block = int(block)
            encrypt_m = pow(block, d, n)
            sign_block += str(encrypt_m) + " "

        sign_block = sign_block.rstrip(" ")

        result_label_sig.config(text=sign_block)
        return
    except ValueError:
        result_error = """Error
        Please enter plaintext to sign."""
        result_label_sig.config(text=result_error,
                                anchor="w")
        return


def encryption(translate_mssg, mssg_sign, b_pub_key):
    try:
        t = str(translate_mssg)
        sign = mssg_sign.split(" ")
        s = sign

        n, e = b_pub_key
        n = int(n)
        e = int(e)

        t = str(t)
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

        encrypted = str(t_block) + ",\n" + str(s_block)

        result_label_enc.config(text=str(encrypted))
        return
    except ValueError:
        result_error = """Error
        Please enter a valid plaintext before encryption."""
        result_label_enc.config(text=result_error,
                                anchor="w")
        return


def decryption_num(ciphertext, b_priv_key):
    try:
        cipher = ciphertext.split(",")
        cipher = cipher[0].split(" ")

        n, d = b_priv_key
        n = int(n)
        d = int(d)

        decrypt_numtext = ""
        for i in cipher:
            i = int(i)
            num = pow(i, d, n)
            num = str(num)
            if len(num) % 2 != 0:
                num = "0" + num
            decrypt_numtext += num

        result_label_dec_num.config(text=decrypt_numtext)
        return
    except ValueError:
        print(ciphertext)
        result_error = """Error
                        Please enter a valid plaintext before encryption."""
        result_label_dec_num.config(text=result_error,
                                    anchor="w")
        return


def decryption_alpha(ciphertext, b_priv_key):
    try:
        cipher = ciphertext.split(",")
        cipher = cipher[0].split(" ")

        n, d = b_priv_key
        n = int(n)
        d = int(d)

        decrypt_numtext = ""
        for i in cipher:
            i = int(i)
            num = pow(i, d, n)
            num = str(num)
            if len(num) % 2 != 0:
                num = "0" + num
            decrypt_numtext += num

        plaintext = ""
        for j in range(0, len(decrypt_numtext), 2):
            val = decrypt_numtext[j:j + 2]
            for key, value in alpha_code.items():
                if alpha_code[key] == val:
                    plaintext += key
                    break

        result_label_dec_alpha.config(text=plaintext)
        return
    except ValueError:
        print(ciphertext)
        result_error = """Error
                        Please enter a valid plaintext before encryption."""
        result_label_dec_num.config(text=result_error,
                                    anchor="w")
        return


def signature_verification(mssg, b_priv_key, a_pub_key):
    try:
        enc = mssg.split(",")

        cipher = enc[0].split(" ")
        b_n, b_d = b_priv_key
        b_n = int(b_n)
        b_d = int(b_d)

        decrypt_numtext = ""
        for i in cipher:
            i = int(i)
            num = pow(i, b_d, b_n)
            num = str(num)
            if len(num) % 2 != 0:
                num = "0" + num
            decrypt_numtext += num

        enc_sign = enc[1].split(" ")

        decrypt_sig = ""
        for i in enc_sign:
            i = int(i)
            num = pow(i, b_d, b_n)
            num = str(num)
            if len(num) % 2 != 0:
                num = "0" + num
            decrypt_sig += num

        n, e = a_pub_key
        n = int(n)
        e = int(e)

        s_block = ""
        for j in range(0, len(decrypt_sig), 2):
            block = decrypt_sig[j:j + 2]
            block = int(block)
            encrypt_s = pow(block, e, n)
            encrypt_s = str(encrypt_s)
            if len(encrypt_s) % 2 != 0:
                encrypt_s = "0" + encrypt_s
            s_block += str(encrypt_s)

        s_block = s_block.rstrip(" ")

        if decrypt_numtext == s_block:
            result_label_verif.config(text="Signature Valid")
            return
        else:
            result_label_verif.config(text="Signature Valid")
            return
    except ValueError:
        result_error = """Error
                Please enter plaintext before decryption."""
        result_label_verif.config(text=result_error,
                                  anchor="w")
        return


# Create main window
window = tk.Tk()
window.title("RSA Calculator")

# Definite Values
WIDTH = 800
HEIGHT = 650
FONT = "Courier" # Computer Style Font
MAIN_BACKGROUND_COLOR = "#b2c1c7"  # light grey/blue

# Window Size
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(True, True)

main_canvas = tk.Canvas(window,
                        bg=MAIN_BACKGROUND_COLOR)
main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=main_canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

main_canvas.configure(yscrollcommand=scrollbar.set)

main_frame = tk.Frame(main_canvas,
                      bg=MAIN_BACKGROUND_COLOR
                      )

window_id = main_canvas.create_window((0, 0), window=main_frame, anchor="nw")


def update_scroll_region(event):
    main_canvas.configure(scrollregion=main_canvas.bbox("all"))

main_frame.bind("<Configure>", update_scroll_region)

# RSA LABEL
rsa_label = tk.Label(main_frame,
                     text="RSA Calculator",
                     font=(FONT, 40, "bold"),
                     width=15,
                     relief="raised"
                     )
rsa_label.pack(anchor="nw",
               pady=10,
               padx=10)

# KEY GENERATION TEXT IN A LABEL
key_gen_text = """Let’s build a public key (n,e)! 
Enter two distinct prime numbers for A's key: p and q"""

key_gen_label = tk.Label(main_frame,
                         text=key_gen_text,
                         justify="left",
                         font=(FONT, 15))
key_gen_label.pack(padx=5,
                   anchor="w")

# P FRAME TO HOLD (LABEL, INPUT, MESSAGE)
# P INPUT
p_frame = tk.Frame(main_frame)
p_frame.pack(anchor="w",
             padx=10,
             pady=10)
label_p = tk.Label(p_frame,
                   text="Enter p : ",
                   font=(FONT, 15))
label_p.pack(padx=10,
             pady=10,
             anchor="nw",
             side="top")

entry_p = tk.Entry(p_frame,
                   font=(FONT, 13))  # Input field
entry_p.pack(pady=5,
             padx=10,
             anchor="nw",
             side="top")

result_label_p = tk.Label(p_frame, text="", font=(FONT, 12))
result_label_p.pack(anchor="w", padx=10, pady=10)

button_p = tk.Button(p_frame,
                     text="Submit",
                     font=(FONT, 13),
                     command=primality_test_p)
button_p.pack(anchor="w", padx=10, pady=5, side="left")

# Q FRAME TO HOLD (LABEL, INPUT, MESSAGE)
# Q INPUT
q_frame = tk.Frame(main_frame)
q_frame.pack(anchor="w",
             padx=10,
             pady=10)
label_q = tk.Label(q_frame,
                   text="Enter q : ",
                   font=(FONT, 15))
label_q.pack(padx=10,
             pady=10,
             anchor="nw",
             side="top")

entry_q = tk.Entry(q_frame,
                   font=(FONT, 13))
entry_q.pack(pady=5,
             padx=10,
             anchor="nw",
             side="top")

result_label_q = tk.Label(q_frame, text="", font=(FONT, 12))
result_label_q.pack(anchor="w", padx=10, pady=10)

button_p = tk.Button(q_frame,
                     text="Submit",
                     font=(FONT, 13),
                     command=primality_test_q)
button_p.pack(anchor="w",
              padx=10,
              pady=5,
              side="left")

# N FRAME TO HOLD (LABEL, MESSAGE, CALCULATION)
# N CALCULATION
n_frame = tk.Frame(main_frame)
n_frame.pack(anchor="w",
             padx=10,
             pady=10)
label_n = tk.Label(n_frame,
                   text="Calculate : n = p * q",
                   font=(FONT, 15))
label_n.pack(padx=10,
             pady=10,
             anchor="nw",
             side="top")

result_label_n = tk.Label(n_frame, text="", font=(FONT, 12))
result_label_n.pack(anchor="w", padx=10, pady=10)

button_n = tk.Button(n_frame,
                     text="Calculate n",
                     font=(FONT, 13),
                     command=lambda: calculate_n(entry_p.get(),
                                                 entry_q.get()))
button_n.pack(anchor="w",
              padx=10,
              pady=5,
              side="left")

# F FRAME TO HOLD (LABEL, MESSAGE, CALCULATION)
# EULEUR CALCULATION
f_frame = tk.Frame(main_frame)
f_frame.pack(anchor="w",
             padx=10,
             pady=10)
label_f_text = "Calculate Euler's Totient Function: tot(n) = φ(n) = (p - 1) * (q - 1)"
label_f = tk.Label(f_frame,
                   text=label_f_text,
                   font=(FONT, 15))
label_f.pack(padx=10,
             pady=10,
             anchor="nw",
             side="top")

result_label_f = tk.Label(f_frame, text="", font=(FONT, 12))
result_label_f.pack(anchor="w", padx=10, pady=10)

button_f = tk.Button(f_frame,
                     text="Calculate φ(n)",
                     font=(FONT, 13),
                     command=lambda: euler_totient(entry_p.get(),
                                                   entry_q.get()))
button_f.pack(anchor="w",
              padx=10,
              pady=5,
              side="left")

# E FRAME TO HOLD (LABEL, INPUT, MESSAGE)
# E INPUT
e_frame = tk.Frame(main_frame)
e_frame.pack(anchor="w",
             padx=10,
             pady=10)

tot = str(result_label_f.cget("text"))
label_e_text = """Enter any number for e where 1 < e < tot(n) and e is coprime to tot(n).
Possible Choices: 17, 29, 41, 53"""

label_e = tk.Label(e_frame,
                   text=label_e_text,
                   font=(FONT, 15))
label_e.pack(padx=10,
             pady=10,
             anchor="nw",
             side="top")

entry_e = tk.Entry(e_frame,
                   font=(FONT, 13))
entry_e.pack(pady=5,
             padx=10,
             anchor="nw",
             side="top")

result_label_e = tk.Label(e_frame, text="", font=(FONT, 12))
result_label_e.pack(anchor="w", padx=10, pady=10)

button_e = tk.Button(e_frame,
                     text="Calculate e",
                     font=(FONT, 13),
                     command=lambda: coprime_e(entry_e.get(),
                                               result_label_f.cget("text")))
button_e.pack(anchor="w",
              padx=10,
              pady=5,
              side="left")

# D FRAME TO HOLD (LABEL, MESSAGE, CALCULATION)
# D CALCULATION
d_frame = tk.Frame(main_frame)
d_frame.pack(anchor="w",
             padx=10,
             pady=10)
label_d_text = "Calculate d : modular multiplicative inverse of e (mod tot(n))"
label_d = tk.Label(d_frame,
                   text=label_d_text,
                   font=(FONT, 15))
label_d.pack(padx=10,
             pady=10,
             anchor="nw",
             side="top")

result_label_d = tk.Label(d_frame, text="", font=(FONT, 12))
result_label_d.pack(anchor="w", padx=10, pady=10)

button_d = tk.Button(d_frame,
                     text="Calculate d",
                     font=(FONT, 13),
                     command=lambda: compute_d(entry_e.get(),
                                               result_label_f.cget("text")))
button_d.pack(anchor="w",
              padx=10,
              pady=5,
              side="left")

# KEY GENERATION COMPLETE
# PUBLIC AND PRIVATE KEYS
key_frame = tk.Frame(main_frame)
key_frame.pack(anchor="w", padx=10, pady=10)

result_label_keys = tk.Label(key_frame,
                             text="",
                             font=(FONT, 12))
result_label_keys.pack(anchor="w",
                       padx=10,
                       pady=10)

button_keys = tk.Button(key_frame,
                        text="Compute Your Keys",
                        font=(FONT, 13),
                        command=lambda: compute_keys(entry_e.get(),
                                                     result_label_d.cget("text"),
                                                     result_label_n.cget("text")))
button_keys.pack(anchor="w",
                 padx=10,
                 pady=5,
                 side="left")

# B KEYS

# KEY GENERATION TEXT IN A LABEL
key_gen_text_b = """Let’s build a public key (n,e)! 
Enter two distinct prime numbers for B's key: p and q"""

key_gen_label_b = tk.Label(main_frame,
                           text=key_gen_text_b,
                           justify="left",
                           font=(FONT, 15))
key_gen_label_b.pack(padx=5,
                     anchor="w")

# P FRAME TO HOLD (LABEL, INPUT, MESSAGE)
# P INPUT
p_frame_b = tk.Frame(main_frame)
p_frame_b.pack(anchor="w",
               padx=10,
               pady=10)
label_p_b = tk.Label(p_frame_b,
                     text="Enter p : ",
                     font=(FONT, 15))
label_p_b.pack(padx=10,
               pady=10,
               anchor="nw",
               side="top")

entry_p_b = tk.Entry(p_frame_b,
                     font=(FONT, 13))  # Input field
entry_p_b.pack(pady=5,
               padx=10,
               anchor="nw",
               side="top")

result_label_p_b = tk.Label(p_frame_b, text="", font=(FONT, 12))
result_label_p_b.pack(anchor="w", padx=10, pady=10)

button_p_b = tk.Button(p_frame_b,
                       text="Submit",
                       font=(FONT, 13),
                       command=primality_test_p_b)
button_p_b.pack(anchor="w", padx=10, pady=5, side="left")

# Q FRAME TO HOLD (LABEL, INPUT, MESSAGE)
# Q INPUT
q_frame_b = tk.Frame(main_frame)
q_frame_b.pack(anchor="w",
               padx=10,
               pady=10)
label_q_b = tk.Label(q_frame_b,
                     text="Enter q : ",
                     font=(FONT, 15))
label_q_b.pack(padx=10,
               pady=10,
               anchor="nw",
               side="top")

entry_q_b = tk.Entry(q_frame_b,
                     font=(FONT, 13))
entry_q_b.pack(pady=5,
               padx=10,
               anchor="nw",
               side="top")

result_label_q_b = tk.Label(q_frame_b, text="", font=(FONT, 12))
result_label_q_b.pack(anchor="w", padx=10, pady=10)

button_p_b = tk.Button(q_frame_b,
                       text="Submit",
                       font=(FONT, 13),
                       command=primality_test_q_b)
button_p_b.pack(anchor="w",
                padx=10,
                pady=5,
                side="left")

# N FRAME TO HOLD (LABEL, MESSAGE, CALCULATION)
# N CALCULATION
n_frame_b = tk.Frame(main_frame)
n_frame_b.pack(anchor="w",
               padx=10,
               pady=10)
label_n_b = tk.Label(n_frame_b,
                     text="Calculate : n = p * q",
                     font=(FONT, 15))
label_n_b.pack(padx=10,
               pady=10,
               anchor="nw",
               side="top")

result_label_n_b = tk.Label(n_frame_b, text="", font=(FONT, 12))
result_label_n_b.pack(anchor="w", padx=10, pady=10)

button_n_b = tk.Button(n_frame_b,
                       text="Calculate n",
                       font=(FONT, 13),
                       command=lambda: calculate_n_b(entry_p_b.get(),
                                                     entry_q_b.get()))
button_n_b.pack(anchor="w",
                padx=10,
                pady=5,
                side="left")

# F FRAME TO HOLD (LABEL, MESSAGE, CALCULATION)
# EULEUR CALCULATION
f_frame_b = tk.Frame(main_frame)
f_frame_b.pack(anchor="w",
               padx=10,
               pady=10)
label_f_text_b = "Calculate Euler's Totient Function: tot(n) = φ(n) = (p - 1) * (q - 1)"
label_f_b = tk.Label(f_frame_b,
                     text=label_f_text_b,
                     font=(FONT, 15))
label_f_b.pack(padx=10,
               pady=10,
               anchor="nw",
               side="top")

result_label_f_b = tk.Label(f_frame_b, text="", font=(FONT, 12))
result_label_f_b.pack(anchor="w", padx=10, pady=10)

button_f_b = tk.Button(f_frame_b,
                       text="Calculate φ(n)",
                       font=(FONT, 13),
                       command=lambda: euler_totient_b(entry_p_b.get(),
                                                       entry_q_b.get()))
button_f_b.pack(anchor="w",
                padx=10,
                pady=5,
                side="left")

# E FRAME TO HOLD (LABEL, INPUT, MESSAGE)
# E INPUT
e_frame_b = tk.Frame(main_frame)
e_frame_b.pack(anchor="w",
               padx=10,
               pady=10)
tot_b = str(result_label_f_b.cget("text"))
label_e_text_b = """Enter any number for e where 1 < e < tot(n) and e is coprime to tot(n).
Possible Choices: 17, 29, 41, 53"""
label_e_b = tk.Label(e_frame_b,
                     text=label_e_text_b,
                     font=(FONT, 15))
label_e_b.pack(padx=10,
               pady=10,
               anchor="nw",
               side="top")

entry_e_b = tk.Entry(e_frame_b,
                     font=(FONT, 13))
entry_e_b.pack(pady=5,
               padx=10,
               anchor="nw",
               side="top")

result_label_e_b = tk.Label(e_frame_b, text="", font=(FONT, 12))
result_label_e_b.pack(anchor="w", padx=10, pady=10)

button_e_b = tk.Button(e_frame_b,
                       text="Calculate e",
                       font=(FONT, 13),
                       command=lambda: coprime_e_b(entry_e_b.get(),
                                                   result_label_f_b.cget("text")))
button_e_b.pack(anchor="w",
                padx=10,
                pady=5,
                side="left")

# D FRAME TO HOLD (LABEL, MESSAGE, CALCULATION)
# D CALCULATION
d_frame_b = tk.Frame(main_frame)
d_frame_b.pack(anchor="w",
               padx=10,
               pady=10)
label_d_text_b = "Calculate d : modular multiplicative inverse of e (mod tot(n))"
label_d_b = tk.Label(d_frame_b,
                     text=label_d_text_b,
                     font=(FONT, 15))
label_d_b.pack(padx=10,
               pady=10,
               anchor="nw",
               side="top")

result_label_d_b = tk.Label(d_frame_b, text="", font=(FONT, 12))
result_label_d_b.pack(anchor="w", padx=10, pady=10)

button_d_b = tk.Button(d_frame_b,
                       text="Calculate d",
                       font=(FONT, 13),
                       command=lambda: compute_d_b(entry_e_b.get(),
                                                   result_label_f_b.cget("text")))

button_d_b.pack(anchor="w",
                padx=10,
                pady=5,
                side="left")

# KEY GENERATION COMPLETE
# PUBLIC AND PRIVATE KEYS
key_frame_b = tk.Frame(main_frame)
key_frame_b.pack(anchor="w", padx=10, pady=10)

result_label_keys_b = tk.Label(key_frame_b,
                               text="",
                               font=(FONT, 12))
result_label_keys_b.pack(anchor="w",
                         padx=10,
                         pady=10)

button_keys_b = tk.Button(key_frame_b,
                          text="Compute Your Keys",
                          font=(FONT, 13),
                          command=lambda: compute_keys_b(entry_e_b.get(),
                                                         result_label_d_b.cget("text"),
                                                         result_label_n_b.cget("text")))
button_keys_b.pack(anchor="w",
                   padx=10,
                   pady=5,
                   side="left")

# ENCRYPTION AND DECRYPTION FRAME
enc_dec_frame = tk.Frame(main_frame)
enc_dec_frame.pack(anchor="w",
                   padx=10,
                   pady=10)

# ENCRYPTION AND DECRYPTION LABEL
encrypt_decrypt_label = tk.Label(enc_dec_frame,
                                 text="ENCRYPTION AND DECRYPTION",
                                 font=("Courier", 40, "bold"),
                                 width=25,
                                 relief="raised"
                                 )
encrypt_decrypt_label.pack(anchor="nw",
                           pady=10,
                           padx=10)

# ENCRYPTION AND DECRYPTION TEXT IN A LABEL
enc_dec_text = """Encryption is done with c(m) = m^e mod n where c is the ciphertext and m is the message. 
Note that both of these values must be integers 1 < m < n and 1 < c < n
Decryption is done with m(c) = c^d mod n
KEY USED FOR TRANSLATING AND DECRYPTING:
A: 01, B: 02, C: 03, D: 04, E: 05, F: 06, G: 07, H: 08, I: 09,
J: 10, K: 11, L: 12, M: 13, N: 14, O: 15, P: 16, Q: 17, R: 18,
S: 19, T: 20, U: 21, V: 22, W: 23, X: 24, Y: 25, Z: 26, \' \': 27"""

enc_dec_label = tk.Label(enc_dec_frame,
                         text=enc_dec_text,
                         justify="left",
                         font=(FONT, 15))
enc_dec_label.pack(padx=5,
                   anchor="w")

# M FRAME TO HOLD (LABEL, INPUT, MESSAGE)
# PLAINTEXT TO NUMBER
m_frame = tk.Frame(enc_dec_frame)
m_frame.pack(anchor="w",
             padx=10,
             pady=10)

label_m_text = "Enter plaintext (m) : "
label_m = tk.Label(m_frame,
                   text=label_m_text,
                   font=(FONT, 15))
label_m.pack(padx=10,
             pady=10,
             anchor="nw",
             side="top")

entry_m = tk.Entry(m_frame,
                   font=(FONT, 13))
entry_m.pack(pady=5,
             padx=10,
             anchor="nw",
             side="top")

result_label_m = tk.Label(m_frame,
                          text="",
                          font=(FONT, 12))
result_label_m.pack(anchor="w",
                    padx=10,
                    pady=10)

button_m = tk.Button(m_frame,
                     text="Translate",
                     font=(FONT, 13),
                     command=lambda: translate(entry_m.get()))

button_m.pack(anchor="w",
              padx=10,
              pady=5,
              side="left")

# SIGNATURE FRAME HOLD (LABEL, MESSAGE)
# A SIGNS THE MESSAGE
sig_frame = tk.Frame(enc_dec_frame)
sig_frame.pack(anchor="w",
               padx=10,
               pady=10)

sig_text = "Sign the Message (Signature)"
label_sig = tk.Label(sig_frame,
                     text=sig_text,
                     font=(FONT, 15))
label_sig.pack(padx=10,
               pady=10,
               anchor="nw",
               side="top")

result_label_sig = tk.Label(sig_frame,
                            text="",
                            font=(FONT, 12))
result_label_sig.pack(anchor="w",
                      padx=10,
                      pady=10)

button_sig = tk.Button(sig_frame,
                       text="Sign",
                       font=(FONT, 13),
                       command=lambda: signature(result_label_m.cget("text"),
                                                 (result_label_d.cget("text"), result_label_n.cget("text"))))
button_sig.pack(anchor="w",
                padx=10,
                pady=5,
                side="left")

# ENCRYPTION FRAME HOLD (LABEL, MESSAGE)
# A ENCRYPTS MESSAGE AND SIGNATURE FOR B
enc_frame = tk.Frame(enc_dec_frame)
enc_frame.pack(anchor="w",
               padx=10,
               pady=10)

enc_text = "Encrypt"
label_enc = tk.Label(enc_frame,
                     text=enc_text,
                     font=(FONT, 15))
label_enc.pack(padx=10,
               pady=10,
               anchor="nw",
               side="top")

result_label_enc = tk.Label(enc_frame,
                            text="",
                            font=(FONT, 12))
result_label_enc.pack(anchor="w",
                      padx=10,
                      pady=10)

button_enc = tk.Button(enc_frame,
                       text="Encrypt (Encrypted Translated Plaintext,Encrypted Signature)",
                       font=(FONT, 13),
                       command=lambda: encryption(result_label_m.cget("text"),
                                                  result_label_sig.cget("text"),
                                                  (result_label_n_b.cget("text"),
                                                   entry_e_b.get())))
button_enc.pack(anchor="w",
                padx=10,
                pady=5,
                side="left")

# DECRYPTION FRAME HOLD (LABEL, MESSAGE)
# B DECRYPTS THE MESSAGE AND SIGNATURE
dec_frame = tk.Frame(enc_dec_frame)
dec_frame.pack(anchor="w",
               padx=10,
               pady=10)

dec_text = "Decrypt"
label_dec = tk.Label(dec_frame,
                     text=dec_text,
                     font=(FONT, 15))
label_dec.pack(padx=10,
               pady=10,
               anchor="nw",
               side="top")

# DECRYPTION TO NUMBER
result_label_dec_num = tk.Label(dec_frame,
                                text="",
                                font=(FONT, 12))
result_label_dec_num.pack(anchor="w",
                          padx=10,
                          pady=10)

button_dec_num = tk.Button(dec_frame,
                           text="Decrypt to Numerical Value",
                           font=(FONT, 13),
                           command=lambda: decryption_num(result_label_enc.cget("text"),
                                                          (result_label_n_b.cget("text"),
                                                           result_label_d_b.cget("text"))))
button_dec_num.pack(anchor="w",
                    padx=10,
                    pady=5,
                    side="left")

# DECRYPTION TO ALPHABET
result_label_dec_alpha = tk.Label(dec_frame,
                                  text="",
                                  font=(FONT, 12))
result_label_dec_alpha.pack(anchor="w",
                            padx=10,
                            pady=10)

button_dec_alpha = tk.Button(dec_frame,
                             text="Decrypt to Plaintext",
                             font=(FONT, 13),
                             command=lambda: decryption_alpha(result_label_enc.cget("text"),
                                                              (result_label_n_b.cget("text"),
                                                               result_label_d_b.cget("text"))))
button_dec_alpha.pack(anchor="w",
                      padx=10,
                      pady=5,
                      side="left")

# VERIFICATION FRAME HOLD (LABEL, MESSAGE)
# B VERIFIES SIGNATURE
verif_frame = tk.Frame(enc_dec_frame)
verif_frame.pack(anchor="w",
                 padx=10,
                 pady=10)

verif_text = "Check for Authentication"
label_verif = tk.Label(verif_frame,
                       text=verif_text,
                       font=(FONT, 15))
label_verif.pack(padx=10,
                 pady=10,
                 anchor="nw",
                 side="top")

result_label_verif = tk.Label(verif_frame,
                              text="",
                              font=(FONT, 12))
result_label_verif.pack(anchor="w",
                        padx=10,
                        pady=10)

button_verif = tk.Button(verif_frame,
                         text="Check for Authentication",
                         font=(FONT, 13),
                         command=lambda: signature_verification(result_label_enc.cget("text"),
                                                                (result_label_n_b.cget("text"),
                                                                 result_label_d_b.cget("text")),
                                                                (result_label_n.cget("text"),
                                                                 entry_e.get())))
button_verif.pack(anchor="w",
                  padx=10,
                  pady=5,
                  side="left")

window.mainloop()
