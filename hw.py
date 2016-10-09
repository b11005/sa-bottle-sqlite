# -*- coding: UTF-8 -*-
# GitHubへのコミットのテスト用
# 本筋とは関係ないので無視してOK
# You can ignore this file because the file is posted in test.

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
