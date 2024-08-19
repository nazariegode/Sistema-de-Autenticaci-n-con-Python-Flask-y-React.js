"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Profile, Rating, PaymentMethod
from datetime import timedelta
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)



#REGISTRO
@api.route('/registro', methods=['POST'])
def register():
    
    name = request.json.get('name', '')
    email = request.json.get('email')
    password = request.json.get('password')
    is_active = request.json.get('is_active', True)

    if not email:
        return jsonify({ "msg": "Email is required!"}), 400
    
    if not password:
        return jsonify({ "msg": "Password is required!"}), 400
    
    found = User.query.filter_by(email=email).first()
    if found:
        return jsonify({ "msg": "Email is already in use"}), 400

    user = User()
    user.email = email
    user.password = generate_password_hash(password)
    user.is_active = is_active

    # Crear el perfil al momento de registrarno
    profile = Profile()
    profile.name = name
    user.profile = profile # vincular el perfil al usuario
    user.save()

    if user:
        return jsonify({
            "status": "success",
            "message": "Registro satisfactorio, por favor inicie sesión"
        })

    return jsonify({
        "status": "fail",
        "message": "Por favor intente mas tarde, póngase en contacto con su administrador. "
    })



#LOGIN
@api.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email:
        return jsonify({ "msg": "Email is required!"}), 400
    
    if not password:
        return jsonify({ "msg": "Password is required!"}), 400
    
    user = User.query.filter_by(email=email, is_active=True).first()

    if not user:
        return jsonify({ "msg": "Credentials not match, please try again"}), 401
    
    if not check_password_hash(user.password, password):
        return jsonify({ "msg": "Credentials not match, please try again"}), 401
    
    expire_at = timedelta(days=1)
    access_token = create_access_token(identity=user.id, expires_delta=expire_at)

    return jsonify({
        "status": "success",
        "message": "Login successfully",
        "access_token": access_token,
        "currentUser": user.serialize()
    }), 200



#PROFILE
@api.route('/profile', methods=['GET'])
@jwt_required() #ruta privada
def profile():
    
    id = get_jwt_identity()

    user = User.query.filter_by(id=id).first()

    if not user.profile:
        #return jsonify({ "msg": "User has not profile"}), 200
        profile = Profile()
        user.profile = profile
        user.update()
        
        return jsonify(user.profile.serialize()), 200

    
    return jsonify(user.profile.serialize()), 200

@api.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    id = get_jwt_identity()
    user = User.query.get_or_404(id)
    data = request.json

    if user.profile:
        profile = user.profile
    else:
        profile = Profile(user_id=id)
    
    profile.name = data.get('name', profile.name)
    profile.phone = data.get('phone', profile.phone)
    profile.address = data.get('address', profile.address)
    
    profile.save()

    return jsonify(profile.serialize()), 200


#USERS ADMIN
#Crear Usuarios
@api.route('/users', methods=['POST'])
@jwt_required() #ruta privada
def create_user():
    data = request.get_json()
    new_user = User(
        avatar=data['avatar'],
        name=data['name'],
        rut=data['rut'],
        email=data['email'],
        phone=data['phone'],
        address=data['address'],
        password=data['password'],
        is_active=data['is_active']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 201

#Obtener todos los usuarios
@api.route('/users', methods=['GET'])
@jwt_required() #ruta privada
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

#Obtener los usuarios por ID
@api.route('/users/<int:id>', methods=['GET'])
@jwt_required() #ruta privada
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.serialize())

#Actualizar Usuarios
@api.route('/users/<int:id>', methods=['PUT'])
@jwt_required() #ruta privada
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.avatar = data.get('avatar', user.avatar)
    user.name = data.get('name', user.name)
    user.rut = data.get('rut', user.rut)
    user.email = data.get('email', user.email)
    user.phone = data.get('phone', user.phone)
    user.address = data.get('address', user.address)
    user.password = data.get('password', user.password)
    user.is_active = data.get('is_active', user.is_active)
    db.session.commit()
    return jsonify(user.serialize())



#RATINGS
#Ratings rutas pendientes: ultimas calificaciones y calificar by user en ese momento
@api.route('/rating', methods=['POST'])
@jwt_required() #ruta privada
def create_ratings():
    data = request.get_json()
    new_rating = Rating(
        user_id=data['user_id'],
        comments=data['comments'],
        stars=data['stars']
    )
    db.session.add(new_rating)
    db.session.commit()
    return jsonify(new_rating.serialize()), 201

#Obtener todos los ratings
@api.route('/ratings', methods=['GET'])
@jwt_required() #ruta privada
def get_all_ratings():
    ratings = Rating.query.all()
    return jsonify([user.serialize() for user in ratings])

#Obtener los ratings por ID
@api.route('/ratings/<int:id>', methods=['GET'])
@jwt_required() #ruta privada
def get_rating_by_id(id):
    rating = Rating.query.get_or_404(id)
    return jsonify(rating.serialize())

#Actualizar ratings
@api.route('/ratings/<int:id>', methods=['PUT'])
@jwt_required() #ruta privada
def update_rating_by_id(id):
    rating = Rating.query.get_or_404(id)
    data = request.get_json()
    rating.user_id = data.get('user_id', rating.user_id)
    rating.comments = data.get('comments', rating.comments)
    rating.stars = data.get('stars', rating.stars)

    db.session.commit()
    return jsonify(rating.serialize())



#PAYMENT METHODS
@api.route('/paymentMethod', methods=['POST'])
@jwt_required() #ruta privada
def create_paymentMethod():
    id = get_jwt_identity()
    user = User.query.filter_by(id=id).first()
    data = request.get_json()
    new_paymentMethod = PaymentMethod(
        user_id=user.id,
        card_name=data['card_name'],
        card_number=data['card_number'],
        exp_date=data['exp_date'],
        cvv2=data['cvv2'],
    )
    
    db.session.add(new_paymentMethod)
    db.session.commit()
    return jsonify(new_paymentMethod.serialize()), 201

#Obtener todos los metodos de pago
@api.route('/paymentMethod', methods=['GET'])
@jwt_required() #ruta privada
def get_all_paymentMethod():
    id = get_jwt_identity()
    user = User.query.filter_by(id=id).first()
    paymentMethods = PaymentMethod.query.filter_by(user_id=user.id)
    return jsonify([payment.serialize() for payment in paymentMethods])

#Obtener los metodos de pago por ID
@api.route('/paymentMethod/<int:payment_id>', methods=['GET'])
@jwt_required() #ruta privada
def get_paymentMethod_by_id(payment_id):
    id = get_jwt_identity()
    user = User.query.filter_by(id=id).first()
    paymentMethod = PaymentMethod.query.filter_by(id=payment_id, user_id=user.id).first()
    return jsonify(paymentMethod.serialize())

#Actualizar metodos de pago
@api.route('/paymentMethod/<int:payment_id>', methods=['PUT'])
@jwt_required() #ruta privada
def update_payment_by_id(payment_id):
    id = get_jwt_identity()
    user = User.query.filter_by(id=id).first()
    paymentMethod = PaymentMethod.query.filter_by(id=payment_id, user_id=user.id).first()
    data = request.get_json()
    paymentMethod.card_name = data.get('card_name', paymentMethod.card_name)
    paymentMethod.card_number = data.get('card_number', paymentMethod.card_number)

    db.session.commit()
    return jsonify(paymentMethod.serialize())


# Eliminar metodo de pago por ID
@api.route('/paymentMethod/<int:payment_id>', methods=['DELETE'])
@jwt_required() # ruta privada
def delete_paymentMethod_by_id(payment_id):
    id = get_jwt_identity()
    user = User.query.filter_by(id=id).first()
    paymentMethod = PaymentMethod.query.filter_by(id=payment_id, user_id=user.id).first()
    
    if not paymentMethod:
        return jsonify({"message": "Método de pago no encontrado"}), 404
    
    db.session.delete(paymentMethod)
    db.session.commit()
    return jsonify({"message": "Método de pago eliminado exitosamente"}), 200

#Modificar contraseña
@api.route('/change-password', methods=['PUT'])
@jwt_required()
def change_password():
    current_user = get_jwt_identity()
    data = request.get_json()

    current_password = data.get('currentPassword')
    new_password = data.get('newPassword')
    confirm_password = data.get('confirmPassword')

    if not current_password or not new_password or not confirm_password:
        return jsonify({"msg": "All fields are required!"}), 400

    if new_password != confirm_password:
        return jsonify({"msg": "New password and confirm password do not match!"}), 400

    user = User.query.filter_by(email=current_user).first()

    if not user or not check_password_hash(user.password, current_password):
        return jsonify({"msg": "Current password is incorrect!"}), 400

    user.password = generate_password_hash(new_password)
    user.update()

    return jsonify({"msg": "Password updated successfully!"}), 200