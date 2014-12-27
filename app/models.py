from app import db

class user(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), unique=True, index=True)
	email = db.Column(db.String(120), index=True, unique=True)


	def __repr__(self):
		return '<User %s>' % (self.nickname)
