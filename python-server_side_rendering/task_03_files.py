#!/Users/laamrisaid/path/to/venv/bin/python
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    # Read and parse the JSON file
    with open('items.json') as file:
        data = json.load(file)
    items_list = data.get("items", [])
    # Get the list of items or an empty list if missing
    return render_template('items.html', items=items_list)


def read_json(file_path):
    with open(file_path) as file:
        return json.load(file)


def read_csv(file_path):
    products = []
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products = []

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    else:
        error = "Wrong source"

    if not error and product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
