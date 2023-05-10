from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/8520be10ffd2bf2822c7").json()

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_number>")
def show_post(post_number):
    return render_template("post.html", posts=posts, post_number=post_number)


if __name__ == "__main__":
    app.run(debug=True)
