const chatHistory = document.querySelector('#chat-history');

function scrollToBottom() {
  chatHistory.scrollTop = chatHistory.scrollHeight;
}

function addMessageToHistory(message, messageType) {
  const div = document.createElement('div');
  div.classList.add('chat-message', messageType);
  div.innerHTML = `<p>${message}</p>`;
  chatHistory.appendChild(div);
  scrollToBottom();
}

function sendMessage(event) {
  event.preventDefault();

  const messageInput = document.querySelector('#message');
  const message = messageInput.value.trim();

  if (message === '') {
    return;
  }

  addMessageToHistory(message, 'user-message');

  fetch('/chatbot', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      message: message
    })
  })
    .then(response => response.json())
    .then(data => {
      const botResponse = data.bot_response;
      const sentiment = data.sentiment;
      const polarity = data.polarity;

      addMessageToHistory(botResponse, 'bot-message');
      
      if (sentiment === 'positive') {
        addMessageToHistory("So! How else are you feeling today?", 'bot-message');
      } else if (sentiment === 'negative') {
        addMessageToHistory("Would you like to talk about it?", 'bot-message');
      } else {
        addMessageToHistory("Wanna be more specific? What else is on your mind?", 'bot-message');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });

  messageInput.value = '';
}

document.querySelector('.chat-message-form form').addEventListener('submit', sendMessage);