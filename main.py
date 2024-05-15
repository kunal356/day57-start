from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    random_num = random.randint(1, 10)
    return render_template('index.html', num=random_num, curr_year = dt.datetime.now().year)

@app.route('/guess/<name>')
def guess(name):
    random_num = random.randint(1, 10)
    parameter = {
        "name": name
    }
    resp_1 = requests.get('https://api.genderize.io',params=parameter)
    resp_2 = requests.get('https://api.agify.io',params=parameter)
    
    return render_template('guess.html', num=random_num, curr_year = dt.datetime.now().year, age=resp_2.json(), gender=resp_1.json())

@app.route('/blogs')
def get_blogs():
    resp = requests.get('https://api.npoint.io/19c4467e9b0030cad0fd')
    data = resp.json()
    return render_template('blog.html', all_posts=data)
if __name__ == "__main__":
    app.run(debug=True)