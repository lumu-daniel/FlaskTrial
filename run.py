from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '12167714fb24d0ef7ad0ae67fbf13b4d'

posts = [
	{'title':'First Post',
	'author':'Daniel Lumu',
	'date_posted':'1st-January-2019',
	'post_content':'We all win sometime'},
	{'title':'Second Post',
	'author':'Ninsiima Java',
	'date_posted':'3st-Febuaru-2019',
	'post_content':'phweeeeeeeeew'},
	{'title':'Third Post',
	'author':'Kiyinji Simon',
	'date_posted':'1st-March-2019',
	'post_content':'You wont all leave'}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts, title='home')

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title="Login", form=form)

@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title="Register", form=form)

@app.route("/about")
def about():
	return render_template('about.html')

if __name__=='__main__':
	app.run(debug=True)
