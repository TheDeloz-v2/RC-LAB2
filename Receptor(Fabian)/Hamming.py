def hamming_decode(received_message):
    """
    Decodifica un mensaje utilizando el código de Hamming y verifica la integridad del mensaje.
    
    Parámetros:
    received_message (str): Un mensaje binario concatenado con la información generada por el emisor.
    
    Retorna:
    tuple: Una tupla que contiene:
           - El mensaje original sin la información generada por el emisor si no se detectaron errores.
           - Un estado indicando si no se detectaron errores, si el mensaje se descarta por errores,
             o si se corrigieron errores, junto con la posición de los bits corregidos y el mensaje corregido.
    """
    def calculate_parity_positions(data_length):
        # Calcula las posiciones de los bits de paridad en el mensaje de longitud data_length
        parity_positions = []
        i = 0
        while (2**i) <= data_length:
            parity_positions.append(2**i)
            i += 1
        return parity_positions

    def calculate_parity_bits(data, parity_positions):
        # Calcula los bits de paridad para los datos dados
        parity_bits = []
        for parity_pos in parity_positions:
            count = 0
            for i in range(1, len(data) + 1):
                if i & parity_pos != 0:
                    count += int(data[i - 1])
            parity_bits.append(count % 2)
        return parity_bits

    def find_error_position(parity_bits):
        # Encuentra la posición del error en el mensaje usando los bits de paridad calculados
        error_position = 0
        for i in range(len(parity_bits)):
            if parity_bits[i] == 1:
                error_position += 2**i
        return error_position

    # Paso 1: Solicitar mensaje en binario concatenado con la información generada por el emisor
    data = received_message
    
    # Calcular las posiciones de los bits de paridad
    parity_positions = calculate_parity_positions(len(data))
    
    # Calcular los bits de paridad en el mensaje recibido
    received_parity_bits = calculate_parity_bits(data, parity_positions)
    
    # Encontrar la posición del error si existe
    error_position = find_error_position(received_parity_bits)

    if error_position == 0:
        # No se detectaron errores
        original_message = ''.join([data[i-1] for i in range(1, len(data) + 1) if i not in parity_positions])
        return original_message, 'No se detectaron errores'
    else:
        # Se detectaron errores, corregir el bit en la posición del error
        error_position -= 1  # Ajustar la posición del error para el índice de la lista
        corrected_data = list(data)
        corrected_data[error_position] = '0' if data[error_position] == '1' else '1'
        corrected_message = ''.join(corrected_data)
        
        # Verificar nuevamente los bits de paridad para asegurarse de que la corrección fue exitosa
        corrected_parity_bits = calculate_parity_bits(corrected_message, parity_positions)
        if sum(corrected_parity_bits) == 0:
            # Se corrigieron errores
            original_message = ''.join([corrected_message[i-1] for i in range(1, len(corrected_message) + 1) if i not in parity_positions])
            return original_message, f'Se detectaron y corrigieron errores en la posición {error_position + 1}', corrected_message
        else:
            # No se pudieron corregir todos los errores
            return None, 'Se detectaron errores: el mensaje se descarta'

def main():
    # Solicitar el mensaje con la información generada por el emisor
    received_message = input("Ingrese el mensaje binario concatenado con la información generada por el emisor: ")
    
    # Ejecutar el algoritmo de Hamming para comprobar la integridad del mensaje
    result = hamming_decode(received_message)
    
    if result[1] == 'No se detectaron errores':
        print(f"Mensaje original: {result[0]}")
    elif result[1] == 'Se detectaron errores: el mensaje se descarta':
        print(result[1])
    else:
        print(f"{result[1]}")
        print(f"Mensaje corregido: {result[2]}")

if __name__ == "__main__":
    main()
