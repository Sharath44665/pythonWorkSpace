from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

class CreateBlogForm(FlaskForm):
    blogPostTitle = StringField(label="Blog Post Title",validators=[DataRequired()])
    subTitle = StringField(label="SubTitle", validators=[DataRequired()])
    yourName = StringField(label="Your Name", validators=[DataRequired()])
    imgUrl = StringField(label="Image URL", validators=[DataRequired(),URL(require_tld=True, message="Please enter the url correctly")])
    blogArea = CKEditorField('Add your Blog', validators=[DataRequired()])
    submitButton = SubmitField(name="Submit Blog")


class RoughPostForm(FlaskForm):
    title = StringField('Title')
    body = CKEditorField('Body')  # <--
    submit = SubmitField('Submit')