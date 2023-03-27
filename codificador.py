def cifrar(cadena, numeros):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    cifrado = ''
    # Recorremos cada carácter de la cadena
    for letra in cadena:
        # Si el carácter es una letra, lo ciframos
        if letra.lower() in alfabeto:
            indice = (alfabeto.index(letra.lower()) + numeros[0]) % 26
            # Convertimos el código cifrado de vuelta a un carácter y lo añadimos al mensaje cifrado
            cifrado += alfabeto[indice]
            # Desplazamos la lista de números
            numeros.append(numeros.pop(0))
        else:
            cifrado += letra
    return cifrado

cadena = input('Introduce la cadena de texto que deseas cifrar: ')
numeros = input('Introduce la lista de números separados por comas: ')
numeros = [int(n) for n in numeros.split(',')]
texto_cifrado = cifrar(cadena, numeros)
print('El texto cifrado es:', texto_cifrado)
