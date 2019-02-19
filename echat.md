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
```python
socket.emit('chat message', { to: to, message: msg });
```
# Send Room Message
```python
socket.emit('room message', (data) => {
    self.io.to(data.roomid).emit('room message', data.message);
});
```
