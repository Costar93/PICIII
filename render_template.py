from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
def hello(name=None):
    name = "Jordi"
    surname = "Costa"
    return render_template('simple_template.html', 
                           user_name=name, 
                           user_surname=surname)

@app.route('/hello2/')
def hello2(name=None):
    name = None
    surname = None
    return render_template('conditional_template.html', 
                           user_name=name, 
                           user_surname=surname)

@app.route('/hello3/')
def hello3(name=None):
    user_list=["Costa", "Darth", "Luke", "Leia", "Han"]
    return render_template('loop_template.html', 
                           users=user_list)

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
