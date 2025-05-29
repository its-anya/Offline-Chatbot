# Offline-Chatbot

A fully offline, intelligent chatbot built using Flask, Ollama (LLaMA3), and HTML/CSS/JS. This chatbot mimics ChatGPT-like behavior with the added ability to:

💬 Chat interactively (no API required)

📁 Understand and respond to uploaded files (PDF, TXT, DOCX)

🎙️ Take voice input through your browser

🧑‍🎨 Provide an attractive, modern UI

🧠 Run completely offline using a locally hosted LLM (via Ollama)

🚀 Features

🧠 Offline Chat	Uses a local LLM (llama3) running with Ollama to respond to queries.

📁 File Upload	Upload .pdf, .txt, or .docx files and the bot reads the content.

🎙️ Voice Input	Uses Web Speech API to take voice input via browser microphone.

💻 Clean UI	Intuitive chat interface with proper formatting and scrollable history.

🔐 Privacy	All processing is done locally. No internet or external APIs are required.

📁 File Upload Supported Formats

.pdf

.txt

.docx

❌ Unsupported formats will result in an appropriate error message.

🗣️ Voice Input

Click the 🎙️ Voice button to start speaking.

Your browser will convert speech to text and send it to the bot.

Ensure microphone permissions are enabled in the browser.

📌 Dependencies

Flask

flask-cors

requests

PyPDF2

python-docx

Ollama (LLaMA3 model)

Browser support for Web Speech API

🙋‍♂️ Author

Kodali Shanmukh Chowdary

📧 kodalishanmukh6thfinger@gmail.com

🧠 B.Tech AI & ML

🌐 India
