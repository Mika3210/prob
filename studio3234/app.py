from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id


class Article_2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(5), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Article_2 %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        date = request.form['date']
        time = request.form['time']
        name = request.form['name']
        phone = request.form['phone']

        article_2 = Article_2(date=date, time=time, name=name, phone=phone)

        try:
            db.session.add(article_2)
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка"
    else:
        return render_template("index.html")


@app.route('/catalog.html')
def catalog():
    return render_template("catalog.html")


@app.route('/contacts.html', methods=['POST', 'GET'])
def contacts():
    if request.method == "POST":
        date = request.form['date']
        time = request.form['time']
        name = request.form['name']
        phone = request.form['phone']

        article_2 = Article_2(date=date, time=time, name=name, phone=phone)

        try:
            db.session.add(article_2)
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка"
    else:
        return render_template("contacts.html")


@app.route('/info.html')
def info():
    return render_template("info.html")


@app.route('/login.html', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']

        article = Article(login=login, password=password)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка логина или пароля"
    else:
        return render_template("login.html")


@app.route('/news.html')
def news():
    return render_template("news.html")


@app.route('/price.html')
def price():
    return render_template("price.html")


@app.route('/product.html')
def product():
    return render_template("product.html")


@app.route('/product_2.html')
def product_2():
    return render_template("product_2.html")


if __name__ == '__main__':
    app.run(debug=True)