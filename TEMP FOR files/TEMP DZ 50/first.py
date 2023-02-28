from flask import Flask, render_template, url_for

app = Flask(__name__)

menu =  [ {'name':'Main',     'url': 'index'},
          {'name':'About us', 'url': 'about'},
          {'name':'Feedback', 'url': 'contact'}  ]

text = 'Input here something.'
count = [1,2,3,4,5]


@app.route('/index')
@app.route('/')
def index():
    # return render_template('indexDZ.html')
    # print(url_for("index"))
    return render_template('indexDZ.html', title = 'Main (indexDZ.html).', menu=menu)


@app.route('/about')
def about():
      # print(url_for('about'))
      return render_template('pageone.html', title = 'About (pageone.html).',menu=menu,
                             text = text, count = count)


@app.route("/profile/<path:username>")
def profile(username):
    return f" User of page: {username}  ({'summ:'} {8+3})"



if __name__ == '__main__':
        app.run(debug = True)

# types for username: int, float, path (any + /)
