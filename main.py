print("pls work")
from flask import Flask, render_template, request, redirect, url_for
from replit import db 
"""
db["Barbaric"] = { "author":"Barry", "rating":"2", "image": "https://i.pinimg.com/736x/68/f2/4c/68f24c81b5b82bee2be4b2bdd699bd1c.jpg", "df":"2/2/2", "review":"none"}
"""


app = Flask('app')

@app.route('/', methods = ["GET", "POST" ])
def hello_world():
    return render_template(
        'index.html', db=db, sorteddb = sorted( db.keys(),key=str.lower)
    )
    #can do ,reverse = true

@app.route("/book/<title>")
def home_func(title):
    return render_template("test1.html", title=title, book=db[title], db=db)

@app.route('/allbooks')
def books_all():
    return render_template('all.html', db=db)
    
@app.route('/form')
def new_template():
    return render_template('Form.html')

#does this work or leqve it?
@app.route('/formafter')
def form_after():
    return render_template('Proof form worked.html',db=db,)
    
#

#for form but why doesnt it work
print("carzy")

@app.route('/formafter', methods=['GET', 'POST'])
def form():
  if request.method == 'POST':
    title = request.form['title']
    userauthor = request.form['userauthor']
    userstars= request.form['userstars']
    userimage= request.form['userimage']
    userdf= request.form['userdf']
    userrev= request.form['userrev']
    userdf = str(userdf)
    userdf= "2024-02-05"
    useryear = userdf[0:4]
    usermonth = userdf[4:8]
    userday = userdf[8:10]
    userdf = userday+usermonth+useryear
    db[title]= { "author":userauthor, "rating":userstars, "image": userimage, "df":userdf, "review":userrev}
    print("ho")
    return db[title]
  else:
    return render_template('index.html')

@app.route('/delete/<title>', methods=['Get','POST'])
def delete_book(title):
    del db[title]
    return redirect(url_for('hello_world'))

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == "GET":
        return "something odd going on"
    query = request.form.get("query")
    matches=[]
    queryl = query.lower()
    for key in db.keys():
        keyl = key.lower()
        if queryl in keyl:
            ifone = key
            matches.append(key)
    if len(matches) > 1:
        return redirect(url_for('multiple_matches', matches=matches))
    elif len(matches)== 1:
        return redirect(url_for('home_func' , title = ifone, query = query))
    else:
        return redirect(url_for('no_matches'))
    
    

@app.route("/multi")
def multiple_matches():
    return render_template("matches.html", matches=request.args.getlist("matches"), db=db)

@app.route("/nomulti")
def no_matches():
    return render_template("nomatches.html")
            
            




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
