from app import app
import flask

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
