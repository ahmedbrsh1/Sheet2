def brute_force(ciphertext):
    ciphertext = ciphertext.upper()
    unique_letters = sorted(set(ciphertext))  

    if len(unique_letters) > 3:  
        print("Too many unique letters")
        return

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                if len(unique_letters) == 1:
                    key = {unique_letters[0]: a}
                elif len(unique_letters) == 2:
                    key = {unique_letters[0]: a, unique_letters[1]: b}
                else:
                    key = {unique_letters[0]: a, unique_letters[1]: b, unique_letters[2]: c}

                decrypted_text = "".join(key.get(c, c) for c in ciphertext)
                print(f"Key: {key} | {decrypted_text}")

# Example usage
ciphertext = "ABC"
brute_force(ciphertext)
