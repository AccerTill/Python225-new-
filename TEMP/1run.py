from flask import Flask, render_template, \
    url_for, request, flash, session, redirect, abort
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fd2dfgdfggf786hfg6hfg6h7f'

menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]
#-------------------------------------------------------------------------
@app.route("/")
def index():
    print(url_for('index'))
    return render_template('1index.html', menu=menu)
#-------------------------------------------------------------------------
@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('1about.html', title="О сайте", menu=menu)
#-------------------------------------------------------------------------
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено успешно!', category='success')
        else:
            flash('Ошибка отправки!', category='error')
        print(request.form)
    return render_template("1contact.html", title="Обратная связь", menu=menu)
#--------------------------------------------------------------------------
@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f"Пользователь: {username}"
#--------------------------------------------------------------------------
@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "Sergi" and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('1login.html', title="Авторизация", menu=menu)
#---------------------------------------------------------------------------
@app.errorhandler(404)
def pageNotFount(error):
    return render_template('1page404.html', title="Страница не найдена", menu=menu), 404
#---------------------------------------------------------------------------



if __name__ == "__main__":
    app.run(debug=True)


    #
    #     e
    #
    #     # context = {
    #     #     'username': request.form['username'],
    #     #     'email': request.form['email'],
    #     #     'message': request.form['message']
    #     # }
    #     # return render_template("contact.html", **context, title="Обратная связь", menu=menu)


#
#
# @app.route("/profile/<path:username>")
# def profile(username):
#     return f"Пользователь: {username}"






# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('about'))
#     print(url_for('profile', username="selfedu"))





