from flask import Flask, render_template, url_for
from .forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']= '121ccc21d257386c2c56ad40e01fb14f'

posts = [
    {
        'author': "John",
        'title': "Ram",
        'content': "hello",
        'date_posted': 'heljrlj',
    },
    {
        'author': "Doe",
        'title': "Ram",
        'content': "hello",
        'date_posted': 'heljrlj',
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title="Register", form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)