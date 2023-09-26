from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__, template_folder='templates')


@app.route('/home')
def index():
    return render_template('index.html', timestamp={'hora': datetime.now()})


@app.route('/onoff')
def onoff():
    return render_template('onoff.html', timestamp={'hora': datetime.now()})


if __name__ == '__main__':
    app.run(debug=True)
