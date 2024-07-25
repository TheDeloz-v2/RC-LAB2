// ChecksumFletcher.js

// Function to calculate the Fletcher checksum for a given message
function fletcher16(data) {
    let sum1 = 0;
    let sum2 = 0;
    for (let bit of data) {
        sum1 = (sum1 + parseInt(bit, 2)) % 255;
        sum2 = (sum2 + sum1) % 255;
    }
    return (sum2 << 8) | sum1;
}

// Function to calculate the parity bit for a given checksum
function calculateParityBit(checksum) {
    let binary = checksum.toString(2);
    let parity = 0;
    for (let bit of binary) {
        parity ^= parseInt(bit);
    }
    return parity;
}

// Function to check the checksum of a received message
function checkReceiverChecksum(receivedMessage) {
    if (receivedMessage.length < 2) {
        return [null, 'Mensaje recibido demasiado corto para contener datos y bit de paridad'];
    }
    
    let data = receivedMessage.slice(0, -1);
    let receivedParityBit = parseInt(receivedMessage.slice(-1), 2);

    let calculatedChecksum = fletcher16(data);
    let calculatedParityBit = calculateParityBit(calculatedChecksum);

    if (receivedParityBit === calculatedParityBit) {
        return [data, 'No se detectaron errores'];
    } else {
        return [null, 'Se detectaron errores: el mensaje se descarta'];
    }
}

export { checkReceiverChecksum };

