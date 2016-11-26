import { Meteor } from 'meteor/meteor';
import net from 'net';
import sendRESP from './_send-resp';
import { Messages } from '/imports/api';

Meteor.startup(() => {

  const server = net.createServer();

  server.on('connection', Meteor.bindEnvironment(handleConnection));

  server.listen(process.env.TCP_PORT, () => {
    console.log(`TCP Server listening to ${JSON.stringify(server.address())}}`);
  });

});

function handleConnection(conn) {
  const {
    remoteAddress: rA,
    remotePort: rP,
  } = conn;
  const remoteAddress = `${rA}:${rP}`;
  console.log(`new client connection from ${remoteAddress}`);

  conn.setEncoding('utf8');

  conn.on('data', Meteor.bindEnvironment(onConnData));
  conn.once('close', Meteor.bindEnvironment(onConnClose));
  conn.on('error', Meteor.bindEnvironment(onConnError));

  function onConnData(d) {
    Messages.insert({
      message: `CLIENT -> ${remoteAddress}: ${d}`,
    });
    console.log(`CLIENT -> ${remoteAddress}: ${d}`);
    const messageType = d.slice(d.length-4);
    console.log(`Received [${messageType}] : ${d}`);
    if (messageType === 'MPTO') {
      sendRESP(d, conn);
    }
  }

  function onConnClose() {
    console.log(`CLIENT -> ${remoteAddress} closed`);
  }

  function onConnError(err) {
    console.log(`CLIENT -> ${remoteAddress} error: ${err.message}`);
  }

}
