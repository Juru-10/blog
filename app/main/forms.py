from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PostForm(FlaskForm):

    name = StringField('Post',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    name = StringField('Comment',validators=[Required()])
    submit = SubmitField('Submit')

# class VoteForm(FlaskForm):
#
#     # upvote = StringField('Upvote',validators=[Required()])
#     # downvote = TextAreaField('Downvote')
#     upvote = SubmitField('Upvote')
    # downvote = SubmitField('Downvote')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
