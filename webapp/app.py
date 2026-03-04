from flask import Flask, render_template, redirect, request, url_for
import requests
import os

app = Flask(__name__)
API_URL = os.getenv('API_URL', 'http://localhost:8000')


@app.route('/')
def index():
    try:
        r = requests.get(f"{API_URL}/products")
        products = r.json()
    except Exception:
        products = []
    return render_template('index.html', products=products)


@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    user_id = request.form.get('user_id', '1')
    product_id = int(request.form['product_id'])
    quantity = int(request.form.get('quantity', 1))
    requests.post(f"{API_URL}/cart/{user_id}/add", json={"product_id": product_id, "quantity": quantity})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
