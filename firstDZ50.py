
#   Елена, все остальные файлы в папке 'templates' :
# indexDZ.html,   pageone.html,   pagetwo.html,  base50.html.
#
#   Файл styleDZ.css в папке static.

#   Сделал в двух вариантах: с индивидуальным кодом на каждой странице и  с обращением
# к base50.html (задокументировано внизу каждой страницы).
#
#   Вопрос: никак не мог вывести изображение. Путь прописывал с корневого диска и вкладывал
# во все папки - все равно браузер не видит. Просто HTML файл из isual Studio  отображает картинку.



from flask import Flask, render_template, url_for

app = Flask(__name__)

menu =  [ {'name':'Main',     'url': 'index'},
          {'name':'To GOOGLE', 'url': 'pageone'},
          {'name':'TO YAHOO', 'url': 'pagetwo'}]

text1 = 'HOME WORK 50 (page 1)'
text2 = 'HOME WORK 50 (page 2)'


@app.route('/index')
@app.route('/')
def index():
    return render_template('indexDZ.html', title = 'MAIN PAGE.', menu=menu)


@app.route('/pageone')
def pageone():
      return render_template('pageone.html', title = 'Google',menu=menu,
                             text1=text1)

@app.route('/pagetwo')
def pagetwo():
      return render_template('pagetwo.html', title = 'Yahoo',menu=menu,
                              text2=text2)



# @app.route("/profile/<path:username>")
# def profile(username):
#     return f" User of page: {username}  ({'summ:'} {8+3})"



if __name__ == '__main__':
        app.run(debug = True)



