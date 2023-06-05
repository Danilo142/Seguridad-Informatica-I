import string

def vigenere_cipher(message, key, mode):
    alphabet = string.ascii_lowercase  # Alfabeto en minúsculas
    key = key.lower()
    key_length = len(key)
    message = message.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios en blanco

    # Construir la clave extendida
    extended_key = ""
    i = 0
    for char in message:
        if char in alphabet:
            extended_key += key[i % key_length]
            i += 1
        else:
            extended_key += char

    result = ""
    for i in range(len(message)):
        if message[i] in alphabet:
            if mode == "encrypt":
                # Cifrar el carácter
                char_index = (alphabet.index(message[i]) + alphabet.index(extended_key[i])) % 26
            elif mode == "decrypt":
                # Descifrar el carácter
                char_index = (alphabet.index(message[i]) - alphabet.index(extended_key[i])) % 26
            result += alphabet[char_index]
        else:
            result += message[i]

    return result


# Ejemplo 
clave = "Capi"
mensaje = "Capi El mas Capi"

# Cifrar el mensaje
mensaje_cifrado = vigenere_cipher(mensaje, clave, "encrypt")
print("Mensaje cifrado:", mensaje_cifrado)

# Descifrar el mensaje cifrado
mensaje_descifrado = vigenere_cipher(mensaje_cifrado, clave, "decrypt")
print("Mensaje descifrado:", mensaje_descifrado)
