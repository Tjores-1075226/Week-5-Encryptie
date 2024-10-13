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

# Programma
if __name__ == "__main__":
    keuze = input("Wil je een nieuwe sleutel maken (g) of een bericht versleutelen/ontsleutelen (v/o)? ").lower()

    if keuze == "g":
        generate_key()
    elif keuze == "v":
        bericht = input("Voer het bericht in dat je wilt versleutelen: ")
        versleuteld = encrypt_message(bericht)
        print(f"Versleuteld bericht: {versleuteld}")
    elif keuze == "o":
        encrypted_message = input("Voer de versleutelde tekst in: ")
        ontsleuteld = decrypt_message(encrypted_message.encode())
        print(f"Ontsleuteld bericht: {ontsleuteld}")
    else:
        print("Ongeldige keuze.")


