from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class TextForm(FlaskForm):
    text = TextAreaField("Write your text here:", validators=[DataRequired()])
    submit = SubmitField("Check Sentiment")
