<script type="text/javascript">
var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('notification', function(data) {
    
    alert(data.message)
});

// Event listener for the "Send Notification" button
document.getElementById('send_notification').addEventListener('click', function() {
    varmessage = prompt('Enter a notification message:')};
    if (message) {
        socket.emit('notification', { message: message })
    }
);

</script>