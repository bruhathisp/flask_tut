from flask import Flask, redirect, render_template, url_for

app= Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
#this is a coo
@app.route("/<name>")
def user(name):
    return render_template("index.html", content=['1', '2','30','4','5'] )



@app.route("/admin/")
def admin():
    return redirect(url_for("user",name="admin page"))

    
if __name__ == "__main__":
    app.run()

#create a new page


