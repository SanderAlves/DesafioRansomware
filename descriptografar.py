import os
import pyaes

## abrir o arquivo criptografado

file_name = "desafioDIO.txt.ransomwareDesafio"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografar

key = b"testeransonwares"
aes = pyeas.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado

os.remove(file_name)

## criar o arquivo descriptografado

new_file = "desafioDIO.txt"
new_file = open(f'{new_file}',"wb")
new_file.write(decrypt_data)
new_file.close()
