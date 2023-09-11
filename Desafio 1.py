import requests

def rot_n(text, n):
    result = ""
    for char in text:
        if char.isalpha(): #isalpha es si la posicion char es una letra
            if char.islower(): #islower es para saber si es minuscula
                result += chr(((ord(char) - ord('a') + n) % 26) + ord('a')) #aqui pasan muchas cosas
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

def vigenere_crypt(textcif, key):
    key_length = len(key)
    decrypted_text = ""
    for i, char in enumerate(textcif):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            if char.islower():
                decrypted_text += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                decrypted_text += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text    

# Mensaje cifrado
mensaje_cifrado = "mensaje random"
# Aplicar Rot(15)
mensaje_rot = rot_n(mensaje_cifrado, 15)
# Clave Vigenère
clave_vigenere = "cvqnoteshrwnszhhksorbqcoas"
# Descifrar Vigenère
mensaje_descifrado = vigenere_crypt(mensaje_rot, clave_vigenere)
# Aplicar Rot(7)
mensaje_final = rot_n(mensaje_descifrado, 7)

# print("mensaje vigenere: ", mensaje_descifrado)
print("mensaje final: ", mensaje_final)

# print("Mensaje root 15:", mensaje_rot)


headers = {
    'Content-Type': 'text/plain',
}

data = '{"msg":"kvzbkye unfmch"}'

response = requests.post('http://finis.malba.cl/SendMsg', headers=headers, data=data)

print(response.text)


#PROCESO DE DECRIFRADO

# Aplicar Root(-7)
mensaje_final = rot_n(mensaje_final, -7)

# Aplicar Vigenere
mensaje_final = vigenere_decrypt(mensaje_final, clave_vigenere)

# Aplicar Root(-15)
mensaje_final = rot_n(mensaje_final, -15)

print("mensaje desencriptado: ",mensaje_final)


