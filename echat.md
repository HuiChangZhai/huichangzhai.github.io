# Client Connection
var socket = io.connect(url, {
  query: { token: $('#Token').val() }
});

# Recieve Message 
socket.on('chat message', function (data) {
  // { from, to, message }
  $('#messages').append($('<li>').text(data.message));
});
# Send Message
socket.emit('chat message', { to: to.split(','), message: msg });
