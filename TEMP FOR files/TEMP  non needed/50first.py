from flask import Flask, render_template, url_for


app = Flask(__name__)

menu =  [ {'name':'Main',     'url': 'index'},
          {'name':'About us', 'url': 'about'},
          {'name':'Feedback', 'url': 'contact'}  ]


@app.route('/index')
@app.route('/')
def index():
    # return render_template('indexDZ.html')
    # print(url_for("index"))
    return render_template('index.html', title = 'Main (index.html).', menu=menu)


@app.route('/about')
def about():
      # print(url_for('about'))
      return render_template('about.html', title = 'About (about.html).',menu=menu,
                             text = text, count = count)


@app.route("/profile/<path:username>")
def profile(username):
    return f" User of page: {username}  ({'summ:'})"



if __name__ == '__main__':
        app.run(debug = True)

# types for username: int, float, path (any + /)
print('dz50')