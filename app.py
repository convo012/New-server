from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your actual Page Access Token (keep it secret!)
PAGE_ACCESS_TOKEN = "YOUR_PAGE_ACCESS_TOKEN"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    recipient_id = request.form.get('psid')
    message_text = request.form.get('message')

    if not recipient_id or not message_text:
        return jsonify({'status': 'error', 'message': 'Recipient ID and message are required'}), 400

    url = f'https://graph.facebook.com/v19.0/me/messages?access_token={PAGE_ACCESS_TOKEN}'
    payload = {
        'recipient': {'id': recipient_id},
        'message': {'text': message_text}
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return jsonify({'status': 'success', 'message': 'Message sent successfully!'})
    else:
        return jsonify({'status': 'error', 'message': response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)