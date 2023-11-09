from flask import Flask, request, jsonify, session, flash, redirect, url_for
from flask_migrate import Migrate
from models import *
from flask_cors import CORS
from werkzeug.utils import secure_filename

# from flask_restful import Api, Resource
import os
# from flask_login import LoginManager
# from flask_login import login_required, current_user



BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Bad_Banana"
app.json.compact = False
UPLOAD_FOLDER = '/post_data/Pictures/'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db.init_app(app)
migrate = Migrate(app, db)

excluded_endpoints = ['login', 'signup', 'check_session', 'root']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # @app.route('/dashboard')
# # @login_required
# # def dashboard():
# #     permission_level = current_user.permission_level
# #     return jsonify({'permission_level': permission_level})


# # @app.before_request
# # def check_logged_in():
# #     if request.endpoint not in excluded_endpoints:
# #         user_id = session.get('user_id')
# #         user = User.query.filter(User.id == user_id).first()

# #         if not user:
# #             # invalid cookie
# #             return {'message': 'invalid session'}, 401


# @app.route('/signup', methods=['POST'])
# def signup():
#     data = request.get_json()
#     new_user = User(username=data['username'])
#     new_user.password_hash = data['_password_hash']
#     new_user.email_address = data['email_address']
#     new_user.full_name = data['full_name']
#     db.session.add(new_user)
#     db.session.commit()

#     return {'message': 'user added'}, 201

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()

#     # check if user exists
#     user = User.query.filter(User.username == data['username']).first()

#     if not user:
#         return {'message': 'user not found'}, 404
    
#     if user.authenticate(data['password']):
#         # passwords matched, add cookie
#         session['user_id'] = user.id
#         return {'message': 'login success'}, 201
#     else:
#         # password did not match, send error resp
#         return {'message': 'login failed'}, 401
    

# @app.route('/check_session')
# def check_session():
#     user_id = session.get('user_id')
#     user = User.query.filter(User.id == user_id).first()

#     if not user:
#         # invalid cookie
#         return {'message': 'invalid session'}, 401
    
#     # valid cookie
#     return {'message': 'valid session'}, 200


# @app.route('/change-password', methods=['POST'])
# def change_password():
#     new_password = request.form.get('new_password')
#     confirm_password = request.form.get('confirm_password')

#     if new_password != confirm_password:
#         flash("New password and confirm password do not match", "error")
#     else:
#         # Update the user's password in the database (assuming you have a User model)
#         current_user = User.query.filter_by(username=session.get('username')).first()
#         if current_user:
#             current_user.password_hash = new_password  # This will automatically hash and store the new password
#             db.session.commit()

#             flash("Password reset successful", "success")
#     return redirect(url_for('login'))


# @app.route('/users', methods=['GET'])
# def users():
#     users = User.query.all()
#     body = [user.to_dict() for user in users]
#     return body, 200


@app.route('/')
def homepage():
        body = 'This iawbfopbaf'
        return body,200

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    body = [user.to_dict() for user in users]
    return body, 200

@app.route('/post', methods=['GET'])
def get_post():
    posts = Post.query.all()
    body = [post.to_dict() for post in posts]
    return body, 200

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    new_user = User(username=data['username'])
    new_user.password_hash = data['_password_hash']
    new_user.email_address = data['email_address']
    new_user.full_name = data['full_name']
    db.session.add(new_user)
    db.session.commit()

    return {'message': 'user added'}, 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # check if user exists
    user = User.query.filter(User.username == data['username']).first()

    if not user:
        return {'message': 'user not found'}, 404
    elif user:
        if user.authenticate(data['_password_hash']):
            # passwords matched, add cookie
            session['user_id'] = user.id
            return {'message': 'login success'}, 201
        else:
            # password did not match, send error resp
            return {'message': 'login failed'}, 401

@app.route('/logout', methods=['DELETE'])
def logout():
    # delete cookie
    session.pop('user_id')
    return redirect(url_for('login'))
    # return {'message': 'logged out'}, 200

    

@app.route('/post', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}, 400)

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}, 400)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        description = request.form.get('description', '')
        likes = request.form.get('likes', 0)
        username = request.form.get('username', 'username')  # You should replace this with user authentication

        try:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            post = Post(filename=filename, description=description, likes=likes, username=username)
            db.session.add(post)
            db.session.commit()

            return jsonify({'message': 'File uploaded successfully', 'post': post.to_dict()}, 200)
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Failed to upload file. Please try again later.'}, 500)
    else:
        return jsonify({'error': 'Invalid file type'}, 400)



if __name__ == '__main__':
    app.run(port=5000, debug=True)