from flask import Flask, request, jsonify, make_response, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from os import environ
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL') # Get var env DB_URL
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)


# Db Model
class Inventory(db.Model):
    __tablename__ = 'inventory' #Table Name

    # Fields & types
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    mac_address = db.Column(db.String(17), nullable=False)
    serial_number = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'mac_address': self.mac_address,
            'serial_number': self.serial_number,
            'manufacturer': self.manufacturer,
            'description': self.description
        }

#db.create_all()  # Create the database tables
with app.app_context():
    db.create_all()

###------------------## Routes ##------------------##

# The inventory will remain here (root)
@app.route('/', methods=['GET'])
def get_all_items():
    try:
        items = Inventory.query.all() # get all items
        return render_template('index.html', items=items)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create an Item (add route)
@app.route('/add', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    
    if request.method == 'POST':
        try:
            name = request.form['name']
            price = request.form['price']
            mac_address = request.form['mac_address']
            serial_number = request.form['serial_number']
            manufacturer = request.form['manufacturer']
            description = request.form['description']

            item = Inventory(
                name=name,
                price=price,
                mac_address=mac_address,
                serial_number=serial_number,
                manufacturer=manufacturer,
                description=description
            )
            db.session.add(item)# Add Item
            db.session.commit() # Commit the changes to the database

            return redirect('/') #Redirect to root(Home)
        
        except Exception as e:
            logging.error(f"Unexpected error occurred: {str(e)}")
            return make_response(jsonify({'message': 'An unexpected error occurred'}), 500)

# Route for Delete Item /delete/id'
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    try:
        item = Inventory.query.get(id)
        if not item:
            abort(404)  # Return a 404 error if the item doesn't exist

        if request.method == 'POST':
            db.session.delete(item) # Delete item
            db.session.commit() # Commit the changes to the database
            return redirect('/')    #redirect to root (home)
        
        return render_template('delete.html', item=item)
    except Exception as e:
        return render_template('error.html', error=str(e)), 500

# Route for Update Item /edit/id'
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = Inventory.query.get(id)
    if not item:
        return f"Item with id={id} not found"

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        mac_address = request.form['mac_address']
        serial_number = request.form['serial_number']
        manufacturer = request.form['manufacturer']
        description = request.form['description']

        # Update the fields of the existing item
        item.name = name
        item.price = price
        item.mac_address = mac_address
        item.serial_number = serial_number
        item.manufacturer = manufacturer
        item.description = description

        # Commit the changes to the database
        db.session.commit()

        return redirect('/')
    return render_template('update.html', item=item)

if __name__ == "__main__":
    app.run(debug=True)