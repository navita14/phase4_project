from flask import Flask, request, jsonify, session, flash, redirect, url_for
from flask_migrate import Migrate
from models import *
from flask_cors import CORS
# from flask_restful import Api, Resource
import os
# from flask_login import LoginManager
from flask_login import login_required, current_user



BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db.init_app(app)
migrate = Migrate(app, db)

excluded_endpoints = ['login', 'signup', 'check_session', 'root']


# @app.route('/dashboard')
# @login_required
# def dashboard():
#     permission_level = current_user.permission_level
#     return jsonify({'permission_level': permission_level})


# @app.before_request
# def check_logged_in():
#     if request.endpoint not in excluded_endpoints:
#         user_id = session.get('user_id')
#         user = User.query.filter(User.id == user_id).first()

#         if not user:
#             # invalid cookie
#             return {'message': 'invalid session'}, 401


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
    
    if user.authenticate(data['password']):
        # passwords matched, add cookie
        session['user_id'] = user.id
        return {'message': 'login success'}, 201
    else:
        # password did not match, send error resp
        return {'message': 'login failed'}, 401
    

@app.route('/check_session')
def check_session():
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()

    if not user:
        # invalid cookie
        return {'message': 'invalid session'}, 401
    
    # valid cookie
    return {'message': 'valid session'}, 200

@app.route('/logout', methods=['DELETE'])
def logout():
    # delete cookie
    session.pop('user_id')
    return {'message': 'logged out'}, 200


@app.route('/change-password', methods=['POST'])
def change_password():
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')

    if new_password != confirm_password:
        flash("New password and confirm password do not match", "error")
    else:
        # Update the user's password in the database (assuming you have a User model)
        current_user = User.query.filter_by(username=session.get('username')).first()
        if current_user:
            current_user.password_hash = new_password  # This will automatically hash and store the new password
            db.session.commit()

            flash("Password reset successful", "success")
    return redirect(url_for('login'))


@app.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    body = [user.to_dict() for user in users]
    return body, 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)