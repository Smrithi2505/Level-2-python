import random
import string

# Caesar Cipher Function
def caesar_cipher(text, key):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))

        elif char.isdigit():
            result += str((int(char) + key) % 10)

        else:
            result += char

    return result


# Reverse Cipher Function
def reverse_cipher(text):
    return text[::-1]


# Generate 5-Letter Secret Code (No Repeated Letters)
def generate_secret_code():
    letters = random.sample(string.ascii_uppercase, 5)
    return "".join(letters)


# Possible Enemy Preambles
preambles = ["python", "coding", "secret", "hacker", "agent"]

# Random Preamble and Secret Code
preamble = random.choice(preambles)
secret_code = generate_secret_code()

# Random Encoder Choice
encoder = random.choice(["caesar", "reverse"])

if encoder == "caesar":

    # Random Caesar Key
    preamble_key = random.randint(1, 5)
    secret_key = preamble_key + 2

    encoded_preamble = caesar_cipher(preamble, preamble_key)
    encoded_secret = caesar_cipher(secret_code, secret_key)

else:

    encoded_preamble = reverse_cipher(preamble)
    encoded_secret = reverse_cipher(secret_code)

# Enemy Message
enemy_message = encoded_preamble + " " + encoded_secret

print("================================")
print("ENEMY MESSAGE")
print(enemy_message)
print("================================")


# -------------------------
# CODE CRACKING SECTION
# -------------------------

possible_preambles = ["python", "coding", "secret", "hacker", "agent"]

cracked = False

# Try Caesar Cipher First
for shift in range(1, 6):

    decoded_preamble = caesar_cipher(encoded_preamble, -shift)

    if decoded_preamble in possible_preambles:

        print("\nPreamble Found:", decoded_preamble)

        decoded_secret = caesar_cipher(
            encoded_secret,
            -(shift + 2)
        )

        print("Secret Code:", decoded_secret)

        cracked = True
        break


# If Caesar Fails, Try Reverse Cipher
if not cracked:

    decoded_preamble = reverse_cipher(encoded_preamble)

    if decoded_preamble in possible_preambles:

        print("\nPreamble Found:", decoded_preamble)

        decoded_secret = reverse_cipher(encoded_secret)

        print("Secret Code:", decoded_secret)

        cracked = True


if not cracked:
    print("Code could not be cracked.")