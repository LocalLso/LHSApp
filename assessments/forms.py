from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AssessmentForm(FlaskForm):
    question = StringField('Question', validators=[DataRequired()])
    answer = StringField('Answer', validators=[DataRequired()])
    submit = SubmitField('Add')

class AnswerForm(FlaskForm):
    answer = StringField('Your Answer', validators=[DataRequired()])
    submit = SubmitField('Submit')

