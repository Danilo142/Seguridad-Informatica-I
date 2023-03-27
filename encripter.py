# Definimos una función para encriptar el mensaje
def encriptar(mensaje, clave):
    # Creamos una cadena de caracteres para almacenar el mensaje encriptado
    mensaje_encriptado = ""
    # Recorremos cada carácter del mensaje
    for caracter in mensaje:
        # Si el carácter es una letra, lo encriptamos
        if caracter.isalpha():
            # Convertimos el carácter a su código ASCII y le restamos el código ASCII de 'a'
            codigo = ord(caracter.lower()) - ord('a')
            # Aplicamos la clave de encriptación (desplazamiento) al código
            codigo_encriptado = (codigo + clave) % 26
            # Convertimos el código encriptado de vuelta a un carácter y lo añadimos al mensaje encriptado
            mensaje_encriptado += chr(codigo_encriptado + ord('a'))
        # Si el carácter no es una letra, lo dejamos igual
        else:
            mensaje_encriptado += caracter
    # Devolvemos el mensaje encriptado
    return mensaje_encriptado

# Ejemplo de uso:
mensaje = "Hola mundo!"
clave = 3
mensaje_encriptado = encriptar(mensaje, clave)
print("Mensaje original:", mensaje)
print("Mensaje encriptado:", mensaje_encriptado)
"""Este código tomará el mensaje y la clave de encriptación como entrada y devolverá el mensaje encriptado.
 En este ejemplo, la clave de encriptación es un número entero que indica cuántas posiciones se desplazará cada letra del mensaje. 
 El encriptador utiliza la técnica de sustitución de caracteres, 
 donde cada letra del alfabeto se sustituye por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto.
 En este caso, la sustitución se hace mediante un desplazamiento de la cantidad indicada por la clave."""