var net = require('net');

var server = net.createServer();
server.on('connection', handleConnection);

server.listen(9000, function() {
  console.log('TCP Server listening to %j', server.address());
});

function handleConnection(conn) {
  var remoteAddress = conn.remoteAddress + ':' + conn.remotePort;
  console.log('new client connection from %s', remoteAddress);

  conn.setEncoding('utf8');

  conn.on('data', onConnData);
  conn.once('close', onConnClose);
  conn.on('error', onConnError);

  function onConnData(d) {
    console.log('CLIENT -> %s: %j', remoteAddress, d);
    var messagetype = d.slice(d.length-4);
    console.log('Received [' + messagetype + '] : ' + d);
    if (messagetype == 'MPTO') {
      sendRESP(d, conn);
    }
  }

  function onConnClose() {
    console.log('CLIENT -> %s closed', remoteAddress);
  }

  function onConnError(err) {
    console.log('CLIENT -> %s error: %s', remoteAddress, err.message);
  }
}

function randomInt (low, high) {
    return Math.floor(Math.random() * (high - low) + low);
}

function sendRESP(message, conn){
  // Parse message
  var deviceid = message.slice(0,4);
  var msgid = message.slice(message.length-9, message.length-5);
  var parameters = '0000000E0000'
  var responseMessage = deviceid + '.' + msgid + '.' + parameters + '.RESP';
  // Communicate
  console.log('Sending [RESP] : ' + responseMessage);
  conn.write(responseMessage);
  console.log('RESP sent ! ');
  sendMTEX(message, conn);
}

function sendMTEX(message, conn){
  setTimeout(function(){
    // Parse message
    var deviceid = message.slice(0,4);
    var msgid = message.slice(message.length-9, message.length-5);
    var ordid = message.slice(15,19);
    var parameters = '0000000E0000'
    var executionMessage = deviceid + '.' + ordid + '.' + parameters + '.1234' + '.MTEX';
    // Communicate
    console.log('Sending [MTEX] : ' + executionMessage);
    conn.write(executionMessage);
    console.log('MTEX sent ! ');
  }, 3000)
}
