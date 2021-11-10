from simplecrypt import encrypt, decrypt

password = "1234"
message = "secret message"

encrypted = encrypt(password, message)
print(encrypted)
with open("files/file.secret", "wb") as secret_file:
    secret_file.write(encrypted)
decrypted = decrypt(password, encrypted).decode("utf-8")
print(decrypted)
