from app import app, db
from models import User, Post

def clear_database():
    with app.app_context():
        ## Delete existing records
        User.query.delete()
        Post.query.delete()
        db.session.commit()

## Dummy user data -- This should suffice to set up some users we can play around with
dummy_users = [
    {
        "email_address": "BossyNav@flatironschool.com",
        "username": "BossyNav",
        "full_name": "Navita",
        "_password_hash": "hashed_password_for_bossynav",
        "permission_level": 1,
    },
    {
        "email_address": "Dommo@flatironschool.com",
        "username": "Young_Dracula",
        "full_name": "Dominick Addison",
        "_password_hash": "hashed_password_for_dommo",
        "permission_level": 2,
    },
    {
        "email_address": "BrianTheStallion@flatironschool.com",
        "username": "BrianTheStallion",
        "full_name": "Brian",
        "_password_hash": "hashed_password_for_brianthestallion",
        "permission_level": 1,
    },
    {
        "email_address": "FurFoxFan@flatironschool.com",
        "username": "SmashLucas_Teh_FurFoxFan",
        "full_name": "Lucas Van der Heyde",
        "_password_hash": "hashed_password_for_smashlucas",
        "permission_level": 2,
    },
    {
        "email_address": "HentaiLuvr@flatironschool.com",
        "username": "HentaiLuvr",
        "full_name": "Kerem Deen",
        "_password_hash": "hashed_password_for_hentailuvr",
        "permission_level": 1,
    },
    {
        "email_address": "EpsteinsHomey@flatironschool.com",
        "username": "EpsteinsHomey",
        "full_name": "Juan Larco",
        "_password_hash": "hashed_password_for_epsteinshomey",
        "permission_level": 1,
    },
]

## Dummy post data -- This should also suffice for our post setup. Not sure how we're fully implementing yet
dummy_posts = [
    {
        "content": "Sample content for post 1",
        "description": "Description 1",
        "likes": 10,
        "comments": "Comment 1 for post 1",
        "user_id": 1,  ## User 1's ID
    },
    ## If you have anything else to add, do it here!
]

def populate_database():
    with app.app_context():
        for user_data in dummy_users:
            user = User(**user_data)
            db.session.add(user)
        for post_data in dummy_posts:
            post = Post(**post_data)
            db.session.add(post)

        db.session.commit()

if __name__ == "__main__":
    clear_database()  ## Clear existing data -- Super Important so we don't keep this stuff
    populate_database()