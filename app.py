from flask import Flask

app=Flask(__name__)
@app.route('/')

def home():
    return '<h1>hello team</h1>'
@app.route('/new')
def new():
    return '<h1>i am new</h1>'

app.run()