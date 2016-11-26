import sendMTEX from './_send-mtex';

const sendRESP = (message, conn) => {
  // Parse message
  const deviceId = message.slice(0,4);
  const msgId = message.slice(message.length-9, message.length-5);
  const parameters = '0000000E0000';
  const responseMessage = `${deviceId}.${msgId}.${parameters}.RESP`;

  // Communicate
  console.log(`Sending [RESP] : ${responseMessage}`);
  conn.write(responseMessage);
  console.log(`RESP sent!`);
  sendMTEX(message, conn);

};

export default sendRESP;
