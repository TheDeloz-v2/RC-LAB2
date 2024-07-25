// Hamming.js

// Function to calculate the parity bit for a given position
function calculateParityBit(data, parityPosition) {
    let parityBit = 0;
    for (let i = 0; i < data.length; i++) {
        if ((i + 1) & parityPosition) {
            parityBit ^= data[i];
        }
    }
    return parityBit;
}

// Function to encode a message using Hamming code
function encodeMessage(data) {
    const n = data.length;
    const m = Math.ceil(Math.log2(n + 1));
    const encodedMessage = new Array(n + m);

    // Copy the message to the
    for (let i = 0; i < n; i++) {
        encodedMessage[i] = data[i];
    }

    // Calculate the parity bits
    for (let i = 0; i < m; i++) {
        const parityPosition = 1 << i;
        encodedMessage[n + i] = calculateParityBit(data, parityPosition);
    }

    return encodedMessage;
} 

// Function to decode a message encoded using Hamming code
function decodeMessage(encodedMessage) {
    const n = encodedMessage.length;
    const m = Math.ceil(Math.log2(n + 1));
    const data = new Array(n - m);

    // Copy the data bits
    for (let i = 0; i < n - m; i++) {
        data[i] = encodedMessage[i];
    }

    // Calculate the parity bits
    for (let i = 0; i < m; i++) {
        const parityPosition = 1 << i;
        const parityBit = calculateParityBit(data, parityPosition);
        if (encodedMessage[n - m + i] !== parityBit) {
            throw new Error('Error decoding the message');
        }
    }

    return data;
}

export { encodeMessage };
 
