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
                        Post(
                content="/post_data/Pictures/LucasGlass.jpg",
                description="Felt cute, might send to ur mom l8r!",
                likes =69,
                comments = "",
                user_id=4
            ),
                                    Post(
                content="/post_data/Pictures/Nav.jpg",
                description="lyKe oMg tOteS lOoKiNg lyKe a CuDdLy bEaR :3",
                likes =-44,
                comments = "",
                user_id=1
            ),
                 Post(
                content="/post_data/Pictures/thefullgroup.jpg",
                description="We took the shortcut to the mall... it took 40 minutes!",
                likes =24,
                comments = "",
                user_id=2
            ),
                             Post(
                content="/post_data/Pictures/brian2.jpg",
                description="Working hard or hardly working??",
                likes =44,
                comments = "",
                user_id=3
            ),
                            Post(
                content="/post_data/Pictures/cleankerem.jpg",
                description="Can't always be a rapscallion ya know?",
                likes =391,
                comments = "",
                user_id=5
            ),
                Post(
                content="/post_data/Pictures/art.jpg",
                description="❤️❤️❤️I am so thankful for my friends I luv them very much ❤️❤️❤️",
                likes =103,
                comments = "",
                user_id=4
            ),
                            Post(
                content="/post_data/Pictures/cookout.jpg",
                description="We eatin GOOD",
                likes =21,
                comments = "",
                user_id=7
            ),
                                         Post(
                content="/post_data/Pictures/brian1.jpg",
                description="Hey, thats me working on THIS project!",
                likes =91,
                comments = "",
                user_id=3
            ),
                 Post(
                content="/post_data/Pictures/juanny.jpg",
                description="Mood: Feelin' myself",
                likes =229,
                comments = "",
                user_id=6
            ),
                Post(
                content="/post_data/Pictures/hentai.jpg",
                description="I love my girls",
                likes =6969,
                comments = "",
                user_id=5
            ),
        ]




        for user in dummy_users:
            db.session.add(user)

        for post in dummy_posts:
            db.session.add(post)

        db.session.commit()

if __name__ == "__main__":
    clear_database()  ## Clear existing data -- If it doesn't work after this ask Ben lol
    populate_database()