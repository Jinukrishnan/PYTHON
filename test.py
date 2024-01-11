from flask import Flask

new=Flask(__name__)
@new.route('/profile/<username>')
def home(username):
    return '<h1>hello %s</h1>' % username
@new.route('/contact/<int:id>')
def contact(id):
    return '<h1>contact %d</h1>' % id
new.run()