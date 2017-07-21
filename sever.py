from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    pass

@app.route('/cost')
def cost():
    pass

@app.route('/tip/{cost}')
def calculated_tip():
    pass

@app.route('/tip/now')
def tip_now():
    pass

@app.route('/login', methods= ['GET', 'POST'])
def login():
    pass


if __name__ == "__main__":
    app.debug = true
    app.run(host="0.0.0.0", port=5001)