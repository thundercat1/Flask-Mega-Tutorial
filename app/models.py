from app import db
from hashlib import md5

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    last_seen = db.Column(db.DateTime)
    about_me = db.Column(db.String(500))


    def is_authenticated(self):
        #Doesn't really mean authenticated
        return True

    def is_active(self):
        #Whatever this is
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %s>' % (self.nickname)

    def avatar(self, size):
    	return 'http://gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf8')).hexdigest(), size)

    


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %s>' % (self.body)
