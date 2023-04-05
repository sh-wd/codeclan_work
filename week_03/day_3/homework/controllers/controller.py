from app import app
from flask import render_template
from models.book_store import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders = orders)

@app.route('/orders/<int:id>')
def single_order(id):
    return render_template('order.html', title='Single Order', order=orders[id-1])