from app import app, db, oid, lm
import flask
import forms
import flask.ext.login as flasklogin
from models import User, Post

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
@oid.loginhandler
def login():
    if flask.g.user is not None and flask.g.user.is_authenticated():
        return flask.redirect(flask.url_for('index'))

    form = forms.LoginForm()

    if form.validate_on_submit():
        flask.session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])

    return flask.render_template('login.html', title='login', form=form, providers=app.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == '':
        flask.flash('Invalid Login -- Try Again')
        return redirect(url_for('login'))

    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        #We haven't registered this user yet
        #Add user to the database
        nickname = resp.nickname
        if nickname is None or nickname == '':
            nickname = resp.email.split('@')[0]
        user = User(email=resp.email, nickname=nickname)
        db.session.add(user)
        db.session.commit()

    remember_me = False
    if 'remember_me' in flask.session:
        remember_me = flask.session['remember_me']
        flask.session.pop('remember_me', None)


    flasklogin.login_user(user, remember=remember_me)
    return flask.redirect(flask.request.args.get('next') or flask.url_for('index'))




@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    flask.g.user = flasklogin.current_user
