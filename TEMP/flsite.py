import sqlite3
import os
from flask import Flask, render_template, request, g, flash, abort, redirect, url_for
from AFDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from AUserLogin import UserLogin
from Aforms import LoginForm, RegisterForm
from admin.admin import admin


DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'fdgfh78@#5?8gfhf89dx3v06k'
# USERNAME = 'admin'
# PASSWORD = '123'

MAX_CONTENT_LENGTH = 1024 * 1024

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))

app.register_blueprint(admin, url_prefix='/admin')

login_manager = LoginManager(app) # login manager (экземпляр класса)
login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "success"


#-----------------------------------------------------------
# здесь будет создаваться объект UserLogin при каждом запросе,
# если пользователь авторизован. Если не авторизован, то функция вызываться не будет.

@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().fromDB(user_id, dbase)

# ----------------------------------------------------------
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row       # для представления в виде словаря
    return conn                    # возвращает соединение
#---------------------------------------------------------------------------
def create_db():
    """Вспомогательная функция для создания таблиц БД"""
    db = connect_db()
    with app.open_resource('1sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()
#---------------------------------------------------------------------------
def get_db():
    '''Соединение с БД, если оно еще не установлено'''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db
#----------------------------------перехват запроса-------------------------
dbase = None
@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением запроса"""
    global dbase
    db = get_db()
    dbase = FDataBase(db)
#---------------------------------------------------------------------------

@app.route("/")
def index():
    # db = get_db() - # рописали в перехвате запроса
    # dbase = FDataBase(db)
    return render_template('1index.html', menu = dbase.getMenu(), posts=dbase.getPostsAnonce())
#---------------------------------------------------------------------------
@app.teardown_appcontext
def close_db(error):
    '''Закрываем соединение с БД, если оно было установлено'''
    if hasattr(g, 'link_db'):
        g.link_db.close()
#---------------------------------------------------------------------------
@app.route("/add_post", methods=["POST", "GET"])
def addPost():
    # db = get_db()
    # dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')

    return render_template('1add_post.html', menu=dbase.getMenu(), title="Добавление статьи")
#--------------------------------------------------------------------------------------------
@app.route("/post/<alias>")
@login_required    # только для авторизованных пользователей
def showPost(alias):
    # db = get_db()
    # dbase = FDataBase(db)
    title, post = dbase.getPost(alias)
    if not title:
        abort(404)

    return render_template('1post.html', menu=dbase.getMenu(), title=title, post=post)


#--------------------------------------------------------------------------------------------
#
#
# @app.route("/login")
# def login():
#     return render_template("1login.html", menu=dbase.getMenu(), title="Авторизация")

#------------
#------------
# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('profile'))
#
#     form = LoginForm()
#     return render_template("1login.html", menu=dbase.getMenu(),
#                            title="Авторизация", form=form)




# - закомментировали так как импортировали в (from forms import LoginForm):

    # if request.method == "POST":
    #     user = dbase.getUserByEmail(request.form['email'])
    #     if user and check_password_hash(user['psw'], request.form['psw']):
    #         userlogin = UserLogin().create(user)
    #         rm = True if request.form.get('remainme') else False
    #         login_user(userlogin, remember=rm)
    #         return redirect(request.args.get("next") or url_for("profile"))
    #
    #     flash("Неверная пара логин/пароль", "error")
    #
    # return render_template("1login.html", menu=dbase.getMenu(), title="Авторизация")



#           WTForms
@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    form = LoginForm()
    if form.validate_on_submit():
        user = dbase.getUserByEmail(form.email.data)
        # user = dbase.getUserByEmail(form.form['email'])

        if user and check_password_hash(user['psw'], form.psw.data):
        # if user and check_password_hash(user['psw'], request.form['psw']):
            userlogin = UserLogin().create(user)
            rm = form.remember.data
        #   rm=True if request.form.get('remaine') else False
            login_user(userlogin, remember=rm)
            return redirect(request.args.get("next") or url_for("profile"))

        flash("Неверная пара логин/пароль", "error")

    return render_template("1login.html", menu=dbase.getMenu(), title="Авторизация", form=form)




#--------------------------------------------------------------------------------------------
# @app.route("/register")
# def register():
#     return render_template("1register.html", menu=dbase.getMenu(), title="Регистрация")
#----------------------------------------------------------------------------------------

#                         REGISTER


# WTForms version:
@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hash = generate_password_hash(request.form['psw'])
        res = dbase.addUser(form.name.data, form.email.data, hash)
        if res:
            flash("Вы успешно зарегистрированы", "success")
            return redirect(url_for('login'))
        else:
            flash("Ошибка при добавлении в БД", "error")

    return render_template("1register.html", menu=dbase.getMenu(), title="Регистрация", form=form)



# ----------
# @app.route("/register", methods=["POST", "GET"])
# def register():
#     if request.method == "POST":
#         # session.pop('_flashes', None) #!!!
#         if len(request.form['name']) > 4 and len(request.form['email']) > 4 \
#                 and len(request.form['psw']) > 2 and request.form['psw'] == request.form['psw2']:
#             hash = generate_password_hash(request.form['psw'])
#             res = dbase.addUser(request.form['name'], request.form['email'], hash)
#             if res:
#                 flash("Вы успешно зарегистрированы", "success")
#                 return redirect(url_for('login'))
#             else:
#                 flash("Ошибка при добавлении в БД", "error")
#         else:
#             flash("Неверно заполнены поля", "error")
#
#     return render_template("1register.html", menu=dbase.getMenu(), title="Регистрация")
# -------------------------------------------------------------------------------------
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect(url_for('login'))
#--------------------------------------------------------------------------------------
@app.route('/profile')
@login_required
def profile():
    # return f"""<a href="{url_for('logout')}">Выйти из профиля. </a>
    #             <p>user info: {current_user.get_id()}"""
    return render_template('1profile.html', menu =dbase.getMenu(), title ='Профиль')

# #-------------------------------------------------------------------------------------
#
#   user info: {current_user.get_id()}"""
#---------------------------------------------------------------------------------------
@app.route('/userava')
@login_required
def userava():
    img = current_user.getAvatar(app)
    if not img:
        return ""

    h = make_response(img)
    h.headers['Content-Type'] = 'image/png'
    return h

#---------------------------------------------
@app.route('/upload', methods=["POST", "GET"])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and current_user.verifyExt(file.filename):
            try:
                img = file.read()
                res = dbase.updateUserAvatar(img, current_user.get_id())
                if not res:
                    flash("Ошибка обновления аватара", "error")
                    return redirect(url_for('profile'))
                flash("Аватар обновлен", "success")
            except FileNotFoundError as e:
                flash("Ошибка чтения файла", "error")
        else:
            flash("Ошибка обновления аватара", "error")

    return redirect(url_for('profile'))








if __name__ == "__main__":
    app.run(debug=True)


# hash:
# from werkzeug.security import generate_password_hash, check_password_hash
# hash = generate_password_hash("12345")
# check_password_hash(hash, "12345")




