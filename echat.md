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
# Join Room
```python
socket.emit('join room', {roomid:roomid});
```

# Send Room Message
```python
socket.emit('room message', {roomid,message});
```
