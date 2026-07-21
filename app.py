from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Selamat ya! Kamu telah menyelesaikan project CI/CD menggunakan Azure... Yeayy :)'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)