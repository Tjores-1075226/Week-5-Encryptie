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