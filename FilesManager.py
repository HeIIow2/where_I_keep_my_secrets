from simplecrypt import encrypt, decrypt


class File:
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password

        open(self.get_path(), "a")

        with open(self.get_path(), "rb") as raw_file:
            self.encrypted_content = raw_file.read()
            if self.encrypted_content == b"":
                self.decrypted_content = ""
            else:
                print("decrypting may take a couple seconds")
                self.decrypted_content = decrypt(self.password, self.encrypted_content).decode("utf-8")
                print("")
                print(self.decrypted_content)

    def get_path(self):
        return f'files/{self.name}.secret'

    def encrypt_and_safe(self):
        self.encrypted_content = encrypt(self.password, self.decrypted_content)
        with open(self.get_path(), "wb") as encrypted_file:
            encrypted_file.write(self.encrypted_content)
        print("changes are saved")

    def write_to_file(self):
        print('every line you type, will get addet to the file, until you type "END"')
        to_add = input("--> ")
        while to_add != "END":
            self.decrypted_content += to_add + "\n"
            to_add = input("--> ")

        print("saving the changes")
        print("this will may take some seconds")
        self.encrypt_and_safe()
