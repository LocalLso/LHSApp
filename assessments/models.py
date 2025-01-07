from app import db

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(200), nullable=False)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessment.id'), nullable=False)
    score = db.Column(db.Float, nullable=False)
    assessment = db.relationship('Assessment', backref=db.backref('grades', lazy=True))

