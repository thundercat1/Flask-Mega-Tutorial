from app import app
import flask
import forms

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Allison'}

    posts = [
            {
                'author': {'nickname': 'John'},
                'body': 'We\'re on an airplane!'
            },
            {
                'author': {'nickname': 'Suzy'},
                'body': 'I work in an office!'
            }
        ]
    return flask.render_template('index.html', title='home', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        flask.flash('Login requested for "%s". Remember me: "%s"' %
                (form.openid.data, str(form.remember_me.data)))
        return flask.redirect('/index')

    return flask.render_template('login.html', title='login', form=form, providers=app.config['OPENID_PROVIDERS'])
