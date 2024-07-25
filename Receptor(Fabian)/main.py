from Hamming import hamming_decode
from ChecksumFletcher import checkReceiverChecksum

def main():
    # Ejecutar el algoritmo de Hamming para comprobar la integridad del mensaje
    received_message = input("Ingrese el mensaje binario concatenado con la información generada por el emisor: ")
    result = hamming_decode(received_message)
    
    if result[1] == 'No se detectaron errores':
        print(f"Mensaje original: {result[0]}")
    elif result[1] == 'Se detectaron errores: el mensaje se descarta':
        print(result[1])
    else:
        print(f"{result[1]}")
        print(f"Mensaje corregido: {result[2]}")
        result2 = hamming_decode(result[2])
        print(f"Mensaje original: {result2[0]}")
    
    # Ejcuta el algoritmo de Fletcher 16 para comprobar la integridad del codigo
    corrected_message, status = checkReceiverChecksum()
    
    if corrected_message:
        print(status)
    else:
        print(status)
if __name__ == "__main__":
    main()