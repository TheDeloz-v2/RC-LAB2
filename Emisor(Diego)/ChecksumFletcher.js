// ChecksumFletcher.js

// Function to calculate the Fletcher checksum for a single 8-bit binary string
function fletcher16(data) {
    let sum1 = 0;
    let sum2 = 0;
    const modulus = 255;

    const bytes = data.split(' ');
    
    for (let byte of bytes) {
        let value = parseInt(byte, 2); 
        sum1 = (sum1 + value) % modulus;
        sum2 = (sum2 + sum1) % modulus;
    }
    
    const code = (sum2 << 8) | sum1;

    return code.toString(16);
}

// Function to check the checksum of a received message
function checkReceiverChecksum(receivedMessage) {
    
    let calculatedChecksum = fletcher16(receivedMessage);

    return [receivedMessage, calculatedChecksum];
}

export { checkReceiverChecksum };


