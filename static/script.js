const video = document.getElementById('video');

// Получаем доступ к веб-камере
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error('Ошибка доступа к веб-камере:', err);
    });

// Чат
const messages = document.getElementById('messages');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');

// Простейшая реализация чата
sendButton.addEventListener('click', () => {
    const messageText = messageInput.value;
    if (messageText) {
        const messageElement = document.createElement('div');
        messageElement.textContent = messageText;
        messages.appendChild(messageElement);
        messageInput.value = '';
        messages.scrollTop = messages.scrollHeight; // Прокрутка вниз
    }
});