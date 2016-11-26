import { Meteor } from 'meteor/meteor';

export default function sendMTEX(message, conn){
  Meteor.setTimeout(function(){
    // Parse message
    const deviceId = message.slice(0,4);
    const msgId = message.slice(message.length-9, message.length-5);
    const ordId = message.slice(15,19);
    const parameters = '0000000E0000'
    const executionMessage = `${deviceId}.${ordId}.${parameters}.1234.MTEX`;

    // Communicate
    console.log(`Sending [MTEX] : ${executionMessage}`);
    conn.write(executionMessage);
    console.log(`MTEX sent!`);
  }, 3000)
}
