import os
import pyaes

file_name = 'teste.txt.ransomwaretroll'
file_open = open(file_name, 'rb')
file_data = file_open.read()
file_open.close()

#chave de descriptografia
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

#remover arquivo criptografado
os.remove(file_name)

#criar novo arquivo descriptografado

new_file = 'teste.txt'
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()