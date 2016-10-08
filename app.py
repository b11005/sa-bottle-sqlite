# coding: UTF-8

# ４種類のパッケージを入れる & 設定
# datetime
from datetime import datetime

# bottle関係
import bottle
from bottle import get, post, run
from bottle import request, template, redirect
from bottle import HTTPError

# sqlalchemy関係
from sqlalchemy import create_engine, Column, Integer, Unicode, DateTime, UnicodeText
from sqlalchemy.ext.declarative import declarative_base

# bottle-sqlalchemy関係
from bottle.ext import sqlalchemy

# wtforms関係
from wtforms.form import Form
from wtforms import validators
from wtforms import StringField, IntegerField, TextAreaField

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo = True)

# bottle-sqlalchemyの設定
plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword = 'db',
    create = True,
    commit = True,
    use_kwargs = False
)

bottle.install(plugin)


# 書籍DB用のモデル作成
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key = True)
    title = Column(Unicode(100), nullable = False)
    price = Column(Integer, nullable = False)
    memo = Column(UnicodeText)
    created_at = Column(DateTime, default = datetime.now)

    def __repr__(self):
        return "<Book('%s', '%s', '%s', '%s')>" % (self.title, self.price, self.memo, self.created_at)


# フォーム定義と入力チェック
class BookForm(Form):

    title = StringField(u'タイトル', [
        validators.required(message = u'入力してください'),
        validators.length(min = 1, max = 100, message = u'入力してください')
    ])

    price = IntegerField(u'価格', [
        validators.required(message = u'数値で入力してください')
    ])

    memo = TextAreaField(u'メモ', [
        validators.required(message = u'入力してください')
    ])


# ルーティング定義
# 一覧用のGET
@get('/books/add')
def new(db):

    form = BookForm()
    return template('edit', form = form, request = request)

# 登録用のGET / POST
@post('/books/add')
def create(db):

    form = BookForm(request.forms.decode())

    if form.validate():

        book = Book(
            title = form.title.data,
            price = form.price.data,
            memo = form.memo.data
        )

        db.add(book)
        redirect("/books")

    else:
        return template('edit', form = form, request = request)

@get('/books')
def index(db):

    books = db.query(Book).all()
    return template('index', books = books, request = request)

# 編集用のGET / POST
@get('/books/<id:int>/edit')
def edit(db, id):

    book = db.query(Book).get(id)

    # 指定したIDに対応する書籍がない場合
    if not book:
        return HTTPError(404, u'書籍が見つかりません')

    form = BookForm(request.POST, book)

    return template('edit', book = book, form = form, request = request)

@post('/books/<id:int>/edit')
def update(db, id):

    book = db.query(Book).get(id)

    # 指定したIDに対応する書籍がない場合
    if not book:
        return HTTPError(404, u'書籍が見つかりません')

    form = BookForm(request.forms.decode())

    if form.validate():

        book.title = form.title.data
        book.price = form.price.data
        book.memo = form.memo.data

        redirect("/books")

    else:
        return template('edit', form = form, request = request)

@post('/books/<id:int>/delete')
def destroy(db, id):

    book = db.query(Book).get(id)

    if not book:
        return HTTPError(404, u'書籍が見つかりません')

    db.delete(book)
    redirect("/books")

if __name__ == '__main__':
    run(host = 'localhost', port = 8080, debug = True, reloader = True)
