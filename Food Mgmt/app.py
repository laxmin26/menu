from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask import render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menu.db'
db = SQLAlchemy(app)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    is_veg = db.Column(db.Boolean, default=True)
    nutritional_value = db.Column(db.String(100))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        is_veg_str = request.form.get('is_veg', 'false')  # Default value is 'false'
        is_veg = bool(is_veg_str.lower() == 'true')  # Convert string to boolean
        nutritional_value = request.form['nutritional_value']

        new_food = Food(title=title, description=description, is_veg=is_veg, nutritional_value=nutritional_value)
        db.session.add(new_food)
        db.session.commit()

    foods = Food.query.all()
    return render_template('index.html', foods=foods)

@app.route('/delete/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    food = Food.query.get_or_404(food_id)
    db.session.delete(food)
    db.session.commit()
    return jsonify({'message': 'Food item deleted successfully'})

@app.route('/edit/<int:food_id>', methods=['GET'])
def edit_food(food_id):
    food = Food.query.get_or_404(food_id)
    # Assuming you have an 'edit.html' template for editing the food item
    return render_template('edit.html', food=food)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
