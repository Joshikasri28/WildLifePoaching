from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Wildlife Poaching Detection System is Running!"

if __name__ == '__main__':
    app.run(debug=True)
   