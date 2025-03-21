#!/Users/laamrisaid/path/to/venv/bin/python
import json
from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
