from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Usuarios
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean(), default=False)
    profile = db.relationship('Profile', backref="user", uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "name": self.profile.name,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit() 

#Perfil del usuario (GET-UPDATE)
class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.Text, default="")
    avatar = db.Column(db.Text, default="")
    rut = db.Column(db.Text, default="")
    phone = db.Column(db.Text, default="")
    address = db.Column(db.Text, default="")
    password = db.Column(db.Text, default="")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "avatar": self.avatar,
            "rut": self.rut,
            "email": self.user.email,
            "phone": self.phone,
            "address": self.address,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit() 

#Metodos de pago
class PaymentMethod(db.Model):
    __tablename__ = 'paymentMethods'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    card_name = db.Column(db.String(120), nullable=False)
    card_number = db.Column(db.String(120), unique=True, nullable=False)
    exp_date = db.Column(db.String(120), nullable=True)
    cvv2 = db.Column(db.String(120), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "card_name": self.card_name,
            "card_number": self.card_number,
            "exp_date": self.exp_date,
            "cvv2": self.cvv2,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit() 

#Reseñas y puntuaciones (POST-DELETE)
class Rating(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comments = db.Column(db.String(120), unique=True, nullable=False)
    stars = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "comments": self.comments,
            "stars": self.starts,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit() 

#Pedidos (POST)
class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "date": self.date,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit() 

#Detalle de las Ordenes (GET)
class PedidoDetail(db.Model):
    __tablename__ = 'pedidoDetails'
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    dish_id = db.Column(db.Integer, db.ForeignKey('dishes.id'), nullable=False)
    quantity = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "pedido_id": self.pedido_id,
            "dish_id": self.dish_id,
            "quantity": self.quantity,
            "price": self.price,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit() 

#Categoria de Productos (GET-POST-UPDATE-DELETE)
class Categorie(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    country = db.Column(db.String(120), unique=True, nullable=False)
    img = db.Column(db.String(120), unique=True, nullable=False)
    category = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.users_id,
            "country": self.country,
            "img": self.img,
            "category": self.category,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit() 

#Categoria de Restaurantes (GET-POST-UPDATE-DELETE)
class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    country = db.Column(db.String(120), unique=True, nullable=False)
    category = db.Column(db.String(120), unique=True, nullable=False)
    rating = db.Column(db.String(120), unique=True, nullable=False)
    deliveryTime = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.String(120), unique=True, nullable=False)
    img = db.Column(db.String(120), unique=True, nullable=False)
    discount = db.Column(db.String(120), unique=True, nullable=False)
    special = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "categories_id": self.categories_id,
            "name": self.name,
            "country": self.country,
            "category": self.category,
            "rating": self.rating,
            "deliveryTime": self.deliveryTime,
            "price": self.price,
            "img": self.img,
            "discount": self.discount,
            "special": self.special,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit() 
  
#Categoria de Dishes (GET-POST-UPDATE-DELETE)
class Dish(db.Model):
    __tablename__ = 'dishes'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    img = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.String(120), unique=True, nullable=False)
    restaurantId = db.Column(db.String(120), unique=True, nullable=False)
    restaurantName = db.Column(db.String(120), unique=True, nullable=False)
    discount = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "category_id": self.category_id,
            "restaurant_id": self.restaurant_id,
            "name": self.name,
            "img": self.img,
            "description": self.description,
            "price": self.price,
            "restaurantId": self.restaurantId,
            "restaurantName": self.restaurantName,
            "discount": self.discount,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit() 

