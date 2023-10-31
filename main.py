from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

app = Flask(__name__)

# For WTForm CSFR token creation
app.secret_key = "my secret key 43"

my_email = 'a@b.hu'
my_password = '1234567890'

bootstrap = Bootstrap5(app)
app.config['BOOTSTRAP_BTN_STYLE'] = 'dark'


# Our WTForm Class contains all of Form element for Login Form
class LoginForm(FlaskForm):
	email = StringField(
		'Email:',
		validators=[DataRequired(message='Please enter your email address.'),
					Regexp(r"^[-\w\.\+]+@([-\w]+\.)+[-\w\ ]{2,4}$",
						   message='This field requires a valid email address')])
	password = PasswordField(' Password: ', [DataRequired(message='Please enter your password.'), Length(min=10, max=35,
																										 message='Password must be between 10 and 35 character.')])
	submit = SubmitField('Log in')


@app.route("/")
def home():
	return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
	# Create an instance of the LoginForm class and pass it to the Login page
	login_form = LoginForm()
	# login_form.validate_on_submit()

	if request.method == 'GET':
		return render_template('login.html', form=login_form)

	elif request.method == 'POST' and login_form.validate_on_submit():
		if login_form.email.data == my_email and login_form.password.data == my_password:
			return render_template('success.html')
		else:
			return render_template('denied.html')
	else:
		return render_template('login.html', form=login_form)


if __name__ == '__main__':
	app.run(debug=True)
