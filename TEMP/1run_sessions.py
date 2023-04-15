from flask import Flask, render_template, \
    make_response, url_for, request, session
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '792768467bd0f338eb43484e2a99e4c8ff1728e6'
app.permanent_session_lifetime = datetime.timedelta(days=10) # - время жизни сессии (см. ниже)

#-----------------------------------------------------------------------
@app.route("/")
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # обновление данных сессии
        print("  add 1 number of session !  ")
    else:
        session['visits'] = 1  # запись данных в сессию

    return f"<h1>Main Page</h1>Число просмотров: {session['visits']}"
#--------------------------------------------------------------------
data = [1, 2, 3, 4]

@app.route("/session")
def session_data():
 #   session.permanent = True # время жизни сессии
    session.permanent = False # время жизни сессии не сохраняется
    if 'data' not in session:
        session['data'] = data
    else:
        session['data'][1] += 1
        session.modified = True

    return f"session['data']: {session['data']}"
#--------------------------------------------------------------------

# import os
# os.urandom(20).hex()
# app.config['SECRET_KEY'] = ''


if __name__ == "__main__":
    app.run(debug=True)
