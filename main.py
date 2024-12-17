from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/devlog")
def devlog():
    return render_template("devlog.html")

@app.route("/image")
def image():
    return render_template("image.html")


if __name__ == '__main__':
    app.run()