def index():
    with open("templates/indexDZ.html", encoding ='utf -8') as template:
        return template.read()


def blog():
    with open("templates/blog.html", encoding = 'utf -8') as template:
        return template.read()



