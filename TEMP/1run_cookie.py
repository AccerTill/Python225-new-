from flask import Flask, render_template, make_response, url_for, request

app = Flask(__name__)

menu = [{"title": "Главная", "url": "/"},
        {"title": "Добавить статью", "url": "/add_post"}]

@app.route("/")
def index():
    return "<h1>Main Page _ cookies </h1>"
#-----------------------------------------------------------------------------
@app.route("/login")
def login():
    log = ""
    if request.cookies.get('logged'):
        log = request.cookies.get('logged')

    res = make_response(f"<h1>Форма авторизации</h1>logged:  :   {log} - log.")
    res.set_cookie("logged", "yes_information_of_cookie")
    return res

# ---Сlearing of cookie-------------------------------------------------------
@app.route("/logout")
def logout():
    res = make_response("Вы больше не авторизованы на этой странице!</p>")
    res.set_cookie("logged", "", 0)
    return res

if __name__ == "__main__":
    app.run(debug=True)