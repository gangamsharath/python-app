#import flask
from flask import Flask

app=Flask(__name__)

@app.route('/')
def homepage():
    return "<h1 style='background-colour:orange'>Hello, World! Your Super</h1>"

@app.route('/about')
def aboutpage():
    return "<h2 style='background-colour:yellow'>Techmojo</h2>"

if __name__ == '__main__':
    app.run(debug=True,port=3000)