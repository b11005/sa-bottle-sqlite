# -*- coding: UTF-8 -*-
from bottle import route, run, template

@route('/')
def hello():
    return template('Hello {{string}}', string = 'world')

@route('/greeting/<name>')
def greeting(name):
    return template('I am {{name}}', name = name)

@route('/show/<id:int>')
def show(id):
    return template('show', id = id)

if __name__ == '__main__':
    run(host = 'localhost', port = 8080, debug = True, reload = True)
