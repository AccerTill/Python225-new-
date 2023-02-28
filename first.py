import sqlite3
import os
from flask import Flask, render_template, \
    url_for, request, flash, session, redirect, abort, g
from FDataBase import FDataBase



DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'b1900f3b6f17742971fb2513ce3347f43f1b560a'



# in console generation of code:
# import os
#os.urandom(20).hex()
#  'b1900f3b6f17742971fb2513ce3347f43f1b560a'



# ------ вызываем базу в консоли:    from first import create_db
                           #  create_db()



app = Flask(__name__)
# app.config['SECRET_KEY'] = 'n5h5j3k34434k343hh5h4jkk3' # задокументировали
                                                        # так как использовали выше.
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))



# доступ к базе данных:
def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('1sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()



menu =  [ {'name':'Main',     'url': 'index'},
          {'name':'About us', 'url': 'about'},
          {'name':'Feedback', 'url': 'contact'}  ]


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db




#  index.html
@app.route('/index')
@app.route('/')
def index():
    db = get_db()
    dbase = FDataBase(db)
    # return render_template('indexDZ.html')
    # print(url_for("index"))
    # return render_template('index.html', title = 'Main (index.html).', menu=menu)
    return render_template("index.html", title="Главная", menu=dbase.get_menu(),
                            posts=dbase.get_posts_anonce())


# добавление статьи (add_post.html)
@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db) # GET

    if request.method == "POST": # POST
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash("Ошибка добавления статьи", category="error")
            else:
                flash("Статья добавлена успешно", category="success")
        else:
            flash("Ошибка добавления статьи", category="error") # POST


    return render_template('add_post.html', menu=dbase.get_menu(), title="Добавление статьи") # GET



#  about.html
@app.route('/about')
def about():
      # print(url_for('about'))
      return render_template('about.html',
                             title = 'About (about.html).', menu=menu)


@app.route("/profile/<path:username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401) # -------------- прерываем.
    return f" User of page: {username}"



# contact.html
@app.route('/contact', methods = ["POST", "GET"])
def contact():
      if request.method == 'POST':
          if len(request.form['username']) > 2:
              flash('Message has been sent successfully.', category='success')
          else:
              flash('Message has error!', category='error')
          # print(request.form['username'])
          # context = {
          #     'username' : request.form ['username'],
          #     'email': request.form['email'],
          #     'message': request.form['message']
          # }
          # return render_template('contact.html',
          #                        **context, title = 'Feedback (contact.html)',
          #                        menu=menu)
      return render_template('contact.html', title = 'Feedback (contact.html)',
                             menu=menu)



#  для ЛОГИНА (login.html) (to http://127.0.0.1:5000/profile/Serge)
@app.route("/login", methods = ["POST", "GET"])
def login():

    if 'userLogged' in session:   # ---------------- встроеная во flask - 'userLogged'
        return redirect(url_for('profile', username=session['userLogged']))

    elif request.method == 'POST' and request.form['username'] == 'Serge' and \
            request.form['passw'] == '123456':
        session['userLogged'] = request.form['username']


        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='Autorization',
                           menu=menu)



#  для несуществующей страницы (page404.html)
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Page not found(404)',
                           menu=menu), 404



# закрытие соединения с базой при окончании работы запроса.
@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'link_db'):
        g.link_db.close()



if __name__ == '__main__':
        app.run(debug = True)

# get_flashed-messages()