from faker import Faker
from .post import db, Post

def create_fake_posts(num_posts=20):
    fake = Faker()
    for _ in range(num_posts):
        post = Post(
            title=fake.sentence(nb_words=6),
            content=fake.text(max_nb_chars=200)
        )
        db.session.add(post)
    db.session.commit()

def delete_all_posts():
    Post.query.delete()
    db.session.commit()