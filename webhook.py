from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_data(as_text=True)
    with open("signals.txt", "w") as f:
        f.write(data)
    return 'Signal received', 200

@app.route('/', methods=['GET'])
def home():
    return "STT Webhook Server Running", 200
