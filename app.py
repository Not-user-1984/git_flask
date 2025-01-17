from flask import Flask, render_template, request, redirect, url_for
from models.post import db, Post
from models.seed import create_fake_posts, delete_all_posts

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


def initialize_data():
    with app.app_context():
        db.create_all()
        if Post.query.count() == 0:
            create_fake_posts()




@app.teardown_appcontext
def cleanup_data(exception=None):
    if hasattr(app, 'data_initialized'):
        delete_all_posts()
        delattr(app, 'data_initialized')


@app.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts)

# @app.route("/create", methods=["GET", "POST"])
# def create_post():
#     if request.method == "POST":
#         title = request.form["title"]
#         content = request.form["content"]
#         post = Post(title=title, content=content)
#         db.session.add(post)
#         db.session.commit()
#         return redirect(url_for("index"))
#     return render_template("create_post.html")


if __name__ == "__main__":
    initialize_data()
    app.run(debug=True)
