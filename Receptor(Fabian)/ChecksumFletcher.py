def fletcher16(data):
    sum1 = 0
    sum2 = 0
    for bit in data:
        sum1 = (sum1 + int(bit)) % 255
        sum2 = (sum2 + sum1) % 255
    return (sum2 << 8) | sum1

def calculate_parity_bit(checksum):
    # El bit de paridad se calcula como la suma de los bits del checksum módulo 2
    binary = bin(checksum)
    return binary.count('1') % 2

def checkReceiverChecksum():
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