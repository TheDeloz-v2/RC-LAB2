def fletcher16(data):
    """
    Calcula el checksum Fletcher-16 para los datos proporcionados.
    
    El checksum Fletcher-16 es un algoritmo de verificación que suma los valores de los bits de entrada
    de forma acumulativa y modular, para detectar errores en la transmisión de datos.
    
    Parámetros:
    data (str): Una cadena de bits binarios.
    
    Retorna:
    int: El checksum Fletcher-16 de los datos como un valor entero de 16 bits.
    """
    sum1 = 0
    sum2 = 0
    for bit in data:
        sum1 = (sum1 + int(bit)) % 255
        sum2 = (sum2 + sum1) % 255
    return (sum2 << 8) | sum1

def calculate_parity_bit(checksum):
    """
    Calcula el bit de paridad para un checksum dado.
    
    El bit de paridad se utiliza para detectar errores en los datos mediante la suma de los bits
    del checksum y verificando si el número de bits '1' es par o impar.
    
    Parámetros:
    checksum (int): Un valor entero que representa el checksum de los datos.
    
    Retorna:
    int: El bit de paridad calculado (0 o 1).
    """
    # El bit de paridad se calcula como la suma de los bits del checksum módulo 2
    binary = bin(checksum)
    return binary.count('1') % 2

def checkReceiverChecksum():
    """
    Verifica la integridad de un mensaje binario utilizando checksum y bit de paridad.
    
    Esta función solicita al usuario un mensaje binario que incluye datos y un bit de paridad.
    Luego, calcula el checksum de los datos y su bit de paridad, y lo compara con el bit de paridad
    recibido para determinar si hay errores en el mensaje.
    
    Retorna:
    tuple: Una tupla que contiene los datos del mensaje y un estado indicando si se detectaron errores.
           Si no se detectaron errores, retorna (data, 'No se detectaron errores').
           Si se detectaron errores, retorna (None, 'Se detectaron errores: el mensaje se descarta').
    """
    # Solicitar mensaje con checksum
    ReceivedMessage = input("Ingrese el mensaje binario concatenado con la información generada por el emisor: ")
    
    data = ReceivedMessage[:-1] #Se obtienen los primeros n bits para el mensaje
    received_parity_bit = int(ReceivedMessage[-1:]) # Se obtiene el ultimo bit que es el de la paridad.

    #Calculamos el checksum para los primeros 4 bits
    calculated_checksum = fletcher16(data)

    #Cclculamos el bit de paridad del checksum calculado
    calculated_parity_bit = calculate_parity_bit(calculated_checksum)


    if received_parity_bit == calculated_parity_bit:
        return data, 'No se detectaron errores'
    else:
        return None, 'Se detectaron errores: el mensaje se descarta'

'''
def main():

    # Verificar la integridad del mensaje
    corrected_message, status = checkReceiverChecksum(ReceivedMessage)
    
    if corrected_message:
        print(f"Mensaje original: {corrected_message}")
    else:
        print(status)

'''