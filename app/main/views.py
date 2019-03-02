from flask import render_template,request,redirect,url_for,abort
from ..models import User,Post,Comment
from . import main
from .forms import PostForm,CommentForm,UpdateProfile
from .. import db,photos
from flask_login import login_required,current_user
import markdown2

@main.route('/',methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best News Review Website Online'
    posts=Post.query.all()
    comments=Comment.query.all()
    print(posts)
    users= None
    for post in posts:

        for comment in comments:

            return render_template('index.html', title = title,posts=posts, users=users)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update/bio',methods = ['GET','POST'])
@login_required
def update_bio(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update_bio.html',form =form)

# @main.route('/user/update/pitch/<id>',methods = ['GET','POST'])
# def single_review(id):
#     pitch=Pitch.query.get(id)
#     if pitch is None:
#         abort(404)
#     form = PitchForm()
#
#     if form.validate_on_submit():
#         user.pitches = form.pitches.data
#
#         db.session.add(user)
#         db.session.commit()
#
#         return redirect(url_for('.profile',pitch=user.pitches))
#
#     format_pitch = markdown2.markdown(pitch.movie_pitch,extras=["code-friendly", "fenced-code-blocks"])
#     return render_template('new_pitch.html',pitch = pitch,format_pitch=format_pitch)

@main.route('/new_post/',methods = ['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(name = form.name.data, user_id = current_user.id)
        db.session.add(post)
        db.session.commit()
        # user=User.query.filter_by(id = current_user.id).first()
        # return redirect(url_for('.new_post',uname=user.username))

        return redirect(url_for('.index'))
    return render_template('profile/new_post.html',post_form=form)

@main.route('/new_comment/<int:id>',methods = ['GET','POST'])
def new_comment(id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(name = form.name.data, post_id = id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('.index'))

    return render_template('profile/new_comment.html',comment_form=form)

# @main.route('/new_vote/',methods = ['GET','POST'])
# @login_required
# def new_vote():
#     form = VoteForm()
#     # votes = get_vote(id)
#
#     if form.validate_on_submit():
#         pitch = Pitch(name = form.name.data, user_id = current_user.id)
#         upvote = Vote(upvote = form.validate_on_submit(),pitch_id = pitch.id)
#         downvote = Vote(downvote = form.validate_on_submit(),pitch_id = pitch.id)
#         up=0
#         down=0
#         for upvote in vote:
#             up+=1
#             db.session.add(upvote=up)
#             db.session.commit()
#         for downvote in vote:
#             down+=1
#             db.session.add(downvote=down)
#             db.session.commit()
#         user=User.query.filter_by(id = pitch.id).first()
#         return redirect(url_for('.index'))
#
#     return render_template('profile/new_comment.html',comment_form=form)
#     return render_template('new_vote.html',upvote = upvote, downvote = downvote, vote_form=form, votes=votes)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
