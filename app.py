from flask import Flask 

app = Flask("meu app")

@app.route('/')
def hello():
    return "Hello, world!"

@app.route('/testando')
def htmlTxT():
    return "<h1>Testando</h1>"