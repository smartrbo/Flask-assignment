$(document).ready(function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('message', function (data) {
        $('#messages').append('<li>' + data + '</li>');
    });

    $('#send_button').on('click', function () {
        var message = $('#message_input').val();
        if (message) {
            socket.emit('message', message);
            $('#message_input').val('').focus();
        }
    });

    $('#message_input').keypress(function (e) {
        if (e.which == 13) {
            $('#send_button').click();
        }
    });
});