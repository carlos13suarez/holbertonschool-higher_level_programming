from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
        return data

def read_csv_file(filepath):
    data = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            data.append(row)
    return data

def read_sqlite_db(dbpath):
    try:
        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        return [
                {'id': row[0], 'name': row[1], 'category': row[2], 'price':row[3]}
                for row in rows
                ]
    except Exception as e:
        raise RuntimeError(f"Error reading SQLite database: {e}")


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
    with open('items.json', 'r') as file:
        data = json.load(file)

    items_list = data.get('items', [])

    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template(
                'product_display.html',
                error_message="Wrong source"
                )

    try:
        if source == 'json':
            products = read_json_file('products.json')
        elif source == 'csv':
            products = read_csv_file('products.csv')
        elif source == 'sql':
            products = read_sqlite_db('products.db')
    except Exception as e:
        return render_template(
                'product_display.html',
                error_message=f"Couldn't read file: {e}"
                )

    if product_id:
        try:
            product_id = int(product_id)
            products = [
                    product for product in products
                    if product['id'] == product_id
                    ]
        except Exception as e:
            return render_template(
                    'product_display.html',
                    error_message="Wrong ID"
                    )
        if not products:
            return render_template(
                    'product_display.html',
                    error_message="Product not found"
                    )

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
