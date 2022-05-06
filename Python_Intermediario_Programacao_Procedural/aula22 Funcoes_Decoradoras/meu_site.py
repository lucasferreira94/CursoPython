from flask import Flask

app = Flask(__name__)

@app.route('/home')
def homepage():
    return 'Essa é minah Homepage'

@app.route('/contatos')
def contatos():
    return 'Esses são meus contatos'

app.run()