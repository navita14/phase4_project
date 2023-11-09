from app import app, db
from models import User, Post

def clear_database():
    with app.app_context():
        ## Delete all the existing records - Yes Nav we need this lol -- Dommo
        User.query.delete()
        Post.query.delete()
        db.session.commit()

def populate_database():
    with app.app_context():
        ## Dummy user data - It's all bullshit we'll change in full version
        dummy_users = [
            User(
                email_address="BossyNav@flatironschool.com",
                username="BossyNav",
                full_name="Navita Ramasar",
                _password_hash="abc123",
                # permission_level=1,
            ),
            User(
                email_address="Dommo@flatironschool.com",
                username="Young_Drac",
                full_name="Dominick Addison",
                _password_hash="abc123",
                # permission_level=2,
            ),
            User(
                email_address="BrianTheStallion@flatironschool.com",
                username="BrianTheStallion",
                full_name="Brian Jara",
                _password_hash="abc123",
                # permission_level=1,
            ),
            User(
                email_address="FurFoxFan@flatironschool.com",
                username="SmashLucas_Teh_FurFoxFan",
                full_name="Lucas Furfan der Heyde",
                _password_hash="hashed_password_for_smashlucas",
                # permission_level=2,
            ),
            User(
                email_address="HentaiLuvr@flatironschool.com",
                username="HentaiLuvr",
                full_name="Kerem Deen",
                _password_hash="hashed_password_for_hentailuvr",
                # permission_level=1,
            ),
            User(
                email_address="EpsteinsHomey@flatironschool.com",
                username="EpsteinsHomey",
                full_name="Juan Larco",
                _password_hash="hashed_password_for_epsteinshomey",
                # permission_level=1,
            ),
                        User(
                email_address="Hanan@flatironschool.com",
                username="H as in Harry, A as in Apple, N as in Nancy, A as in Apple, N as in Nancy",
                full_name="Hanan Hammouda",
                _password_hash="hashed_password_for_Hanan",
                # permission_level=3,
            ),
        ]

        ## Dummy post data
        dummy_posts = [
            Post(
                content="/post_data/Pictures/The_Gang.jpg", ## I added a folder called post_data and added an image. We'll have to think of a way to link this. Json is NOT the way to go.
                description="My gang, Flatiron REPRESENT!",
                likes=10,
                comments="Comment 1 for post 1",
                user_id=2,  ## User 2's ID -- This should link to me -- Dommo
            ),
            Post(
                content="/post_data/Pictures/HananNav.jpg",
                description="Me and Nav!",
                likes =18,
                comments = "",
                user_id=7
            ),
            ## If you have anything else to add, do it here!
        ]

        for user in dummy_users:
            db.session.add(user)

        for post in dummy_posts:
            db.session.add(post)

        db.session.commit()

if __name__ == "__main__":
    clear_database()  ## Clear existing data -- If it doesn't work after this ask Ben lol
    populate_database()