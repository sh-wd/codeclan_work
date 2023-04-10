from app import app
from flask import render_template, redirect, url_for,request
from models.book_list import *
from models.book import *

@app.route('/library')
def library():
    return render_template('index.html', book_list=book_list)

@app.route('/')
def index():
    return redirect(url_for('library'))

@app.route('/library/<index>')
def show_book(index):
    selected_book = book_list[int(index)]
    return render_template('show.html', index=selected_book)

@app.route('/library', methods=['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    new_book = Book(book_title, book_author, book_genre)
    add_new_book(new_book)
    return render_template('index.html', book_list=book_list)
     

@app.route('/library/delete/<book_title>')
def delete(book_title):
    remove_book(book_title)
    return redirect('/library')