# Connect And Auth
```python
var socket = io.connect(url, {
  query: { token: 'token' }
});

socket.on('connect', () => {
  socket.on('authorized', () => {
    console.log("authorized");
  }).on('unauthorized', () => {
    console.log("unauthorized");
  });
  socket.emit('authenticate', authid, clientid);
});
```
# Disconnect
```python
socket.on('disconnect', (reason) => {
  console.log(`Disconnected. Reason: ${reason}`);
});
```

# Send Message
socket.emit('chat message', { to: to, message: msg });
