from flask import Flask, render_template, url_for, redirect
from models.book_list import list_of_books




app = Flask(__name__)

@app.route('/')
def welcome():
    return redirect(url_for('homepage'))

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/library')
def selection():
    return render_template('index.html', list_of_books=list_of_books)

@app.route('/expanse')
def book_0():
    return render_template('individual_0.html', list_of_books=list_of_books)

@app.route('/brief_history')
def book_1():
    return render_template('individual_1.html', list_of_books=list_of_books)

@app.route('/game_thrones')
def book_2():
    return render_template('individual_2.html', list_of_books=list_of_books)

@app.route('/space_odyssey')
def book_3():
    return render_template('individual_3.html', list_of_books=list_of_books)

@app.route('/the_shining')
def book_4():
    return render_template('individual_4.html', list_of_books=list_of_books)



if __name__ == "__main__":
    app.run(debug=True)