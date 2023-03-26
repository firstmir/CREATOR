from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world(): 
    return render_template('basic.html')

if __name__ == '__main__':
    app.run(app, host="0.0.0.0", port=5000)
    