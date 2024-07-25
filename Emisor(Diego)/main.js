// Main.js

import { encodeMessage } from './Hamming.js';
import { checkReceiverChecksum } from './ChecksumFletcher.js';

async function main() {
    try {
        const data = [1, 0, 1, 1, 0, 0, 1, 0];

        // Encode the message
        const encodedMessage = encodeMessage(data);

        // Display the encoded message
        console.log('Encoded message:', encodedMessage);

        // Calculate the Fletcher checksum
        const checksum = checkReceiverChecksum(data);

        // Display the Fletcher checksum
        console.log('Fletcher checksum:', checksum);
    }
    catch (error) {
        console.error('Error:', error.message);
    }

}

main();