from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')
@app.route('/profile/<username>')
def profile(username):
    
    return render_template('profile.html',username=username,isActive=False)
# loops
@app.route('/books')
def books():
    books=[{'name':'book1','auther':'abc1','cover':'https://assets.visme.co/templates/banners/thumbnails/i_Fiction-Book-Cover_full.jpg'},
           {'name':'book2','auther':'abc2','cover':'https://assets.visme.co/templates/banners/thumbnails/i_Fiction-Book-Cover_full.jpg'},
           {'name':'book3','auther':'abc3','cover':'https://assets.visme.co/templates/banners/thumbnails/i_Fiction-Book-Cover_full.jpg'}]
    return render_template('book.html',books=books)

app.run(debug=True)