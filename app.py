from flask import Flask, render_template, request, redirect, session, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///documents.db'

app.secret_key = "abc123"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(100),
        nullable=False
    )


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(
        db.String(200),
        nullable=False
    )

    category = db.Column(
        db.String(100),
        nullable=False
    )

    file_path = db.Column(
        db.String(300)
    )


with app.app_context():
    db.create_all()

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(
            username=username,
            password=password
        ).first()

        if user:
            session["user"] = username
            return redirect("/index")

        return "Sai tài khoản hoặc mật khẩu"

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        check_user = User.query.filter_by(
            username=username
        ).first()

        if check_user:
            return "Tên đăng nhập đã tồn tại"

        user = User(
            username=username,
            password=password
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/")

    return render_template("register.html")

@app.route("/index")
def index():

    if "user" not in session:
        return redirect("/")

    documents = Document.query.all()

    return render_template(
        "index.html",
        documents=documents
    )

@app.route("/add", methods=["GET", "POST"])
def add():

    if "user" not in session:
        return redirect("/")

    if request.method == "POST":

        title = request.form["title"]
        category = request.form["category"]

        filename = ""

        file = request.files["file"]

        if file and file.filename != "":

            filename = secure_filename(file.filename)

            file.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    filename
                )
            )

        doc = Document(
            title=title,
            category=category,
            file_path=filename
        )

        db.session.add(doc)
        db.session.commit()

        return redirect("/index")

    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    if "user" not in session:
        return redirect("/")

    document = Document.query.get(id)

    if request.method == "POST":

        document.title = request.form["title"]
        document.category = request.form["category"]

        file = request.files["file"]

        if file and file.filename != "":

            filename = secure_filename(file.filename)

            file.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    filename
                )
            )

            document.file_path = filename

        db.session.commit()

        return redirect("/index")

    return render_template(
        "edit.html",
        document=document
    )


@app.route("/delete/<int:id>")
def delete(id):

    if "user" not in session:
        return redirect("/")

    document = Document.query.get(id)

    db.session.delete(document)
    db.session.commit()

    return redirect("/index")


@app.route("/search", methods=["GET", "POST"])
def search():

    if "user" not in session:
        return redirect("/")

    results = []

    if request.method == "POST":

        keyword = request.form["keyword"]

        results = Document.query.filter(
            (Document.title.contains(keyword)) |
            (Document.category.contains(keyword))
        ).all()

    return render_template(
        "search.html",
        results=results
    )


@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/")
@app.route("/download/<filename>")
def download_file(filename):
    if "user" not in session:
        return redirect("/")

    return send_from_directory(
        app.config["UPLOAD_FOLDER"], 
        filename, 
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)