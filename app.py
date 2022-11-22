
from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
from flask_pymongo import PyMongo
import database as dbase
from product import Product

db = dbase.dbConnection()

app = Flask (__name__)


@app.route('/')
def home():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products = productsReceived)
    

@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    name = request.form['name']
    lastname = request.form['lastname']
    age = request.form['age']

    if name and lastname and age:
        product = Product(name,lastname,age)
        products.insert_one(product.toDBCollection())
        response=jsonify({
            'name' : name,
            'lastname' : lastname,
            'age' : age

        })
        return redirect(url_for('home'))
    
    

@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name': product_name})
    return redirect(url_for('home'))

@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    lastname = request.form['lastname']
    age = request.form['age']

    if name and lastname and age:
        products.update_one({'name' : product_name},{'$set': {'name' : name, 'lastname' : lastname, 'age' : age}})
        response = jsonify({'message' : 'Usuario' + product_name + 'actualizado correctamente'})
        return redirect(url_for('home'))
    


@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado'+ request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response



if __name__ == '__main__':
    app.run(debug=True, port=4000)