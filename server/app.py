from flask import Flask, request, jsonify, session, flash, redirect, url_for
from flask_migrate import Migrate
from models import *
from flask_cors import CORS
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Bad_Banana"
app.json.compact = False

db.init_app(app)
migrate = Migrate(app, db)

excluded_endpoints = ['login', 'signup', 'check_session', 'root']

@app.route('/')
def homepage():
    body = 'This is your homepage'
    return body, 200

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    body = [user.to_dict() for user in users]
    return body, 200

@app.route('/posts', methods=['GET'])
def get_posts():
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
    user = User.query.filter(User.username == data['username']).first()

    if not user:
        return {'message': 'user not found'}, 404
    elif user.authenticate(data['_password_hash']):
        session['user_id'] = user.id
        return {'message': 'login success', 'user_id': user.id}, 201  # Include 'user_id'
    else:
        return {'message': 'login failed'}, 401

@app.route('/logout', methods=['DELETE'])
def logout():
    session.pop('user_id')
    return redirect(url_for('login'))  # Corrected closing parenthesis

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(
        content=data.get('content'),
        description=data.get('description'),
        likes=data.get('likes'),
        comments=data.get('comments'),
        user_id=data.get('user_id')
    )
    db.session.add(new_post)
    db.session.commit()
    return {'message': 'post created'}, 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)
