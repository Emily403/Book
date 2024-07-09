print("pls work")
from flask import Flask, render_template, request 
from replit import db


db["Awsome"] = { "author":"Andy", "rating":"1",  "image":"https://i.pinimg.com/originals/86/14/09/861409c0a92f6777d9b07346766fa00f.gif", "df":"1/1/1"}
db["Barbaric"] = { "author":"Barry", "rating":"2", "image": "https://i.pinimg.com/736x/68/f2/4c/68f24c81b5b82bee2be4b2bdd699bd1c.jpg", "df":"2/2/2"}
db["Cool"] = { "author":"Cecil", "rating":"3", "image":"https://i.pinimg.com/736x/63/91/d4/6391d47ec03aa844555dccba7db5fabf.jpg", "df":"3/3/3"}
db["Dead"] = { "author":"Dad", "rating":"4",  "image":"https://i.pinimg.com/originals/86/14/09/861409c0a92f6777d9b07346766fa00f.gif", "df":"4/4/4"}

"""del db["H"]"""

app = Flask('app')

@app.route('/')
def hello_world():
    return render_template(
        'index.html', db=db,
    )


@app.route("/book/<title>")
def home_func(title):
    return render_template("test1.html", title=title, book=db[title])

@app.route('/form')
def new_template():
    return render_template('Form.html')

#does this work or leqve it?
@app.route('/formafter')
def form_after():
    return render_template('Proof form worked.html',db=db)
#


#for form but why doesnt it work
print("carzy")

@app.route('/formafter', methods=['GET', 'POST'])
def form():
  if request.method == 'POST':
    name = request.form['title']
    userauthor = request.form['userauthor']
    userstars= request.form['userstars']
    userimage= request.form['userimage']
    userdf= request.form['userdf']
    # Process the name here (e.g., store it in a database)
    db[name]= { "author":userauthor, "rating":userstars, "image": userimage, "df":userdf}
    print("ho")
    return db[title]
  else:
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
