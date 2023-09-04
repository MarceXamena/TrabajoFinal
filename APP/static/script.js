document.addEventListener('DOMContentLoaded', function() {
    var chatForm = document.getElementById('chat-form');
    var messageInput = document.getElementById('message-input');
    var chatMessages = document.getElementById('chat-messages');

    chatForm.addEventListener('submit', function(event) {
        event.preventDefault();
        var message = messageInput.value;
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/api/chat', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                console.log('Message sent');
                messageInput.value = '';
                var newMessageElement = document.createElement('p');
                newMessageElement.textContent = message;
                chatMessages.appendChild(newMessageElement);
            }
        };
        xhr.send(JSON.stringify({ 'message': message }));
    });
});