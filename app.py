from flask import Flask, render_template, request, jsonify
import requests
import PyPDF2
import os

app = Flask(__name__)
chat_history = []
uploaded_text = ""

# Chat Model using Ollama HTTP API
def chat_with_model(history):
    prompt = "\n".join([f"You: {msg['user']}\nBot: {msg['bot']}" for msg in history[:-1]])
    prompt += f"\nYou: {history[-1]['user']}\nBot:"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json().get('response', '').strip()
    except Exception as e:
        return "⚠️ Error communicating with the model: " + str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global uploaded_text
    user_msg = request.json['message']

    # Inject uploaded file if user wants to reference it
    if "upload" in user_msg.lower() or "file" in user_msg.lower():
        if uploaded_text.startswith("⚠️"):
            user_msg += f"\n\nNote: {uploaded_text}"
        else:
            user_msg += f"\n\nHere is the uploaded content:\n{uploaded_text}"

    chat_history.append({'user': user_msg, 'bot': ''})
    bot_response = chat_with_model(chat_history)
    chat_history[-1]['bot'] = bot_response
    return jsonify({'response': bot_response})

@app.route('/upload', methods=['POST'])
def upload_file():
    global uploaded_text
    uploaded_file = request.files['file']
    content = ""

    try:
        if uploaded_file.filename.endswith('.pdf'):
            reader = PyPDF2.PdfReader(uploaded_file)
            text = []
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text.strip())
            content = "\n".join(text)
        elif uploaded_file.filename.endswith('.txt'):
            content = uploaded_file.read().decode('utf-8')
        else:
            content = "⚠️ Unsupported file type. Please upload a PDF or TXT file."

        content = content.strip().replace('\n\n', '\n')[:1500]  # Sanitize and limit
        if not content or content.startswith("\u0000"):
            content = "⚠️ File content could not be read or is empty."

    except Exception as e:
        content = "⚠️ An error occurred while reading the file."

    uploaded_text = content
    return jsonify({'content': content})

if __name__ == '__main__':
    app.run(debug=True)
