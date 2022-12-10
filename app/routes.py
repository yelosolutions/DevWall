from flask import render_template, url_for
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from .models import User, Post, Comment, Portfolio, Tag, Follow 
from werkzeug.security import check_password_hash
from .forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse


@app.route('/index')
def index():
    return render_template('index.html', title='index')

@app.route('/base')
def base():
    return render_template('base.html', title='base')

@app.route('/profile')
def profile():
    # code for rendering the user profile page
    return render_template('profile.html')

@app.route('/landing')
def landing():
    return render_template('landing.html', title='landing page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('')
        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)




@app.route('/signup')
def signup():
    return render_template('signup.html', title='signup')

@app.route('/')
@app.route('/home')
@login_required
def home():
    posts = Post.query.order_by(Post.timestamp.desc()).limit(10).all()
    return render_template('home.html', posts=posts)

@app.route('/user/<username>')
def user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc()).limit(10).all()
    comments = user.comments.order_by(Comment.timestamp.desc()).limit(10).all()
    portfolio = user.portfolio.order_by(Portfolio.title).all()
    return render_template('user_profile.html', user=user, posts=posts, comments=comments, portfolio=portfolio)

@app.route('/post/<int:post_id>')
def post(post_id):
    post =Post.query.get_or_404(post_id)
    comments = post.comments.order_by(Comment.timestamp.asc()).all()
    return render_template('post.html', post=post, comments=comments)

@app.route('/portfolio/<username>')
def portfolio(username):
    user = User.query.filter_by(username=username).first_or_404()
    portfolio = user.portfolio.order_by(Portfolio.title).all()
    return render_template('portfolio.html', user=user, portfolio=portfolio)

@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first_or_404()
    follow = Follow.query.filter_by(follower=current_user, followee=user).first()
    if follow is None:
        follow = Follow(follower=current_user, followee=user)
        db.session.add(follow)
        db.session.commit()
    return redirect(url_for('user_profile', username=username))

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first_or_404()
    follow = Follow.query.filter_by(follower=current_user, followee=user).first()
    if follow is not None:
        db.session.delete(follow)
        db.session.commit()
    return redirect(url_for('user_profile', username=username))

@app.route('/search')
def search():
    query = request.args.get('q')
    users = User.query.filter(User.username.contains(query)).all()
    posts = Post.query.filter(Post.title.contains(query)).all()
    tags = Tag.query.filter(Tag.name.contains(query)).all()
    return render_template('search.html', query=query, users=users, posts=posts, tags=tags)

@app.route('/admin')
@login_required
def admin():
    # Admin controls go here
    return render_template('admin.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('landing'))
