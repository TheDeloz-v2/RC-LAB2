// Main.js

import { encodeMessage } from './Hamming.js';
import { checkReceiverChecksum } from './ChecksumFletcher.js';
import fs from 'fs';

async function main() {
    try {
        let encodedMessages = [];

        fs.readFile('Mensajes/codificar.txt', 'utf8', (err, data) => {
            if (err) {
              console.error(err);
              return;
            }
            
            data = data.replace(/\r/g, '');

            let lines = data.split('\n');

            for (let line of lines) {
                console.log('\nMensaje original:', line);

                // Encode the message
                const encodedMessage = encodeMessage(line);

                // Display the encoded message
                console.log('Encoded message:', encodedMessage);

                // Store the encoded message
                encodedMessages.push(encodedMessage);

                // Calculate the Fletcher checksum
                const checksum = checkReceiverChecksum(line);

                // Display the Fletcher checksum
                console.log('Fletcher checksum:', checksum);

                // Store the checksum
                encodedMessages.push(checksum);
            }
          });
    }
    catch (error) {
        console.error('Error:', error.message);
    }

}

main();