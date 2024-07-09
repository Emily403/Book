
from flask import Flask, render_template 
from replit import db


db["Awsome"] = { "author":"Andy", "rating":"1",  "image":"https://i.pinimg.com/originals/86/14/09/861409c0a92f6777d9b07346766fa00f.gif", "Date finished":"1/1/1"}
db["Barbaric"] = { "author":"Barry", "rating":"2", "image": "https://i.pinimg.com/736x/68/f2/4c/68f24c81b5b82bee2be4b2bdd699bd1c.jpg", "Date finished":"2/2/2"}
db["Cool"] = { "author":"Cecil", "rating":"3", "image":"https://i.pinimg.com/736x/63/91/d4/6391d47ec03aa844555dccba7db5fabf.jpg", "Date finished":"3/3/3"}

"""del db["Barbatic"]"""

app = Flask('app')

@app.route('/')
def hello_world():
    return render_template(
        'index.html', db=db
    )


@app.route("/book/<title>")
def home_func(title):
    return render_template("test1.html", title=title, book=db[title])

@app.route('/form')
def new_template():
    return render_template('Form.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
