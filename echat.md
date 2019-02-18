*Connect And Auth
var socket = io.connect(url, {
  query: { token: 'token' }
});

socket.on('connect', () => {
  socket.on('authorized', () => {
    console.log("authorized");
  }).on('unauthorized', () => {
    console.log("unauthorized");
  });
  socket.emit('authenticate', $('#send-from').val(), "client_" + Date.now() + "_" + Math.random().toString().substring(2));
});
