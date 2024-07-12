print("pls work")
from flask import Flask, render_template, request, redirect, url_for
from replit import db 


app = Flask('app')

@app.route('/', methods = ["GET", "POST" ])
def index():
    return render_template(
        'index.html', db=db, sorteddb = sorted( db.keys(),key=str.lower)
    )
    #can do ,reverse = true

@app.route("/book/<title>") 
def home_func(title):
    return render_template("test1.html", title=title, book=db[title], db=db)

@app.route("/edit/<title>")
def form_edit(title):
    hi = title
    return render_template("EditForm.html", title=title, book=db[title], db=db)
    
@app.route('/form')
def new_template():
    return render_template('Form.html')

#For the form to add a additional books to db
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
    useryear = userdf[0:4]
    usermonth = userdf[4:8]
    userday = userdf[8:10]
    userdf = userday+usermonth+useryear
    db[title]= { "author":userauthor, "rating":userstars, "image": userimage, "df":userdf, "review":userrev}
    
  else:
      return render_template("Proof_worked.html")

@app.route('/delete/<title>', methods=['Get','POST'])
def delete_book(title):
    del db[title]
    return redirect(url_for('index'))

@app.route('/search', methods=['GET','POST'])
def search():
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
