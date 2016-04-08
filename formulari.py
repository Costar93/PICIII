from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
	user = request.form.get('user')
        password = request.form.get('password')
        do_the_login(user,password)
    else:
        return render_template('formulari.html') 

if __name__ == '__main__':
    app.run('0.0.0.0')
