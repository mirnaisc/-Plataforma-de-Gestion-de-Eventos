from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def serve():
    return send_file('../frontend/index.html')

if __name__ == '__main__':
    app.run(debug=True)
