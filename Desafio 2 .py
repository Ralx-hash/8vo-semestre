#DESAFIO 2
import json

import requests

headers = {
    'Content-Type': 'text/plain',
}

response = requests.get('http://finis.malba.cl/GetMsg', headers=headers)



def rot_n(text, n):
    result = ""
    for char in text:
        if char.isalpha(): 
            if char.islower(): 
                result += chr(((ord(char) - ord('a') + n) % 26) + ord('a')) 
            else:
                result += chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
        else:
            result += char
    return result

#decifrado vigenere

def vigenere_decrypt(textocif, key):
    key_length = len(key)
    decrypted_text = ""
    for i, char in enumerate(textocif):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            if char.islower():
                decrypted_text += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))

            else:
                decrypted_text += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text


msg_import = json.loads(response.text)

texto_decifrar = msg_import['msg']

clave_vigenere = 'aobkqolrzsrigpknkufezioer'


#decifrar root(-7)
mensaje_final = rot_n(texto_decifrar, -7)
print("mensaje root: ",mensaje_final)

#Decifrar vigenere
mensaje_final = vigenere_decrypt(mensaje_final,clave_vigenere)
print("mensaje vigenere:", mensaje_final)

#Decifrar root(-15)
mensaje_final = rot_n(mensaje_final, -15)

print("texto desencriptado: ", mensaje_final)
