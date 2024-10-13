from cryptography.fernet import Fernet

# genereren van sleutel
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Sleutel gemaakt en opgeslagen in 'secret.key'.")

# sleutel laden
def load_key():
    return open("secret.key", "rb").read()

#tekst versleutelen
def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message


# tekst ontsleutelen
def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message


