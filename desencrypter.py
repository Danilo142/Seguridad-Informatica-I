def desencriptar(mensaje_encriptado, clave):
    mensaje_desencriptado = ""
    for caracter in mensaje_encriptado:
        if caracter.isalpha():
            codigo_encriptado = ord(caracter.lower()) - ord('a')
            codigo_desencriptado = (codigo_encriptado - clave) % 26
            mensaje_desencriptado += chr(codigo_desencriptado + ord('a'))
        else:
            mensaje_desencriptado += caracter
    return mensaje_desencriptado

clave = 3
mensaje = "hola mundo"
mensaje_encriptado = encriptar(mensaje, clave)
print("Mensaje encriptado:", mensaje_encriptado)

mensaje_desencriptado = desencriptar(mensaje_encriptado, clave)
print("Mensaje desencriptado:", mensaje_desencriptado)