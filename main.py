from flask import Flask, render_template
import random
import datetime as dt

app = Flask(__name__)

@app.route('/')
def hello_world():
    random_num = random.randint(1, 10)
    return render_template('index.html', num=random_num, curr_year = dt.datetime.now().year)

if __name__ == "__main__":
    app.run(debug=True)