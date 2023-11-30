// Import the readline module
const readline = require('readline');

// Create readline interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Ask a question and wait for user input
rl.question('Digite seu nome: ', (nome) => {
  // Handle the user input
  console.log(`Olá, ${nome}.`);

  // Close the readline interface
  rl.close();
});
