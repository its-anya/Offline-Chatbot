// Voice input functionality using the Web Speech API
const startVoiceInput = () => {
  if (!('webkitSpeechRecognition' in window)) {
    alert('Speech recognition is not supported in this browser.');
    return;
  }

  const recognition = new webkitSpeechRecognition();
  recognition.lang = 'en-US';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    document.getElementById('input').value = transcript;
    send();
  };

  recognition.onerror = (err) => {
    alert('Speech recognition error: ' + err.error);
  };

  recognition.start();
};

// Speech output using SpeechSynthesis API
const speak = (text) => {
  const speechSynthesis = window.speechSynthesis;
  const utterance = new SpeechSynthesisUtterance(text);
  speechSynthesis.speak(utterance);
};

// Send text message to backend
const send = () => {
  const input = document.getElementById('input');
  const message = input.value;
  if (!message) return;
  appendMessage('user', message);
  input.value = '';
  fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  })
  .then((res) => res.json())
  .then((data) => {
    appendMessage('bot', data.response);
    speak(data.response);
  });
};

// Display user or bot messages in chat
const appendMessage = (sender, text) => {
  const messagesDiv = document.getElementById('messages');
  const msg = document.createElement('div');
  msg.className = 'msg';
  msg.innerHTML = `<span class="${sender}">${sender === 'user' ? 'You' : 'Bot'}:</span> ${text}`;
  messagesDiv.appendChild(msg);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
};

// File upload handler
const uploadFile = () => {
  const file = document.getElementById('fileInput').files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append('file', file);

  fetch('/upload', {
    method: 'POST',
    body: formData
  })
  .then(res => res.json())
  .then(data => {
    appendMessage('bot', '📁 File uploaded: ' + file.name);
    if (data.content.startsWith('⚠️')) {
      appendMessage('bot', data.content);
    }
  });
};
