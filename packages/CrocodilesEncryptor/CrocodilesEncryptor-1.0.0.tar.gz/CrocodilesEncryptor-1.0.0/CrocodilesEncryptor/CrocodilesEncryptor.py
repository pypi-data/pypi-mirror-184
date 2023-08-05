import random

class CrocodilesEncryptor:
    def __init__(self, password):
        self.password = password

    def encrypt_file(self, file_path, output_file_path=None):
        with open(file_path, 'r') as f:
            contents = f.read()
        encrypted_contents = self.encrypt(contents)
        if output_file_path is None:
            output_file_path = file_path + '.encrypted'
        with open(output_file_path, 'w') as f:
            f.write(encrypted_contents)
        return output_file_path

    def encrypt(self, contents):
        encrypted_contents = ''
        password_index = 0
        c_index = 1
        for c in contents:
            key = ord(self.password[password_index])
            encrypted_char = chr(ord(c) ^ key)
            if c_index % 2 == 0:
                encrypted_char += random.choice('ابتثجحخدذرزسشصضطظعغفقكلمنهوي')
                c_index = 0
            encrypted_contents += encrypted_char
            password_index = (password_index + 1) % len(self.password)
        return encrypted_contents

    def decrypt_file(self, encrypted_file_path, output_file_path: str = None):
        with open(encrypted_file_path, 'r') as f:
            encrypted_contents = f.read()
        decrypted_contents = self.decrypt(encrypted_contents)
        if output_file_path is None:
            output_file_path = encrypted_file_path[:-len('.encrypted')]
        with open(output_file_path, 'w') as f:
            f.write(decrypted_contents)
        return output_file_path

    def decrypt(self, encrypted_contents):
        decrypted_contents = ''
        password_index = 0
        c_index = 1
        for c in encrypted_contents:
            key = ord(self.password[password_index])
            decrypted_char = chr(ord(c) ^ key)
            if c_index % 2 == 0:
                decrypted_char = ""
                c_index = 0
            decrypted_contents += decrypted_char
            password_index = (password_index + 1) % len(self.password)
        return decrypted_contents
