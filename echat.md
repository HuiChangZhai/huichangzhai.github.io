# Client Connection
```javascript
var socket = io.connect(url, {
  query: { token: $('#Token').val() }
});
```

# Recieve Message 
```javascript
socket.on('chat message', function (data) {
  // { from, to, message }
  $('#messages').append($('<li>').text(data.message));
});
```
# Send Message
```javascript
socket.emit('chat message', { to: to.split(','), message: msg });
```
