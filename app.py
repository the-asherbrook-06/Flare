from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.errorhandler(404)
def _404Error(e):
    return render_template('404.html')


@app.route("/")
def base():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug= True)