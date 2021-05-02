import os
from flask import render_template,redirect,url_for,abort,request,flash
from app.main import main
from .forms import UpdateProfile,NewBlog
from flask_login import login_required,current_user
from ..email import mail_message
from app.models import User,Blog,Comment,Follower

@main.route('/')
def index():
    quotes = get_quotes()
    blogs = Blog.query.all()
    serialized_data = []
    for blog in blogs:
        serialized_data.append(blog.serialize)
    return render_template('index.html', quote = quotes,blogs=blogs)

@main.route('/new_post',methods=['POST','GET'])
@login_required
def new_blog():
    followers = Follower.query.all()
    form = NewBlog()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id =  current_user._get_current_object().id
        blog = Blog(title=title,content=content,user_id=user_id)
        blog.save()
        for follower in followers:
            mail_message("New Blog Post","email/new_blog",subscriber.email,blog=blog)
        return redirect(url_for('main.index'))
        flash('You Posted a new Blog')
    return render_template('newblogs.html', form = form)

@main.route('/blog/<blog_id>/update',methods = ['GET','POST'])
@login_required
def updatedblog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    form = NewBlog()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.content.data
        db.session.commit()
        flash("You have updated your Blog!")
        return redirect(url_for('main.blog',id = blog.id)) 
    if request.method == 'GET':
        form.title.data = blog.title
        form.content.data = blog.content
    return render_template('newblogs.html', form = form)

@blogs.route('/blog/<blog_id>/delete', methods=["DELETE"])
@login_required
def delete_post(blog_id):
    blog = Blog.query.filter_by(blog_id).first()
    db.session.delete(blog)
    db.session.commit()

    return jsonify("Blog was deleted"),200


@main.route('/user/<string:username>')
def user_posts(username):
    user = User.query.filter_by(username=username).first()
    return render_template('user.html',blogs=blogs,user = user)


@main.route('/follower',methods = ['POST','GET'])
def subscribe():
    email = request.form.get('follower')
    new_follower = Follower(email = email)
    new_follower.save_follower()
    mail_message("Subscribed to My-Blog","email/welcome_follower",new_follower.email,new_follower=new_follower)
    flash('Sucessfuly subscribed')
    return redirect(url_for('main.index'))
   
    
@main.route('/profile',methods = ['POST','GET'])
@login_required
def profile():
    form = UpdateProfile()
    if form.validate_on_submit():
        if form.profile_picture.data:
            picture_file = save_picture(form.profile_picture.data)
            current_user.profile_pic_path = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Succesfully updated your profile')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.bio.data = current_user.bio
    profile_pic_path = url_for('static',filename = 'photos/'+ current_user.profile_pic_path) 
    return render_template('profile/profile.html', profile_pic_path=profile_pic_path, form = form)


@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/updateprofile.html',form =form)

@main.route('/comment/<blog_id>', methods = ['Post','GET'])
@login_required
def comment(blog_id):
    blog = Blog.query.get(blog_id)
    comment =request.form.get('newcomment')
    new_comment = Comment(comment = comment, user_id = current_user._get_current_object().id, blog_id=blog_id)
    new_comment.save()
    return redirect(url_for('main.blog',id = blog.id))